import json
import argparse
import os
import sys
from datetime import datetime

REGISTER_PATH = os.path.join(os.path.dirname(__file__), "sample_risks.json")

LIKELIHOOD_LABELS = {1: "Rare", 2: "Unlikely", 3: "Possible", 4: "Likely", 5: "Almost certain"}
IMPACT_LABELS = {1: "Negligible", 2: "Minor", 3: "Moderate", 4: "Major", 5: "Critical"}


def load():
    with open(REGISTER_PATH) as f:
        return json.load(f)


def save(risks):
    with open(REGISTER_PATH, "w") as f:
        json.dump(risks, f, indent=2)


def score_level(score):
    if score >= 17:
        return "Critical"
    if score >= 10:
        return "High"
    if score >= 5:
        return "Medium"
    return "Low"


def list_risks(args):
    risks = load()
    status_filter = args.status if hasattr(args, "status") and args.status else None
    filtered = [r for r in risks if not status_filter or r.get("status", "open") == status_filter]

    if not filtered:
        print("No risks found.")
        return

    print(f"\n{'ID':<12} {'Risk':<35} {'Score':<7} {'Level':<10} {'Status':<12} {'Owner'}")
    print("-" * 90)
    for r in sorted(filtered, key=lambda x: x["likelihood"] * x["impact"], reverse=True):
        score = r["likelihood"] * r["impact"]
        level = score_level(score)
        status = r.get("status", "open")
        print(f"{r['id']:<12} {r['title'][:34]:<35} {score:<7} {level:<10} {status:<12} {r['owner']}")
    print()


def add_risk(args):
    risks = load()
    existing_ids = [r["id"] for r in risks]
    num = max([int(i.split("-")[1]) for i in existing_ids if "-" in i], default=0) + 1
    new_id = f"RISK-{str(num).zfill(3)}"

    score = args.likelihood * args.impact
    level = score_level(score)

    risk = {
        "id": new_id,
        "title": args.title,
        "description": args.description or args.title,
        "likelihood": args.likelihood,
        "impact": args.impact,
        "score": score,
        "level": level,
        "owner": args.owner,
        "treatment": args.treatment or "mitigate",
        "status": "open",
        "created": datetime.now().strftime("%Y-%m-%d"),
        "updated": datetime.now().strftime("%Y-%m-%d"),
    }

    risks.append(risk)
    save(risks)
    print(f"\n[+] Added {new_id}: {args.title}")
    print(f"    Score: {score} ({level})")
    print(f"    Owner: {args.owner}")
    print(f"    Treatment: {risk['treatment']}\n")


def close_risk(args):
    risks = load()
    found = False
    for r in risks:
        if r["id"] == args.id.upper():
            r["status"] = "closed"
            r["updated"] = datetime.now().strftime("%Y-%m-%d")
            r["closed_note"] = args.note or "Closed"
            found = True
            print(f"\n[+] {r['id']} marked as closed: {r['title']}\n")
            break
    if not found:
        print(f"\n[-] Risk ID {args.id} not found.\n")
        sys.exit(1)
    save(risks)


def update_risk(args):
    risks = load()
    found = False
    for r in risks:
        if r["id"] == args.id.upper():
            if args.likelihood:
                r["likelihood"] = args.likelihood
            if args.impact:
                r["impact"] = args.impact
            if args.owner:
                r["owner"] = args.owner
            if args.treatment:
                r["treatment"] = args.treatment
            r["score"] = r["likelihood"] * r["impact"]
            r["level"] = score_level(r["score"])
            r["updated"] = datetime.now().strftime("%Y-%m-%d")
            found = True
            print(f"\n[+] Updated {r['id']}: score now {r['score']} ({r['level']})\n")
            break
    if not found:
        print(f"\n[-] Risk ID {args.id} not found.\n")
        sys.exit(1)
    save(risks)


def main():
    parser = argparse.ArgumentParser(
        description="GRC Risk Register Manager",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python risk_manager.py list
  python risk_manager.py list --status open
  python risk_manager.py add --title "Ransomware attack" --likelihood 4 --impact 5 --owner "Security Team"
  python risk_manager.py update RISK-001 --likelihood 3
  python risk_manager.py close RISK-006 --note "Laptop encrypted, risk accepted"
        """
    )
    sub = parser.add_subparsers(dest="command")

    # list
    lp = sub.add_parser("list", help="List all risks")
    lp.add_argument("--status", choices=["open", "closed"], help="Filter by status")
    lp.set_defaults(func=list_risks)

    # add
    ap = sub.add_parser("add", help="Add a new risk")
    ap.add_argument("--title", required=True, help="Short risk title")
    ap.add_argument("--description", help="Full description")
    ap.add_argument("--likelihood", type=int, required=True, choices=range(1, 6), metavar="1-5")
    ap.add_argument("--impact", type=int, required=True, choices=range(1, 6), metavar="1-5")
    ap.add_argument("--owner", required=True, help="Team or person responsible")
    ap.add_argument("--treatment", choices=["mitigate", "accept", "transfer", "avoid"], default="mitigate")
    ap.set_defaults(func=add_risk)

    # update
    up = sub.add_parser("update", help="Update an existing risk")
    up.add_argument("id", help="Risk ID e.g. RISK-001")
    up.add_argument("--likelihood", type=int, choices=range(1, 6), metavar="1-5")
    up.add_argument("--impact", type=int, choices=range(1, 6), metavar="1-5")
    up.add_argument("--owner")
    up.add_argument("--treatment", choices=["mitigate", "accept", "transfer", "avoid"])
    up.set_defaults(func=update_risk)

    # close
    cp = sub.add_parser("close", help="Close a risk")
    cp.add_argument("id", help="Risk ID e.g. RISK-001")
    cp.add_argument("--note", help="Closing note or reason")
    cp.set_defaults(func=close_risk)

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        return
    args.func(args)


if __name__ == "__main__":
    main()
