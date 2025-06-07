import os
import subprocess
import psutil
import shutil
import sys
import logging
from datetime import datetime, timedelta
from colorama import Fore, Style, init

init(autoreset=True)

# Logging-Konfiguration
logging.basicConfig(filename="diagnose_tool.log", level=logging.INFO, format='%(asctime)s %(message)s')

def log_and_print(message, color=Fore.CYAN):
    print(color + message)
    logging.info(message)

# Prüfungen definieren mit Fehlerbehandlung
def check_disk():
    try:
        usage = psutil.disk_usage('/')
        status = f"Festplatte fast voll ({usage.percent}% belegt)" if usage.percent > 80 else f"Festplatte OK ({usage.percent}% belegt)"
        log_and_print(status, Fore.RED if usage.percent > 80 else Fore.GREEN)
    except Exception as e:
        log_and_print(f"Festplattenprüfung Fehler: {e}", Fore.RED)

def check_memory():
    try:
        mem = psutil.virtual_memory()
        status = f"Hoher RAM Verbrauch ({mem.percent}% verwendet)" if mem.percent > 80 else f"RAM OK ({mem.percent}% verwendet)"
        log_and_print(status, Fore.RED if mem.percent > 80 else Fore.GREEN)
    except Exception as e:
        log_and_print(f"RAM Prüfung Fehler: {e}", Fore.RED)

def check_cpu():
    try:
        cpu_load = psutil.cpu_percent(interval=1)
        status = f"Hohe CPU-Auslastung ({cpu_load}%)" if cpu_load > 80 else f"CPU OK ({cpu_load}% ausgelastet)"
        log_and_print(status, Fore.RED if cpu_load > 80 else Fore.GREEN)
    except Exception as e:
        log_and_print(f"CPU Prüfung Fehler: {e}", Fore.RED)

def check_network():
    try:
        subprocess.check_output(['ping', '-c', '2', '8.8.8.8'], stderr=subprocess.STDOUT)
        log_and_print("Netzwerk OK (Internet erreichbar)", Fore.GREEN)
    except subprocess.CalledProcessError:
        log_and_print("WARNUNG: Kein Internetzugriff", Fore.RED)

def check_system_updates():
    try:
        result = subprocess.check_output(['apt-get', '-s', 'upgrade']).decode()
        status = "System Updates OK (keine Updates verfügbar)" if "0 upgraded, 0 newly installed" in result else "WARNUNG: Systemupdates verfügbar"
        log_and_print(status, Fore.GREEN if "0 upgraded, 0 newly installed" in result else Fore.YELLOW)
    except Exception as e:
        log_and_print(f"Systemupdates Prüfung Fehler: {e}", Fore.RED)

def check_open_ports():
    try:
        result = subprocess.check_output(['netstat', '-tuln']).decode()
        log_and_print("Offene Ports:\n" + result)
    except Exception as e:
        log_and_print(f"Portprüfung Fehler: {e}", Fore.RED)

# Menü anzeigen
def show_menu():
    menu_items = [
        "1. Alle Checks ausführen",
        "2. Festplattenprüfung",
        "3. RAM Prüfung",
        "4. CPU Prüfung",
        "5. Netzwerkprüfung",
        "6. Systemupdateprüfung",
        "7. Offene Ports anzeigen",
        "0. Beenden"
    ]
    print(Style.BRIGHT + "\nSystem Diagnose Menü:")
    for item in menu_items:
        print(item)

# Hauptfunktion modular gestaltet
def main():
    checks = [check_disk, check_memory, check_cpu, check_network, check_system_updates, check_open_ports]

    while True:
        show_menu()
        choice = input("Wähle eine Option: ")
        if choice == '1':
            for check in checks:
                check()
        elif choice in map(str, range(2, 8)):
            checks[int(choice) - 2]()
        elif choice == '0':
            log_and_print("Programm beendet.")
            sys.exit(0)
        else:
            log_and_print("Ungültige Eingabe, bitte erneut versuchen.", Fore.YELLOW)

# Starte die Anwendung
if __name__ == "__main__":
    main()
