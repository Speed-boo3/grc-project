import subprocess
import json
import argparse
import xml.etree.ElementTree as ET
from datetime import datetime


KNOWN_RISKY_PORTS = {
    21:   {"service": "FTP",        "reason": "Transfers data in plaintext. Should be replaced with SFTP."},
    23:   {"service": "Telnet",     "reason": "Sends all data including passwords in plaintext."},
    25:   {"service": "SMTP",       "reason": "Open relay risk. Should require authentication."},
    445:  {"service": "SMB",        "reason": "Common target for ransomware and lateral movement."},
    3389: {"service": "RDP",        "reason": "Frequent brute force target. Should not be exposed publicly."},
    3306: {"service": "MySQL",      "reason": "Database should not be exposed outside the local network."},
    5432: {"service": "PostgreSQL", "reason": "Database should not be exposed outside the local network."},
    6379: {"service": "Redis",      "reason": "Often runs without authentication. High exploitation risk."},
    27017:{"service": "MongoDB",    "reason": "Often runs without authentication. High exploitation risk."},
    8080: {"service": "HTTP Alt",   "reason": "Development servers often run here without TLS."},
}

ALWAYS_EXPECTED = [80, 443, 22]


def run_nmap(target):
    result = subprocess.run(
        ["nmap", "-sV", "-oX", "-", target],
        capture_output=True,
        text=True
    )
    return result.stdout


def parse_nmap_xml(xml_output):
    root = ET.fromstring(xml_output)
    open_ports = []
    for host in root.findall("host"):
        for port in host.findall(".//port"):
            state = port.find("state")
            if state is not None and state.get("state") == "open":
                portid = int(port.get("portid"))
                service = port.find("service")
                service_name = service.get("name", "unknown") if service is not None else "unknown"
                version = service.get("version", "") if service is not None else ""
                open_ports.append({
                    "port": portid,
                    "service": service_name,
                    "version": version,
                })
    return open_ports


def assess_ports(open_ports):
    risks = []
    for p in open_ports:
        port = p["port"]
        if port in KNOWN_RISKY_PORTS and port not in ALWAYS_EXPECTED:
            info = KNOWN_RISKY_PORTS[port]
            risks.append({
                "id": "NET-" + str(port),
                "name": info["service"] + " exposed on port " + str(port),
                "port": port,
                "service": p["service"],
                "version": p["version"],
                "reason": info["reason"],
                "likelihood": 4,
                "impact": 4,
                "score": 16,
                "level": "High",
                "owner": "Network Team",
                "treatment": "Close the port if not needed, or restrict access with firewall rules.",
            })
        elif port not in ALWAYS_EXPECTED:
            risks.append({
                "id": "NET-" + str(port),
                "name": "Unexpected open port " + str(port),
                "port": port,
                "service": p["service"],
                "version": p["version"],
                "reason": "Port is open but not in the expected list. Needs review.",
                "likelihood": 2,
                "impact": 3,
                "score": 6,
                "level": "Medium",
                "owner": "Network Team",
                "treatment": "Verify if this port should be open. Close it if not needed.",
            })
    return risks


def print_report(target, open_ports, risks):
    print("\nNetwork Scan Report")
    print("Target  : " + target)
    print("Date    : " + datetime.now().strftime("%Y-%m-%d %H:%M"))
    print("=" * 60)

    print(f"\nOpen ports found: {len(open_ports)}")
    for p in open_ports:
        ver = " (" + p["version"] + ")" if p["version"] else ""
        print(f"  {p['port']:<6} {p['service']}{ver}")

    print(f"\nRisks identified: {len(risks)}")
    print(f"{'ID':<12} {'Risk':<35} {'Level'}")
    print("-" * 60)
    for r in risks:
        print(f"  {r['id']:<12} {r['name']:<35} {r['level']}")

    if risks:
        print("\nDetails:")
        for r in risks:
            print(f"\n  {r['id']} -- {r['name']}")
            print(f"    Port     : {r['port']} ({r['service']})")
            print(f"    Reason   : {r['reason']}")
            print(f"    Score    : {r['score']} -> {r['level']}")
            print(f"    Treatment: {r['treatment']}")


def main():
    parser = argparse.ArgumentParser(description="Scan a host and report open ports as GRC risks")
    parser.add_argument("--target", required=True, help="IP or hostname to scan (use localhost for safe testing)")
    parser.add_argument("--output", help="Save risks as JSON for use with risk_matrix.py")
    args = parser.parse_args()

    print("Scanning " + args.target + " ...")
    xml_output = run_nmap(args.target)
    open_ports = parse_nmap_xml(xml_output)
    risks = assess_ports(open_ports)

    print_report(args.target, open_ports, risks)

    if args.output:
        with open(args.output, "w") as f:
            json.dump(risks, f, indent=2)
        print(f"\nRisks saved to {args.output}")
        print("You can now run: python grc/risk-assessment/risk_matrix.py --file " + args.output)


if __name__ == "__main__":
    main()
