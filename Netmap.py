import argparse
import socket
import concurrent.futures
import os
import platform
from scapy.all import *

def scan_port(target_ip, port):
    # ... (unchanged)

def detect_service(target_ip, port):
    # ... (unchanged)

def os_fingerprint(target_ip):
    # ... (unchanged)

def nmap_style_scan(target_ip, port_range):
    # ... (unchanged)

def main():
    parser = argparse.ArgumentParser(description="Enhanced Network Scanner")
    parser.add_argument("target_ip", help="Specify the target IP address for scanning")
    parser.add_argument("-p", "--port-range", type=str, help="Specify the port range (e.g., '80-100')")
    
    args = parser.parse_args()

    target_ip_address = args.target_ip
    port_range_str = args.port_range or "1-1024"  # Default port range
    port_range_to_scan = tuple(map(int, port_range_str.split('-')))

    nmap_style_scan(target_ip_address, port_range_to_scan)

if __name__ == "__main__":
    main()
