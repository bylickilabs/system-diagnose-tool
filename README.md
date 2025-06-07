|![Python](https://img.shields.io/badge/python-3.8%2B-blue?style=flat-square)|![Platform](https://img.shields.io/badge/platform-Kali%20Linux%20%7C%20Debian-lightgrey?style=flat-square)|![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)|![Status](https://img.shields.io/badge/status-stable-brightgreen?style=flat-square)|
|---|---|---|---|

> system-diagnose-tool
- Interaktives CLI-Diagnosetool für Kali &amp; Linux
  - prüft Systemzustand, Netzwerke, Dienste und Sicherheitsaspekte automatisiert im Terminal. Farbcodiert. Modular. Erweiterbar.

<br>

---

<br>

- [📚 Inhaltsverzeichnis](#-inhaltsverzeichnis)
- [📦 Voraussetzungen](#-voraussetzungen)
- [📥 Installation](#-installation)
  - [1. Repository klonen](#1-repository-klonen)
  - [2. Abhängigkeiten installieren](#2-abhängigkeiten-installieren)
  - [3. Ausführungsrechte setzen (optional)](#3-ausführungsrechte-setzen-optional)
- [▶️ Anwendung starten](#️-anwendung-starten)
- [🧩 Optional: Tools installieren](#-optional-tools-installieren)
- [🛡️ Hinweise zur Ausführung](#️-hinweise-zur-ausführung)
- [📝 Lizenz](#-lizenz)

<br>

---

<br>

📦 Voraussetzungen
> 1. Betriebssystem: Kali Linux oder eine Debian-basierte Linux-Distribution

```yarn
Python-Version: 3.8+
Administratorrechte für bestimmte Funktionen (z. B. Netzwerkscan, Dienststatus)
Optional installierte Tools:
net-tools (für netstat)
ufw (Firewall)
traceroute
dnsutils (für nslookup)
```

<br>

---

<br>

📥 Installation
  - Repository klonen

```yarn
git clone https://github.com/dein-benutzername/system-diagnose-tool.git
cd system-diagnose-tool
```

<p>
> 2. Abhängigkeiten installieren
