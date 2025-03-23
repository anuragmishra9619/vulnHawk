import argparse
from vuln_hawk.core import subdomain_enum, port_scan, vuln_scan, dir_bruteforce

def main():
    parser = argparse.ArgumentParser(description="VulnHawk - Website Security Scanner")
    parser.add_argument("-u", "--url", help="Target website URL", required=True)
    parser.add_argument("--subdomain", help="Perform subdomain enumeration", action="store_true")
    parser.add_argument("--ports", help="Perform port scanning", action="store_true")
    parser.add_argument("--vuln", help="Perform vulnerability scanning", action="store_true")
    parser.add_argument("--dir", help="Perform directory brute-force", action="store_true")
    
    args = parser.parse_args()

    print(f"Scanning Target: {args.url}\n")

    if args.subdomain:
        subdomain_enum.run(args.url)
    if args.ports:
        port_scan.run(args.url)
    if args.vuln:
        vuln_scan.run(args.url)
    if args.dir:
        dir_bruteforce.run(args.url)

if __name__ == "__main__":
    main()
