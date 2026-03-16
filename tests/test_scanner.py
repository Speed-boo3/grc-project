import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from grc.network_scan.scanner import assess_ports


def test_known_risky_port_flagged_as_high():
    ports = [{"port": 3389, "service": "ms-wbt-server", "version": ""}]
    risks = assess_ports(ports)
    assert len(risks) == 1
    assert risks[0]["level"] == "High"
    assert risks[0]["port"] == 3389


def test_expected_ports_not_flagged():
    ports = [
        {"port": 80, "service": "http", "version": ""},
        {"port": 443, "service": "https", "version": ""},
        {"port": 22, "service": "ssh", "version": ""},
    ]
    risks = assess_ports(ports)
    assert len(risks) == 0


def test_unexpected_port_flagged_as_medium():
    ports = [{"port": 9999, "service": "unknown", "version": ""}]
    risks = assess_ports(ports)
    assert len(risks) == 1
    assert risks[0]["level"] == "Medium"


def test_multiple_risky_ports():
    ports = [
        {"port": 21, "service": "ftp", "version": ""},
        {"port": 23, "service": "telnet", "version": ""},
        {"port": 443, "service": "https", "version": ""},
    ]
    risks = assess_ports(ports)
    assert len(risks) == 2


def test_risk_has_required_fields():
    ports = [{"port": 3306, "service": "mysql", "version": "8.0"}]
    risks = assess_ports(ports)
    r = risks[0]
    assert "id" in r
    assert "name" in r
    assert "level" in r
    assert "treatment" in r
    assert "score" in r
