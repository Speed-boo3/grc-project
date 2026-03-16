import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from grc.risk_assessment.risk_matrix import risk_level, assess_risks


def test_low_risk():
    assert risk_level(4) == "Low"


def test_medium_risk():
    assert risk_level(6) == "Medium"
    assert risk_level(9) == "Medium"


def test_high_risk():
    assert risk_level(12) == "High"
    assert risk_level(16) == "High"


def test_critical_risk():
    assert risk_level(20) == "Critical"
    assert risk_level(25) == "Critical"


def test_assess_risks_sorted_by_score():
    risks = [
        {"id": "R1", "name": "Low risk", "likelihood": 1, "impact": 1},
        {"id": "R2", "name": "High risk", "likelihood": 5, "impact": 5},
        {"id": "R3", "name": "Medium risk", "likelihood": 3, "impact": 3},
    ]
    results = assess_risks(risks)
    assert results[0]["id"] == "R2"
    assert results[-1]["id"] == "R1"


def test_assess_risks_score_calculation():
    risks = [{"id": "R1", "name": "Test", "likelihood": 4, "impact": 3}]
    results = assess_risks(risks)
    assert results[0]["score"] == 12
    assert results[0]["level"] == "High"


def test_missing_owner_defaults():
    risks = [{"id": "R1", "name": "Test", "likelihood": 2, "impact": 2}]
    results = assess_risks(risks)
    assert results[0]["owner"] == "Unassigned"


def test_likelihood_label():
    risks = [{"id": "R1", "name": "Test", "likelihood": 5, "impact": 1}]
    results = assess_risks(risks)
    assert results[0]["likelihood_label"] == "Almost certain"
