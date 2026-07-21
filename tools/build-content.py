#!/usr/bin/env python3
"""One-off extractor: walks the Cyberbuam data folder and dumps raw text
(intro/conclusion .txt + PDF text) into raw-content.json for hand-authoring
of interactives/quiz on top. Re-run whenever new source files are added."""
import json
import re
from pathlib import Path

import pdfplumber

ROOT = Path(__file__).resolve().parents[2] / "Cyberbuam"
OUT = Path(__file__).resolve().parents[1] / "raw-content.json"


def read_txt(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8", errors="replace").strip()


def find_txt_ci(folder: Path, name: str) -> Path:
    for f in folder.iterdir():
        if f.is_file() and f.name.lower() == name.lower():
            return f
    return folder / name


def extract_pdf(path: Path) -> str:
    text_parts = []
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            t = page.extract_text() or ""
            text_parts.append(t)
    return "\n".join(text_parts).strip()


def natural_key(s: str):
    return [int(t) if t.isdigit() else t.lower() for t in re.split(r"(\d+)", s)]


def clean_title(name: str) -> str:
    name = re.sub(r"^\d+\.\s*", "", name)
    name = re.sub(r"^Module\s*\d+\s*_?\s*", "", name, flags=re.IGNORECASE)
    return name.strip()


def slugify(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def find_leaf_dirs(root: Path):
    """Any directory that directly contains a .txt or .pdf file is a 'topic' leaf.
    Its parent chain (relative to root) is the module/course breadcrumb."""
    leaves = []
    for dirpath, dirnames, filenames in __import__("os").walk(root):
        d = Path(dirpath)
        if any(f.lower().endswith((".txt", ".pdf")) for f in filenames):
            leaves.append(d)
    return leaves


def main():
    leaf_dirs = find_leaf_dirs(ROOT)
    modules_by_path = {}
    module_order = []

    for topic_dir in sorted(leaf_dirs, key=lambda d: natural_key(str(d.relative_to(ROOT)))):
        rel_parts = topic_dir.relative_to(ROOT).parts
        module_path_parts = rel_parts[:-1]  # everything above the topic folder
        module_key = "/".join(module_path_parts) if module_path_parts else "general"
        module_title = " / ".join(clean_title(p) for p in module_path_parts) if module_path_parts else "General"

        if module_key not in modules_by_path:
            modules_by_path[module_key] = {
                "id": slugify(module_key) or "general",
                "title": module_title,
                "topics": [],
            }
            module_order.append(module_key)

        intro = read_txt(find_txt_ci(topic_dir, "introduction.txt"))
        conclusion = read_txt(find_txt_ci(topic_dir, "conclusion.txt"))
        pdfs = sorted(
            (f for f in topic_dir.iterdir() if f.suffix.lower() == ".pdf"),
            key=lambda f: natural_key(f.name),
        )
        pdf_texts = []
        for pdf in pdfs:
            print(f"extracting: {pdf}")
            pdf_texts.append({"source": pdf.name, "text": extract_pdf(pdf)})

        modules_by_path[module_key]["topics"].append(
            {
                "id": slugify(topic_dir.name),
                "title": clean_title(topic_dir.name),
                "intro": intro,
                "conclusion": conclusion,
                "pdfSources": pdf_texts,
            }
        )

    modules = [modules_by_path[k] for k in module_order]
    OUT.write_text(json.dumps({"modules": modules}, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
