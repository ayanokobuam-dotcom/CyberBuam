#!/usr/bin/env python3
"""Hand-authored content.json: intro/keyTerms/interactives/quiz per topic,
built on top of the raw text extracted by build-content.py (raw-content.json).
rawText is pulled in automatically from raw-content.json; everything else
below is authored by hand and reviewed against the source PDFs."""
import json
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "content.json"
RAW = Path(__file__).resolve().parents[1] / "raw-content.json"

raw = json.loads(RAW.read_text(encoding="utf-8"))


def raw_text_for(module_id_hint, topic_id):
    for m in raw["modules"]:
        for t in m["topics"]:
            if t["id"] == topic_id:
                parts = []
                if t["intro"]:
                    parts.append(t["intro"])
                for p in t["pdfSources"]:
                    parts.append(p["text"])
                return "\n\n---\n\n".join(parts)
    return ""


topic1 = {
    "id": "1-inside-a-computer-system",
    "title": "Inside a Computer System",
    "summary": "The physical building blocks of a computer and what happens the instant you press the power button.",
    "intro": (
        "Every computer, from a phone to a data center server, is built from the same handful of "
        "parts. Think of it like a body: each component has a job, and they only come alive together "
        "once you hit the power button."
    ),
    "keyTerms": [
        {"term": "CPU", "def": "The Brains. Executes instructions and does the actual computing."},
        {"term": "RAM", "def": "Short-term Memory. Holds data the CPU is actively using; wiped on shutdown."},
        {"term": "Motherboard", "def": "Skeleton and Nerves. The board that connects every other component together."},
        {"term": "PSU", "def": "Heart and Lungs. Converts and delivers power to every component."},
        {"term": "GPU", "def": "Visual Cortex. Renders images and video; also great at parallel math."},
        {"term": "HDD / SSD", "def": "Long-term Memory. Stores files and the OS even when the power is off."},
        {"term": "Firmware (UEFI/BIOS)", "def": "The low-level program that wakes up hardware before an OS exists."},
        {"term": "POST", "def": "Power-On Self Test. A quick health check the firmware runs on every component."},
        {"term": "Bootloader", "def": "The small program that finds and hands control to the operating system."},
    ],
    "interactives": [
        {
            "type": "hotspot-diagram",
            "title": "Tap a component to see its job",
            "layout": "scatter",
            "items": [
                {"id": "cpu", "icon": "🧠", "label": "CPU", "short": "The Brains", "detail": "Executes every instruction your programs need. Faster CPU = faster thinking, but it does nothing without the other organs around it."},
                {"id": "ram", "icon": "⚡", "label": "RAM", "short": "Short-term memory", "detail": "Holds whatever the CPU is working on right now. It's fast but forgetful — everything in RAM disappears when the power cuts."},
                {"id": "motherboard", "icon": "🦴", "label": "Motherboard", "short": "Skeleton & nerves", "detail": "The board every other part plugs into. It's the nervous system carrying signals between CPU, RAM, storage, and everything else."},
                {"id": "psu", "icon": "❤️", "label": "PSU", "short": "Heart & lungs", "detail": "Pulls power from the wall and converts it into the exact voltages every component needs. Nothing turns on without it."},
                {"id": "gpu", "icon": "👁️", "label": "GPU", "short": "Visual cortex", "detail": "Specialized at drawing pixels and doing thousands of small calculations at once — used for graphics, but also AI and cracking passwords."},
                {"id": "storage", "icon": "🗄️", "label": "HDD / SSD", "short": "Long-term memory", "detail": "Where your files and operating system live permanently. Unlike RAM, it keeps its data with the power off — that's how the computer remembers anything between reboots."},
            ],
        },
        {
            "type": "step-flow",
            "title": "What happens when you press the power button",
            "mode": "sequence",
            "steps": [
                {"icon": "🔘", "title": "Press the power button", "detail": "A signal tells the PSU to start letting power flow to every component — like waking up and taking your first breath."},
                {"icon": "🔥", "title": "Firmware starts", "detail": "The UEFI (formerly called BIOS) wakes up first. It's the low-level program that exists before any operating system does."},
                {"icon": "🩺", "title": "POST — Power-On Self Test", "detail": "The firmware quickly checks that the CPU, RAM, and other core parts are actually working before going further."},
                {"icon": "💽", "title": "Select a boot device", "detail": "The firmware looks at the configured device order (SSD, USB, network...) to find where the operating system lives."},
                {"icon": "🚀", "title": "Bootloader starts", "detail": "A small program on that device takes over and loads the real operating system into RAM, handing it control of the machine."},
            ],
        },
    ],
    "conclusion": raw_text_for(None, "1-inside-a-computer-system"),  # placeholder, replaced below
    "quiz": [
        {"q": "Which component is most accurately described as the computer's 'short-term memory'?", "choices": ["CPU", "RAM", "SSD", "PSU"], "answer": 1, "explain": "RAM holds active data for instant access but loses everything once power is cut — just like short-term memory."},
        {"q": "What is the very first thing that happens after you press the power button?", "choices": ["The bootloader loads the OS", "POST checks the hardware", "A signal tells the PSU to start supplying power", "The GPU renders the login screen"], "answer": 2, "explain": "Power has to flow before anything else can happen — that's the PSU's job, triggered the instant you press the button."},
        {"q": "What does POST stand for, and what does it do?", "choices": ["Power-On Self Test — checks hardware health at boot", "Power Output Signal Trigger — turns on the fans", "Primary Operating System Trace — logs boot errors", "Processor Overload Safety Timer — prevents overheating"], "answer": 0, "explain": "POST is the firmware's quick health check on core components before boot continues."},
        {"q": "Which component is often called the 'skeleton and nerves' of a computer?", "choices": ["GPU", "Motherboard", "HDD/SSD", "RAM"], "answer": 1, "explain": "The motherboard physically connects every other component and carries signals between them."},
        {"q": "Why is hardware boot behavior something cyber security professionals care about?", "choices": ["It's never relevant to security", "The boot process is sometimes a target for attackers", "It only affects gaming performance", "It has nothing to do with firmware"], "answer": 1, "explain": "Attacks on firmware/bootloaders (e.g. bootkits) are a real category of attack — that's exactly why this room flags the boot process as important later on."},
    ],
}

