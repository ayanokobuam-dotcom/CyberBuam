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
        {"term": "Firmware (UEFI/BIOS)", "def": "The low-level program that wakes up hardware before an OS exists. UEFI is the modern standard; the older term 'BIOS' does the same job but has mostly been replaced by it."},
        {"term": "POST", "def": "Power-On Self Test. A quick health check the firmware runs on every component."},
        {"term": "Bootloader", "def": "The small program that finds the OS on the boot device, transfers it into RAM, then hands control over to it."},
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
                {"icon": "🚀", "title": "Bootloader starts", "detail": "A small program on that device takes over, transfers the operating system into RAM, and once that's done, the firmware hands control of the machine over to the OS."},
            ],
        },
        {
            "type": "matching",
            "title": "Match the body-analogy to the real component",
            "pairs": [
                {"left": "The Brains", "right": "CPU"},
                {"left": "Short-term Memory", "right": "RAM"},
                {"left": "Skeleton and Nerves", "right": "Motherboard"},
                {"left": "Heart and Lungs", "right": "PSU"},
                {"left": "Visual Cortex", "right": "GPU"},
                {"left": "Long-term Memory", "right": "HDD / SSD"},
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
        {"q": "What's the relationship between BIOS and UEFI?", "choices": ["They're unrelated technologies", "UEFI is the modern replacement for BIOS — BIOS does the same job but has mostly been superseded", "BIOS replaced UEFI in modern PCs", "BIOS only exists inside GPUs"], "answer": 1, "explain": "UEFI (Unified Extensible Firmware Interface) is the modern standard; you'll still hear 'BIOS' used loosely for the same role."},
        {"q": "Once the bootloader finds the OS on the boot device, where does it transfer the OS before handing over control?", "choices": ["Directly into the GPU", "Into RAM", "Into the PSU", "It doesn't transfer it anywhere — it runs straight off the disk"], "answer": 1, "explain": "The bootloader moves the OS from storage into RAM; only after that does the firmware hand control over to it."},
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
        {"term": "Laptop", "def": "Portable, everyday computing — trades raw performance for battery life and mobility. Has a screen and keyboard."},
        {"term": "Desktop", "def": "Stays in one place, uses wall power, better cooling — consistent performance over mobility. Has a screen and keyboard."},
        {"term": "Workstation", "def": "Built for precision and reliability on professional tasks like simulation or 3D rendering. Has a screen and keyboard."},
        {"term": "Server", "def": "No screen or keyboard needed — exists to provide services to many users over a network, running continuously."},
        {"term": "Smartphone", "def": "Pocket-sized computer optimized for battery life and constant connectivity — e.g. an iPhone or Android phone."},
        {"term": "Tablet", "def": "Touch-first computer with a larger screen than a phone, still highly portable — e.g. an iPad or drawing tablet."},
        {"term": "IoT device", "def": "Network-connected device with a single purpose — e.g. a thermostat, smart doorbell, or fitness tracker."},
        {"term": "Embedded computer", "def": "A computer built into another device, often working silently for years unnoticed — e.g. a coffee maker controller, automatic door sensor, or lamp dimmer chip."},
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
        {
            "type": "hotspot-diagram",
            "title": "Spot the hidden computer",
            "layout": "scatter",
            "items": [
                {"id": "smartphone", "icon": "📱", "label": "Smartphone", "short": "In your pocket", "detail": "An iPhone or Android phone packs a full computer optimized for battery life and constant connectivity — the most powerful computer most people carry."},
                {"id": "tablet", "icon": "🖊️", "label": "Tablet", "short": "Touch-first, bigger screen", "detail": "An iPad or drawing tablet — a touch-first computer with a larger screen than a phone, still highly portable."},
                {"id": "iot", "icon": "🌡️", "label": "IoT Device", "short": "Connected, single-purpose", "detail": "A thermostat, smart doorbell, or fitness tracker — connects to a network to report data or receive commands."},
                {"id": "embedded", "icon": "🚪", "label": "Embedded Computer", "short": "Invisible, everywhere", "detail": "Sophia walked through automatic doors every day at Nova Labs without realizing a tiny embedded computer inside the door frame was detecting her movement and signaling the motor to open — invisible, reliable, everywhere. Also hides inside coffee maker controllers and lamp dimmer chips, often with zero network connection."},
            ],
        },
        {
            "type": "flip-cards",
            "title": "Screen & keyboard? Comparing the 4 types you sit in front of",
            "cards": [
                {"front": "Laptop", "back": "Screen & Keyboard: Yes. Portable everyday computing — trades performance for battery life."},
                {"front": "Desktop", "back": "Screen & Keyboard: Yes. Sustained performance at a fixed location — wall power and better cooling than a laptop."},
                {"front": "Workstation", "back": "Screen & Keyboard: Yes. Precision and reliability for professional tasks like simulation or 3D rendering."},
                {"front": "Server", "back": "Screen & Keyboard: No. Runs continuously, answering requests from many users at once — no one sits in front of it."},
            ],
        },
    ],
    "conclusion": "",
    "quiz": [
        {"q": "What's the key difference between an IoT device and an embedded computer?", "choices": ["IoT devices are always faster", "IoT devices connect to a network; embedded computers might not", "Embedded computers always have a screen", "There is no real difference"], "answer": 1, "explain": "Both can be small and single-purpose — but IoT devices report data or receive commands over a network, while embedded computers can quietly do their job with no connectivity at all."},
        {"q": "Which computer type is defined by having no screen or keyboard, serving many users over a network?", "choices": ["Workstation", "Server", "Tablet", "Laptop"], "answer": 1, "explain": "A server exists purely to provide a service to other systems, so it doesn't need a screen or keyboard."},
        {"q": "Why does a desktop typically outperform a laptop on sustained heavy workloads?", "choices": ["Desktops are always newer", "Desktops use wall power and have better cooling, so they don't need to throttle", "Laptops don't have a CPU", "Desktops are always more portable"], "answer": 1, "explain": "Laptops must balance battery life and heat in a small chassis; desktops use continuous wall power and better cooling to sustain performance longer."},
        {"q": "A workstation is best described as being built for...", "choices": ["Maximum portability", "Casual browsing only", "Precision and reliability on professional tasks (e.g. simulation, rendering)", "Running only as a network service"], "answer": 2, "explain": "Workstations trade portability for the raw, reliable power professional workloads need."},
        {"q": "Which of these is a real-world example of an embedded computer rather than an IoT device?", "choices": ["A smart doorbell that sends you phone alerts", "A fitness tracker that syncs to an app", "An automatic door sensor that silently opens a door with no network connection", "A thermostat you control from your phone"], "answer": 2, "explain": "IoT devices connect to a network; embedded computers, like the sensor in Nova Labs' automatic doors, can work invisibly with no connectivity at all."},
        {"q": "In the Screen & Keyboard comparison, which of these four types is the only one marked 'No'?", "choices": ["Laptop", "Desktop", "Workstation", "Server"], "answer": 3, "explain": "Laptops, desktops, and workstations all have a screen and keyboard — a server doesn't need either since no one sits in front of it."},
        {"q": "Which of these is the clearest real-world example of a smartphone?", "choices": ["A drawing tablet", "An iPhone or Android phone", "A smart doorbell", "A coffee maker controller"], "answer": 1, "explain": "iPhones and Android phones are the room's named examples of pocket-sized, always-connected smartphones."},
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
        {"term": "DNS", "def": "Domain Name Service — resolves a hostname to a server's IP address, just like a GPS resolves a place name into coordinates."},
        {"term": "Port", "def": "A number identifying a specific service running on a server — like a specific door for takeaway vs. dine-in vs. delivery at the same restaurant."},
        {"term": "Protocol", "def": "The shared rules a client and server use to talk: which commands are understood, how a request is structured, what syntax is used, and how faulty requests are handled."},
        {"term": "RFC", "def": "Request for Comments — the official specification documents that define standards like HTTP, including its 9 core methods."},
    ],
    "interactives": [
        {
            "type": "step-flow",
            "title": "A request, animated: ordering a pizza vs. loading a page",
            "mode": "linkflow",
            "actors": ["Client", "Server"],
            "steps": [
                {"icon": "🙋", "from": "client", "title": "Client sends a request", "detail": "Alice tells Bob what she wants → your browser sends a GET request for a page."},
                {"icon": "🧭", "from": "client", "title": "DNS resolves the address", "detail": "Bob only knows the name 'Luigi's Pizza' — he needs an address. Your browser only knows a hostname → DNS resolves it into an IP address, exactly like a GPS turning a place name into coordinates."},
                {"icon": "🛵", "from": "client", "title": "The request travels", "detail": "Bob drives to Luigi's specific door for takeaway → the HTTP request travels to the host's IP address, on the correct port for that service."},
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
        {
            "type": "hotspot-diagram",
            "title": "The 9 HTTP methods, defined in the HTTP RFCs",
            "layout": "scatter",
            "items": [
                {"id": "get", "icon": "📥", "label": "GET", "short": "Read a resource", "detail": "Retrieves a resource from the server — the most common method, used every time your browser loads a page."},
                {"id": "post", "icon": "📤", "label": "POST", "short": "Submit new data", "detail": "Sends new data to the server, e.g. submitting a form or uploading a file."},
                {"id": "put", "icon": "🔁", "label": "PUT", "short": "Replace a resource", "detail": "Replaces a resource entirely with the data you send."},
                {"id": "delete", "icon": "🗑️", "label": "DELETE", "short": "Remove a resource", "detail": "Asks the server to delete the specified resource."},
                {"id": "patch", "icon": "🩹", "label": "PATCH", "short": "Partially update", "detail": "Applies a partial update to a resource instead of replacing the whole thing."},
                {"id": "head", "icon": "🎩", "label": "HEAD", "short": "Headers only", "detail": "Same as GET but returns only the headers, not the body — useful for checking if a resource exists."},
                {"id": "options", "icon": "❓", "label": "OPTIONS", "short": "Ask what's allowed", "detail": "Asks the server which methods it supports for a given resource."},
                {"id": "connect", "icon": "🔌", "label": "CONNECT", "short": "Open a tunnel", "detail": "Establishes a tunnel to the server, often used to route HTTPS through a proxy."},
                {"id": "trace", "icon": "🪞", "label": "TRACE", "short": "Echo the request", "detail": "Echoes the received request back — mainly used for debugging."},
            ],
        },
        {
            "type": "matching",
            "title": "Match the concept to its pizza-delivery analogy",
            "pairs": [
                {"left": "DNS", "right": "Works like a GPS — turns a name into an address"},
                {"left": "Port", "right": "Works like a specific door — each service has its own"},
                {"left": "Protocol", "right": "Works like a shared language — the rules both sides follow"},
                {"left": "Client", "right": "Alice, the one who starts the order"},
                {"left": "Server", "right": "Luigi's Pizzas, the one who fulfills it"},
            ],
        },
    ],
    "conclusion": "",
    "quiz": [
        {"q": "In the client-server model, who always initiates the communication?", "choices": ["The server", "The client", "Both at the same time", "Neither — it's automatic"], "answer": 1, "explain": "Just like Alice ordering pizza before Luigi makes it — the client always starts the conversation."},
        {"q": "What does it mean that HTTP is 'stateless'?", "choices": ["It never works across state lines", "Each request is processed independently, with no memory of previous requests", "It only works on secure connections", "It can only send one request ever"], "answer": 1, "explain": "Without cookies/sessions layered on top, the server treats every request as if it's the first one it's ever seen from you."},
        {"q": "A '200 OK' you see in dev tools is an example of a...", "choices": ["Host", "Status code", "Scheme", "Filename"], "answer": 1, "explain": "Status codes tell you whether the request succeeded — 200 means success."},
        {"q": "Which HTTP method is most associated with simply requesting (reading) a resource?", "choices": ["DELETE", "GET", "PATCH", "CONNECT"], "answer": 1, "explain": "GET is the most common method — used every time a browser loads a page."},
        {"q": "What does DNS do?", "choices": ["Encrypts your traffic", "Resolves a hostname to a server's IP address", "Stores your browsing history", "Compresses web pages"], "answer": 1, "explain": "DNS works like a GPS for the internet, turning a name like tryhackme.com into an IP address."},
        {"q": "In the Luigi's takeaway analogy, what does a Port represent?", "choices": ["The pizza itself", "A specific door for a specific service on the same server", "The delivery driver", "The menu"], "answer": 1, "explain": "Just like Luigi's uses door A for takeaway and door B for dine-in, a single server can run multiple services, each identified by a different port."},
        {"q": "Which of the following formally defines HTTP's methods and rules?", "choices": ["CSS specifications", "RFC (Request for Comments) documents", "The client's browser settings", "DNS records"], "answer": 1, "explain": "HTTP is standardized in RFC documents — that's where its 9 core methods are formally defined."},
        {"q": "Which HTTP method removes a resource from the server?", "choices": ["GET", "POST", "DELETE", "HEAD"], "answer": 2, "explain": "DELETE is the method that asks the server to remove the specified resource."},
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
        {"term": "Hypervisor", "def": "The 'manager' software that creates and runs the virtual machines, and manages their whole lifecycle — start, stop, pause, clone, delete."},
        {"term": "Virtual Machine (VM)", "def": "A whole virtual computer inside the real one, with its own OS."},
        {"term": "Container", "def": "A small, isolated box for one app that shares the host's OS instead of running a full OS itself."},
        {"term": "Container Image", "def": "A pre-packed template used to create containers."},
        {"term": "Network Port", "def": "A numbered entry point apps use to talk to each other over a network."},
        {"term": "Type 1 Hypervisor", "def": "Runs directly on physical hardware — fast, efficient, used in servers and data centers."},
        {"term": "Type 2 Hypervisor", "def": "Runs inside an existing OS — easier to install, ideal for learning and small setups. Tools like Oracle VirtualBox and VMware Workstation are Type 2 hypervisors."},
        {"term": "Kernel", "def": "The part of an operating system that talks directly to hardware and manages resources like memory and running programs — containers share the host's kernel instead of bringing their own."},
        {"term": "Docker", "def": "The most common open-source platform for building, deploying, and running containers."},
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
                {"id": "apps", "icon": "📦", "label": "Apps / Containers", "short": "What actually runs", "detail": "The website, database, or service you actually care about — running inside a VM, or even more lightweight, inside a container that shares the host OS's kernel."},
            ],
        },
        {
            "type": "matching",
            "title": "Match the use case to the right hypervisor type",
            "pairs": [
                {"left": "Production Server", "right": "Type 1 — runs directly on hardware"},
                {"left": "Data Center", "right": "Type 1 — runs directly on hardware"},
                {"left": "Database Server", "right": "Type 1 — runs directly on hardware"},
                {"left": "Testing Malicious Files", "right": "Type 2 — runs inside a host OS, easy to isolate/reset"},
                {"left": "Software Testing", "right": "Type 2 — runs inside a host OS, easy to isolate/reset"},
                {"left": "Kali Linux for learning", "right": "Type 2 — easy to install, ideal for learning"},
            ],
        },
        {
            "type": "flip-cards",
            "title": "The 8 benefits of virtualization",
            "cards": [
                {"front": "Cost savings", "back": "Fewer physical servers to buy, power, cool, and house."},
                {"front": "Better resource usage", "back": "Multiple VMs share one machine instead of each app getting its own underused server — some servers sat at just 5-20% usage before virtualization."},
                {"front": "Safe testing", "back": "Isolate a VM to test malicious files or risky changes without endangering the host machine."},
                {"front": "Faster deployment", "back": "Spinning up a new VM takes minutes, not the days or weeks needed to buy and rack a new physical server."},
                {"front": "Flexibility", "back": "Resize a VM's CPU, memory, or storage on demand instead of buying new hardware."},
                {"front": "Portability", "back": "A VM or container image can move between hosts and run consistently anywhere."},
                {"front": "Scalability", "back": "Add more VMs or containers as demand grows, without buying new physical hardware."},
                {"front": "Centralized Management", "back": "A single tool like a Virtualization Manager lets you monitor and control every VM and host from one dashboard."},
            ],
        },
        {
            "type": "step-flow",
            "title": "A day managing AutoGalo's VMs",
            "mode": "sequence",
            "steps": [
                {"icon": "🚨", "title": "Mail-SERVER goes down", "detail": "Everyone at AutoGalo stops receiving email. The Mail-SERVER lab machine is found sitting in an Error state inside the Virtualization Manager."},
                {"icon": "🔁", "title": "A restart fixes it", "detail": "Restarting the Mail-SERVER VM brings it back to a healthy running state — no more errors."},
                {"icon": "🆕", "title": "Create Marketing-VM", "detail": "The marketing team needs a VM for their website: 4 CPU cores, 8GB memory, 100GB disk. Created in seconds — no new hardware to buy."},
                {"icon": "📊", "title": "Check host capacity", "detail": "HV-PROD-01 still has room for more VMs. HV-PROD-02 is almost at 100% capacity — worth flagging to the manager. HV-BACKUP-01 is disconnected and hosts nothing."},
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
        {"q": "What does the kernel do, and why does it matter for containers?", "choices": ["It's a cooling component; irrelevant to containers", "It's the part of the OS that talks to hardware and manages resources — containers share the host's kernel instead of bringing their own", "It's a type of hypervisor", "It only exists inside VMs, never on the host"], "answer": 1, "explain": "Because containers share the host's kernel rather than running a full OS, they start faster and use fewer resources than VMs — but must match the host's OS type."},
        {"q": "What is Docker?", "choices": ["A hardware brand for servers", "The most common open-source platform for building, deploying, and running containers", "A type of Type 1 hypervisor", "A cloud storage service"], "answer": 1, "explain": "Docker is the easiest way to deploy containers in a VM — an open-source platform built around containerization."},
        {"q": "In the AutoGalo scenario, what specs were used to create the Marketing-VM?", "choices": ["2 CPU cores, 4GB memory, 50GB disk", "4 CPU cores, 8GB memory, 100GB disk", "8 CPU cores, 16GB memory, 200GB disk", "1 CPU core, 2GB memory, 20GB disk"], "answer": 1, "explain": "The Marketing-VM was created with 4 CPU cores, 8GB memory, and a 100GB disk to host the marketing team's website."},
    ],
}

topic5 = {
    "id": "5-cloud-computing-fundamentals",
    "title": "Cloud Computing Fundamentals",
    "summary": "Why almost nothing you use today lives on one computer anymore — and how renting resources over the internet changed the rules.",
    "intro": (
        "Your laptop can't serve users on the other side of the world without lag, and it definitely "
        "can't grow the moment your app goes viral. Cloud computing solves that by letting you rent "
        "computing power over the internet instead of owning every server yourself."
    ),
    "keyTerms": [
        {"term": "Cloud Computing", "def": "Using computing resources — servers, storage, networking — over the internet instead of running everything on your own machine."},
        {"term": "IaaS", "def": "Infrastructure as a Service. Rent the basic building blocks (servers, storage, network); you manage the OS and app yourself."},
        {"term": "PaaS", "def": "Platform as a Service. The provider manages infrastructure and OS; you just build, deploy, and run your app."},
        {"term": "SaaS", "def": "Software as a Service. A ready-to-use application over the internet — the provider manages everything, you just log in."},
        {"term": "Public Cloud", "def": "Shared infrastructure open to anyone — affordable, scalable, no hardware to manage."},
        {"term": "Private Cloud", "def": "Dedicated infrastructure for one organization — more control, customization, and compliance for sensitive data."},
        {"term": "Hybrid Cloud", "def": "A mix of public and private clouds working together, e.g. keeping data private while scaling publicly."},
        {"term": "EC2", "def": "Amazon's virtual servers — created, resized, and destroyed on demand."},
        {"term": "Instance Type", "def": "Describes how powerful a virtual server is (e.g. t2, t3, m5) — bigger instance types mean more CPU/RAM but higher cost."},
        {"term": "Region", "def": "A geographical location where your cloud resources live, e.g. Europe or North America."},
        {"term": "Major Cloud Vendors", "def": "AWS is the industry leader; other major vendors include Microsoft Azure, Google Cloud Platform (GCP), Alibaba Cloud, IBM Cloud, and Oracle Cloud, each with different specialties."},
    ],
    "interactives": [
        {
            "type": "hotspot-diagram",
            "title": "Renting a place to live: IaaS vs PaaS vs SaaS",
            "layout": "stack",
            "items": [
                {"id": "iaas", "icon": "🏗️", "label": "IaaS", "short": "Renting empty land", "detail": "You get the raw plot — servers, storage, networking. Building the house (installing the OS, configuring, running your app) is entirely on you."},
                {"id": "paas", "icon": "🏠", "label": "PaaS", "short": "Renting an unfurnished apartment", "detail": "Walls, plumbing, and electricity (infrastructure + OS) are already handled by the provider. You just move your furniture in — build, deploy, and run your app."},
                {"id": "saas", "icon": "🏨", "label": "SaaS", "short": "Renting a furnished hotel room", "detail": "Everything is done for you. You just walk in and use it — like opening Gmail or Zoom in a browser."},
            ],
        },
        {
            "type": "matching",
            "title": "Match the cloud deployment type to who'd use it",
            "pairs": [
                {"left": "Startup launching a public app", "right": "Public Cloud — affordable, scales instantly, no infrastructure to manage"},
                {"left": "Bank / healthcare / government", "right": "Private Cloud — control, customization, compliance for sensitive data"},
                {"left": "E-commerce site during a sale spike", "right": "Hybrid Cloud — keeps sensitive data private while scaling publicly on demand"},
            ],
        },
        {
            "type": "step-flow",
            "title": "How servers evolved to the cloud",
            "mode": "sequence",
            "steps": [
                {"icon": "🖥️", "title": "Physical Servers", "detail": "One dedicated machine per application — expensive, slow to scale, and often sitting at low utilization."},
                {"icon": "🧩", "title": "Virtualization", "detail": "A hypervisor splits one physical machine into many isolated VMs, so multiple applications finally share hardware safely."},
                {"icon": "📦", "title": "Containers", "detail": "Lighter-weight than VMs — apps package with just what they need and share the host's kernel, so they start almost instantly."},
                {"icon": "☁️", "title": "Cloud", "detail": "Virtualization, containers, and automation combine into on-demand, pay-as-you-go infrastructure you rent over the internet instead of own."},
            ],
        },
        {
            "type": "step-flow",
            "title": "Deploy and optimize an AWS environment",
            "mode": "sequence",
            "steps": [
                {"icon": "🌍", "title": "Pick a region", "detail": "Choose the geographical location where your resources will live, e.g. Europe or North America."},
                {"icon": "🖥️", "title": "Create application-interface", "detail": "A t3.micro EC2 instance to host the app itself — small and cheap, since it's just serving the interface."},
                {"icon": "🧪", "title": "Create two study machines", "detail": "study-machine-1 and study-machine-2, both m5.large — more powerful instances for users to practice cyber security skills on."},
                {"icon": "💵", "title": "Check the Billing section", "detail": "See exactly how much each instance is costing — the two powerful study machines are driving most of the cost."},
                {"icon": "⏸️", "title": "Stop unused study machines", "detail": "Since users haven't started yet, stop study-machine-1 and study-machine-2. Billing drops considerably — you only pay for what's running."},
            ],
        },
        {
            "type": "flip-cards",
            "title": "Major cloud vendors",
            "cards": [
                {"front": "AWS", "back": "Industry leader — the most extensive service offerings and global reach."},
                {"front": "Microsoft Azure", "back": "Strong competitor, especially in enterprise and hybrid cloud environments."},
                {"front": "Google Cloud Platform (GCP)", "back": "Known for powerful data analytics, AI, and machine learning tools."},
                {"front": "Alibaba Cloud", "back": "A major player in Asia, offering competitive cloud services globally."},
                {"front": "IBM Cloud", "back": "Focuses on hybrid cloud and AI-driven solutions for businesses."},
                {"front": "Oracle Cloud", "back": "Focuses on enterprise applications and databases."},
            ],
        },
    ],
    "conclusion": "",
    "quiz": [
        {"q": "What's the main advantage of the cloud over hosting an app on a single personal computer?", "choices": ["It's always completely free", "It can scale on demand and stay reachable worldwide without you owning the hardware", "It removes the need for any code", "It only works for gaming"], "answer": 1, "explain": "The cloud lets your app grow, shrink, and stay available globally by renting shared infrastructure instead of being limited to one machine."},
        {"q": "In the 'renting a place to live' analogy, which service model is like renting a furnished hotel room where everything is already done for you?", "choices": ["IaaS", "PaaS", "SaaS", "None of these"], "answer": 2, "explain": "SaaS hands you a complete, ready-to-use application — the provider manages the infrastructure, OS, and the app itself."},
        {"q": "Why would a bank most likely choose a Private Cloud over a Public Cloud?", "choices": ["Private clouds are always cheaper", "Private clouds offer more control, customization, and compliance for sensitive data", "Public clouds cannot be used by banks at all", "There's no real difference between them"], "answer": 1, "explain": "Organizations handling sensitive data often need the extra control and compliance guarantees a dedicated private cloud provides."},
        {"q": "What does an EC2 instance represent in AWS?", "choices": ["A billing plan", "A virtual computer/server you can create, resize, and destroy on demand", "A type of database", "A physical data center"], "answer": 1, "explain": "EC2 (Elastic Compute Cloud) is AWS's virtual server offering — just like a real computer, it has CPU and RAM and can run applications."},
        {"q": "Which of these is NOT one of the cloud benefits covered in this room?", "choices": ["Scalability", "Pay only for what you use", "Guaranteed permanent hardware ownership", "High availability"], "answer": 2, "explain": "The cloud's whole point is that you don't need to own permanent hardware — you rent resources on-demand instead."},
        {"q": "What comes right after Virtualization in the evolution from physical servers to the cloud?", "choices": ["Cloud", "Containers", "Physical Servers", "Nothing — Virtualization was the last step"], "answer": 1, "explain": "The order is Physical Servers → Virtualization → Containers → Cloud."},
        {"q": "In the AWS deployment scenario, why did stopping the study machines reduce the bill?", "choices": ["It permanently deleted all data", "Cloud billing charges for running instances — stopping unused ones means you stop paying for them", "AWS gives a discount for stopping machines", "It has no effect on billing"], "answer": 1, "explain": "Pay-as-you-go billing means cost tracks what's actually running — stopping the idle study machines immediately cut the bill."},
        {"q": "Which cloud vendor is specifically known for its strength in data analytics, AI, and machine learning tools?", "choices": ["Oracle Cloud", "IBM Cloud", "Google Cloud Platform (GCP)", "Alibaba Cloud"], "answer": 2, "explain": "GCP is called out specifically for its data analytics, AI, and machine learning strengths."},
    ],
}

topics = [topic1, topic2, topic3, topic4, topic5]

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
