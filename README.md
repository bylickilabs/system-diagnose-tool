# 🧠 System Diagnose Tool – Kali/Linux CLI Analyzer

|![System Diagnostics](./assets/system_diagnostics_neon.png)|
|---|

Ein interaktives, farbcodiertes CLI-Diagnosetool für Kali Linux und andere Debian-Systeme. Entwickelt zur schnellen Erkennung und automatisierten Analyse von System-, Netzwerk- und Sicherheitsproblemen – mit optionalen Root-Rechten, erweiterten Netzwerktools und modularer Erweiterbarkeit.

---

## 📚 Inhaltsverzeichnis

- [🧠 System Diagnose Tool – Kali/Linux CLI Analyzer](#-system-diagnose-tool--kalilinux-cli-analyzer)
- [📚 Inhaltsverzeichnis](#-inhaltsverzeichnis)
- [📦 Voraussetzungen](#-voraussetzungen)
- [📥 Installation](#-installation)
  - [1. Repository klonen](#1-repository-klonen)
  - [2. Abhängigkeiten installieren](#2-abhängigkeiten-installieren)
  - [3. Optional: Tools für Netzwerkdiagnose installieren](#3-optional-tools-für-netzwerkdiagnose-installieren)
- [🛡️ Root-Rechte korrekt einrichten](#️-root-rechte-korrekt-einrichten)
- [▶️ Anwendung starten](#️-anwendung-starten)
- [🧩 Menüübersicht](#-menüübersicht)
- [🛠 Funktionsübersicht](#-funktionsübersicht)
- [📁 Projektstruktur](#-projektstruktur)
- [📝 Lizenz](#-lizenz)

---

## 📦 Voraussetzungen

| Komponente     | Benötigt     | Beschreibung                        |
|----------------|--------------|-------------------------------------|
| OS             | ✅ Linux      | Debian-basiert (Kali empfohlen)     |
| Python         | ✅ 3.8+       | Für psutil, colorama                |
| Netzwerktools  | 🔸 optional   | `net-tools`, `traceroute`, `dnsutils`, `ufw` |

---

## 📥 Installation

### 1. Repository klonen

```bash
git clone https://github.com/dein-benutzername/system-diagnose-tool.git
cd system-diagnose-tool
