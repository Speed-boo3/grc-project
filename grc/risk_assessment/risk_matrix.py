import json
import argparse

LIKELIHOOD_LABELS = {1: "Rare", 2: "Unlikely", 3: "Possible", 4: "Likely", 5: "Almost certain"}
IMPACT_LABELS = {1: "Negligible", 2: "Minor", 3: "Moderate", 4: "Major", 5: "Critical"}


def risk_level(score):
    if score <= 4:
        return "Low"
    elif score <= 9:
        return "Medium"
    elif score <= 16:
        return "High"
    return "Critical"


def assess_risks(risks):
    results = []
    for risk in risks:
        score = risk["likelihood"] * risk["impact"]
        results.append({
            "id": risk["id"],
            "name": risk["name"],
            "likelihood": risk["likelihood"],
            "likelihood_label": LIKELIHOOD_LABELS[risk["likelihood"]],
            "impact": risk["impact"],
            "impact_label": IMPACT_LABELS[risk["impact"]],
            "score": score,
            "level": risk_level(score),
            "owner": risk.get("owner", "Unassigned"),
            "treatment": risk.get("treatment", "None defined"),
        })
    return sorted(results, key=lambda x: x["score"], reverse=True)


def print_report(results):
    print("\nRisk Assessment Report")
    print("=" * 70)
    print(f"{'ID':<10} {'Risk':<32} {'Score':<7} {'Level':<10} {'Owner'}")
    print("-" * 70)
    for r in results:
        print(f"{r['id']:<10} {r['name']:<32} {r['score']:<7} {r['level']:<10} {r['owner']}")
    print("=" * 70)
    print("\nDetails:")
    for r in results:
        print(f"\n  {r['id']} -- {r['name']}")
        print(f"    Likelihood : {r['likelihood']} ({r['likelihood_label']})")
        print(f"    Impact     : {r['impact']} ({r['impact_label']})")
        print(f"    Score      : {r['score']} -> {r['level']}")
        print(f"    Treatment  : {r['treatment']}")


def main():
    parser = argparse.ArgumentParser(description="Score and rank risks from a JSON file")
    parser.add_argument("--file", required=True, help="Path to JSON risk register")
    parser.add_argument("--output", help="Save results to JSON file")
    args = parser.parse_args()

    with open(args.file, "r") as f:
        risks = json.load(f)

    results = assess_risks(risks)
    print_report(results)

    if args.output:
        with open(args.output, "w") as f:
            json.dump(results, f, indent=2)
        print(f"\nSaved to {args.output}")


if __name__ == "__main__":
    main()