topic2 = {
    "id": "2-computer-type",
    "title": "Computer Types",
    "summary": "Not every computer looks like a laptop — the same building blocks get reshaped for very different jobs.",
    "intro": (
        "Computers hide in more places than you'd think: in your pocket, inside your fridge, behind an "
        "automatic door. Each type trades mobility, power, and reliability differently depending on the "
        "job it needs to do."
    ),
    "keyTerms": [
        {"term": "Laptop", "def": "Portable, everyday computing — trades raw performance for battery life and mobility."},
        {"term": "Desktop", "def": "Stays in one place, uses wall power, better cooling — consistent performance over mobility."},
        {"term": "Workstation", "def": "Built for precision and reliability on professional tasks like simulation or 3D rendering."},
        {"term": "Server", "def": "No screen/keyboard needed — exists to provide services to many users over a network."},
        {"term": "Smartphone", "def": "Pocket-sized computer optimized for battery life and constant connectivity."},
        {"term": "Tablet", "def": "Touch-first computer with a larger screen than a phone, still highly portable."},
        {"term": "IoT device", "def": "Network-connected device with a single purpose — a thermostat, doorbell, or fitness tracker."},
        {"term": "Embedded computer", "def": "A computer built into another device, often working silently for years unnoticed."},
    ],
    "interactives": [
        {
            "type": "matching",
            "title": "Match each computer type to what it's built for",
            "pairs": [
                {"left": "Laptop", "right": "Portable everyday computing"},
                {"left": "Desktop", "right": "Sustained performance at a fixed location"},
                {"left": "Workstation", "right": "Precision and reliability for professional tasks"},
                {"left": "Server", "right": "Providing services to many users over a network"},
                {"left": "Smartphone", "right": "Pocket-sized, optimized for battery and connectivity"},
                {"left": "IoT device", "right": "Network-connected, single purpose (e.g. smart doorbell)"},
                {"left": "Embedded computer", "right": "Built into another device, often invisible to the user"},
            ],
        },
        {
            "type": "step-flow",
            "title": "Why computers come in different flavors",
            "mode": "sequence",
            "steps": [
                {"icon": "🔋", "title": "Mobility costs power", "detail": "Smaller, portable computers must sacrifice sustained performance to stay battery-friendly."},
                {"icon": "💰", "title": "Reliability costs money", "detail": "Servers and critical systems use redundancy — extra power supplies, extra disks — to avoid failure, which isn't cheap."},
                {"icon": "🎯", "title": "Purpose shapes everything", "detail": "You touch a phone. You ask a server for information. An IoT device works quietly without demanding attention. There's no single 'best' computer — only the right tool for the job."},
            ],
        },
    ],
    "conclusion": "",
    "quiz": [
        {"q": "What's the key difference between an IoT device and an embedded computer?", "choices": ["IoT devices are always faster", "IoT devices connect to a network; embedded computers might not", "Embedded computers always have a screen", "There is no real difference"], "answer": 1, "explain": "Both can be small and single-purpose — but IoT devices report data or receive commands over a network, while embedded computers can quietly do their job with no connectivity at all."},
        {"q": "Which computer type is defined by having no screen or keyboard, serving many users over a network?", "choices": ["Workstation", "Server", "Tablet", "Laptop"], "answer": 1, "explain": "A server exists purely to provide a service to other systems, so it doesn't need a screen or keyboard."},
        {"q": "Why does a desktop typically outperform a laptop on sustained heavy workloads?", "choices": ["Desktops are always newer", "Desktops use wall power and have better cooling, so they don't need to throttle", "Laptops don't have a CPU", "Desktops are always more portable"], "answer": 1, "explain": "Laptops must balance battery life and heat in a small chassis; desktops use continuous wall power and better cooling to sustain performance longer."},
        {"q": "A workstation is best described as being built for...", "choices": ["Maximum portability", "Casual browsing only", "Precision and reliability on professional tasks (e.g. simulation, rendering)", "Running only as a network service"], "answer": 2, "explain": "Workstations trade portability for the raw, reliable power professional workloads need."},
    ],
}

