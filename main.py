import pyfiglet
import argparse
from modules.subdomain_enum import subdomain_scan
from modules.port_scan import port_scan
from modules.vuln_scan import vuln_scan
from modules.dir_bruteforce import dir_bruteforce
from modules.ip_lookup import ip_lookup
from modules.generate_report import generate_pdf_report

def main():
    banner = pyfiglet.figlet_format("SecureVajr")
    print(banner)
    print("[✔] SecureVajr - Web Security Scanner [✔]")
    print("[✔] Developed by Anurag Mishra [✔]\n")

    # User Input
    target = input("Enter Target Domain/IP: ").strip()
    
    print("\nSelect Scans to Perform:")
    print("[1] Subdomain Enumeration")
    print("[2] Port Scanning")
    print("[3] Vulnerability Scanning")
    print("[4] Directory Bruteforce")
    print("[5] IP Lookup")
    
    choices = input("Enter option numbers separated by comma (e.g., 1,3,5): ")
    options = choices.split(',')

    results = {}

    if '1' in options:
        results['subdomains'] = subdomain_scan(target)
    if '2' in options:
        results['ports'] = port_scan(target)
    if '3' in options:
        results['vulnerabilities'] = vuln_scan(target)
    if '4' in options:
        results['directories'] = dir_bruteforce(target)
    if '5' in options:
        results['ip_info'] = ip_lookup(target)

    # Generate Report
    generate_pdf_report(target, results)
    print("\n[✔] Scan Completed! Report saved as reports/{}.pdf".format(target.replace('.', '_')))

if __name__ == "__main__":
    main()
