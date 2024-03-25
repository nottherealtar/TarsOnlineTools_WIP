import scapy.all as scapy
from scapy.all import ARP, Ether, srp
import speedtest
from colorama import Fore, Back, Style, init
from rich.console import Console
from rich.table import Table
import requests
import netifaces
import ipaddress
import os
import socket
import platform
import logging
import time
import threading

# Set up logging
logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

init(autoreset=True)

console = Console()

def main_menu():
    """
    This function displays the main menu and handles the user's selection.
    """
    while True:
        try:
            console.rule("[bold green]Main Menu")
            table = Table(show_header=True, header_style="bold magenta")
            table.add_column("Option", style="dim", width=12)
            table.add_column("Tool", style="dim", width=20)
            table.add_row("1", "IP Tools")
            table.add_row("2", "LAN Tools")
            table.add_row("3", "Speedtest")
            table.add_row("4", "Speedtest Advanced")
            table.add_row("5", "Device Information")
            table.add_row("q", "Quit")
            console.print(table)
            
            user_input = input("Select a tool: ")
            
            if user_input == '1':
                ip_tools_submenu()
            elif user_input == '2':
                lan_tools()
            elif user_input == '3':
                speedtest_tool()
            elif user_input == '4':
                speedtest_advanced()
            elif user_input == '5':
                device_info()
            elif user_input.lower() == 'q':
                break
            else:
                console.print(Fore.RED + "Invalid input!" + Style.RESET_ALL)
        except Exception as e:
            logging.error("Exception occurred", exc_info=True)
            console.print(Fore.RED + "An error occurred: " + str(e) + Style.RESET_ALL)

def network_monitoring():
    """
    This function sniffs network packets and prints a summary of each packet.
    Sniffing continues until the user interrupts the process (usually with Ctrl+C).
    """
    print("Network Monitoring")
    print("Sniffing network packets. Press Ctrl+C to stop.")
    try:
        scapy.sniff(prn=lambda x: x.summary())
    except KeyboardInterrupt:
        print("\nStopped sniffing.")

def print_ip_range():
    """
    This function prints the IP range of the network interface that is currently up.
    """
    for interface in netifaces.interfaces():
        addresses = netifaces.ifaddresses(interface)
        if netifaces.AF_INET in addresses:
            ip_info = addresses[netifaces.AF_INET][0]
            network = ipaddress.ip_network(f"{ip_info['addr']}/{ip_info['netmask']}", strict=False)
            print(f"The IP range for {interface} is {network}")

def network_scanning(ip_range):
    """
    This function scans a range of IP addresses and identifies the devices connected to the network.
    It sends ARP requests to the IP range and prints the IP and MAC addresses of the devices that respond.
    """
    print("Scanning IP range...")
    ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip_range), timeout=2, verbose=0)

    for sent, received in ans:
        print(received.sprintf(r"%ARP.psrc% %Ether.src%"))

def ip_tools_submenu():
    """
    This function displays the IP Tools submenu and handles the user's selection.
    """
    while True:
        print(Fore.YELLOW + "\nIP Tools:")
        print("1. Network Monitoring")
        print("2. Device Identification")
        print("3. Print IP Range")
        print("4. Back to Main Menu" + Style.RESET_ALL)

        selection = input("\nEnter your selection: ")

        if selection == '1':
            network_monitoring()
        elif selection == '2':
            print_ip_range()
            ip_range = input("Enter the IP range to scan (e.g., 192.168.1.0/24): ")
            network_scanning(ip_range)
        elif selection == '3':
            print_ip_range()
        elif selection == '4':
            break
        else:
            print(Fore.RED + "Invalid selection!" + Style.RESET_ALL)

def lan_tools():
    """
    This function displays the LAN Tools submenu and handles the user's selection.
    """
    while True:
        print(Fore.YELLOW + "\nLAN Tools:")
        print("1. Network Scanning")
        print("2. Back to Main Menu" + Style.RESET_ALL)

        selection = input("\nEnter your selection: ")

        if selection == '1':
            print_ip_range()
            ip_range = input("Enter the IP range to scan (e.g., 192.168.1.0/24): ")
            network_scanning(ip_range)
        elif selection == '2':
            break
        else:
            print(Fore.RED + "Invalid selection!" + Style.RESET_ALL)

def spinner():
    """
    This function creates a simple text-based spinner.
    """
    while True:
        for cursor in '|/-\\':
            yield cursor

def spinner():
    """
    This function creates a simple text-based spinner.
    """
    while True:
        for cursor in '|/-\\':
            yield cursor

def speedtest_tool():
    """
    This function performs a speedtest and prints the download and upload speed.
    """
    print("Speedtest")
    st = speedtest.Speedtest()

    print("Running speedtest...", end="")
    spin = spinner()

    results = {}
    def run_speedtest():
        results['download_speed'] = st.download() / 1024 / 1024
        results['upload_speed'] = st.upload() / 1024 / 1024

    speedtest_thread = threading.Thread(target=run_speedtest)
    speedtest_thread.start()

    while speedtest_thread.is_alive():
        print(next(spin), end='\r', flush=True)
        time.sleep(0.1)

    print(f"\nDownload: {results['download_speed']:.2f} MBps")
    print(f"Upload: {results['upload_speed']:.2f} MBps")
    input("\nPress Enter to return to the menu...")

def speedtest_advanced():
    """
    This function performs a speedtest and prints detailed results.
    """
    print("Speedtest Advanced")
    st = speedtest.Speedtest()

    print("Running speedtest...", end="")
    spin = spinner()

    results = {}
    def run_speedtest():
        st.get_best_server()
        results['download_speed'] = st.download() / 1024 / 1024
        results['upload_speed'] = st.upload() / 1024 / 1024
        results['ping'] = st.results.ping
        results['server'] = st.results.server['name']
        results['country'] = st.results.server['country']

    speedtest_thread = threading.Thread(target=run_speedtest)
    speedtest_thread.start()

    while speedtest_thread.is_alive():
        print(next(spin), end='\r', flush=True)
        time.sleep(0.1)

    print(f"\nDownload: {results['download_speed']:.2f} MBps")
    print(f"Upload: {results['upload_speed']:.2f} MBps")
    print(f"Ping: {results['ping']} ms")
    print(f"Server: {results['server']} ({results['country']})")
    input("\nPress Enter to return to the menu...")
    
def device_info():
    """
    This function prints information about the device running the script.
    """
    print("Device Information")
    print(f"OS: {platform.system()} {platform.release()}")
    print(f"Hostname: {socket.gethostname()}")
    for interface in netifaces.interfaces():
        addresses = netifaces.ifaddresses(interface)
        if netifaces.AF_INET in addresses:
            ip_info = addresses[netifaces.AF_INET][0]
            print(f"IP Address ({interface}): {ip_info['addr']}")
            print(f"MAC Address ({interface}): {ip_info['broadcast']}")

if __name__ == "__main__":
    try:
        main_menu()
    except Exception as e:
        logging.error("Exception occurred", exc_info=True)
        console.print(Fore.RED + "An error occurred: " + str(e) + Style.RESET_ALL)
    finally:
        input("\nPress Enter to exit...")