topic3 = {
    "id": "3-client-server-basics",
    "title": "Client-Server Basics",
    "summary": "How one computer asks another for something — from ordering a pizza to a browser's GET request.",
    "intro": (
        "Almost everything on the internet is a conversation between a client that asks for something "
        "and a server that answers. The pizza-delivery analogy makes it click: someone orders, someone "
        "fulfills the order, and the order itself follows a very specific format."
    ),
    "keyTerms": [
        {"term": "Client", "def": "The one who initiates the request — like Alice ordering a pizza."},
        {"term": "Server", "def": "The one who fulfills the request — like Luigi's Pizzas making the order."},
        {"term": "HTTP(S)", "def": "The stateless client-server protocol used to request and serve web pages."},
        {"term": "Stateless", "def": "Each request is handled independently — the server doesn't remember your last request by default."},
        {"term": "Session / Cookie", "def": "A mechanism websites use to fake 'memory' on top of a stateless protocol, e.g. staying logged in."},
        {"term": "GET", "def": "The HTTP method used to request (read) a resource — the most common method a browser sends."},
        {"term": "Status code", "def": "A number telling you if the request succeeded — e.g. 200 OK."},
        {"term": "Host", "def": "The name of the server you're requesting resources from."},
    ],
    "interactives": [
        {
            "type": "step-flow",
            "title": "A request, animated: ordering a pizza vs. loading a page",
            "mode": "linkflow",
            "actors": ["Client", "Server"],
            "steps": [
                {"icon": "🙋", "from": "client", "title": "Client sends a request", "detail": "Alice tells Bob what she wants → your browser sends a GET request for a page."},
                {"icon": "🛵", "from": "client", "title": "The request travels", "detail": "Bob drives to Luigi's → the HTTP request travels over the network to the host's address."},
                {"icon": "🍕", "from": "server", "title": "Server processes it", "detail": "Luigi makes the pizza → the web server looks up the requested file and prepares a response."},
                {"icon": "📦", "from": "server", "title": "Server sends a response", "detail": "The order is handed over → the server replies with a status code, headers, and the response body (the page content)."},
                {"icon": "🏠", "from": "client", "title": "Client receives it", "detail": "Bob brings the pizza home → the browser renders the page it received."},
            ],
        },
        {
            "type": "flip-cards",
            "title": "HTTP response fields",
            "cards": [
                {"front": "Scheme", "back": "Which protocol was used: HTTP or HTTPS."},
                {"front": "Host", "back": "The name of the host you requested resources from."},
                {"front": "Filename", "back": "Which file was requested — '/' actually means index.html."},
                {"front": "Address", "back": "The IP address the website is hosted at."},
                {"front": "Status", "back": "Whether the request succeeded — e.g. '200 OK'."},
            ],
        },
    ],
    "conclusion": "",
    "quiz": [
        {"q": "In the client-server model, who always initiates the communication?", "choices": ["The server", "The client", "Both at the same time", "Neither — it's automatic"], "answer": 1, "explain": "Just like Alice ordering pizza before Luigi makes it — the client always starts the conversation."},
        {"q": "What does it mean that HTTP is 'stateless'?", "choices": ["It never works across state lines", "Each request is processed independently, with no memory of previous requests", "It only works on secure connections", "It can only send one request ever"], "answer": 1, "explain": "Without cookies/sessions layered on top, the server treats every request as if it's the first one it's ever seen from you."},
        {"q": "A '200 OK' you see in dev tools is an example of a...", "choices": ["Host", "Status code", "Scheme", "Filename"], "answer": 1, "explain": "Status codes tell you whether the request succeeded — 200 means success."},
        {"q": "Which HTTP method is most associated with simply requesting (reading) a resource?", "choices": ["DELETE", "GET", "PATCH", "CONNECT"], "answer": 1, "explain": "GET is the most common method — used every time a browser loads a page."},
    ],
}

topic4 = {
    "id": "4-virtualisation-basics",
    "title": "Virtualisation Basics",
    "summary": "How one physical machine gets split into many safe, isolated virtual ones.",
    "intro": (
        "'One server, one application' used to be the rule — expensive, wasteful, and slow to scale. "
        "Virtualization broke that rule by letting one physical machine safely pretend to be many."
    ),
    "keyTerms": [
        {"term": "Virtualization", "def": "Enables a single physical computer to act like multiple separate computers."},
        {"term": "Hypervisor", "def": "The 'manager' software that creates and runs the virtual machines."},
        {"term": "Virtual Machine (VM)", "def": "A whole virtual computer inside the real one, with its own OS."},
        {"term": "Container", "def": "A small, isolated box for one app that shares the host's OS instead of running a full OS itself."},
        {"term": "Container Image", "def": "A pre-packed template used to create containers."},
        {"term": "Network Port", "def": "A numbered entry point apps use to talk to each other over a network."},
        {"term": "Type 1 Hypervisor", "def": "Runs directly on physical hardware — fast, efficient, used in servers and data centers."},
        {"term": "Type 2 Hypervisor", "def": "Runs inside an existing OS — easier to install, ideal for learning and small setups."},
    ],
    "interactives": [
        {
            "type": "hotspot-diagram",
            "title": "The virtualization stack, bottom to top",
            "layout": "stack",
            "items": [
                {"id": "hardware", "icon": "🖥️", "label": "Physical Hardware", "short": "The real machine", "detail": "The actual CPU, RAM, and storage sitting in a data center or under your desk."},
                {"id": "hypervisor", "icon": "🧑‍💼", "label": "Hypervisor", "short": "The building manager", "detail": "Divides the physical machine into isolated slices, giving each one its own share of CPU, memory, and storage — and keeps them from interfering with each other."},
                {"id": "vms", "icon": "🏠", "label": "Virtual Machines", "short": "Isolated 'apartments'", "detail": "Each VM behaves like a full, separate computer with its own OS, even though several of them share the same physical hardware underneath."},
                {"id": "apps", "icon": "📦", "label": "Apps / Containers", "short": "What actually runs", "detail": "The website, database, or service you actually care about — running inside a VM, or even more lightweight, inside a container that shares the host OS."},
            ],
        },
        {
            "type": "matching",
            "title": "Match the use case to the right hypervisor type",
            "pairs": [
                {"left": "Production Server", "right": "Type 1 — runs directly on hardware"},
                {"left": "Data Center", "right": "Type 1 — runs directly on hardware"},
                {"left": "Testing Malicious Files", "right": "Type 2 — runs inside a host OS, easy to isolate/reset"},
                {"left": "Kali Linux for learning", "right": "Type 2 — easy to install, ideal for learning"},
            ],
        },
    ],
    "conclusion": "",
    "quiz": [
        {"q": "Before virtualization, what was the standard rule for running services?", "choices": ["One server = one application", "One server = unlimited applications", "Servers were never used for single apps", "Applications ran only on client devices"], "answer": 0, "explain": "Each service typically got its own dedicated physical machine — expensive and inefficient."},
        {"q": "What is a hypervisor's main job?", "choices": ["Physically cools the server", "Creates and manages virtual machines, dividing hardware between them", "Writes application code", "Replaces the need for a CPU"], "answer": 1, "explain": "The hypervisor is 'the building manager' — it slices up one physical machine into several isolated virtual ones."},
        {"q": "Which hypervisor type runs directly on the physical hardware, favored for production servers and data centers?", "choices": ["Type 1", "Type 2", "Type 3", "None — hypervisors always run inside an OS"], "answer": 0, "explain": "Type 1 hypervisors run straight on the hardware, making them fast and efficient for professional environments."},
        {"q": "What's the key difference between a VM and a container?", "choices": ["A VM is a full virtual computer with its own OS; a container shares the host's OS", "They are exactly the same thing", "Containers are always slower than VMs", "VMs cannot run applications"], "answer": 0, "explain": "A VM emulates a whole machine including its own OS, while a container is a lighter-weight box that shares the host operating system."},
        {"q": "Which of these is NOT a listed benefit of virtualization?", "choices": ["Cost savings", "Better resource usage", "Guaranteed internet speed increase", "Faster deployment"], "answer": 2, "explain": "The benefits covered are cost savings, better resource usage, safe testing, faster deployment, flexibility, portability, scalability, and centralized management — internet speed isn't one of them."},
    ],
}

topics = [topic1, topic2, topic3, topic4]

# pull in real conclusion + rawText from raw-content.json instead of placeholders
for t in topics:
    for m in raw["modules"]:
        for rt in m["topics"]:
            if rt["id"] == t["id"]:
                t["conclusion"] = rt["conclusion"]
                body = []
                for p in rt["pdfSources"]:
                    body.append(f"### {p['source']}\n\n{p['text']}")
                t["rawText"] = "\n\n".join(body)

content = {
    "modules": [
        {
            "id": "pre-security-computer-fundamentals",
            "title": "Pre Security — Computer Fundamentals",
            "topics": topics,
        }
    ]
}

OUT.write_text(json.dumps(content, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"wrote {OUT}")
