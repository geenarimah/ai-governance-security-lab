import csv
import json
from datetime import datetime, timezone
from pathlib import Path


RISK_REGISTER = Path("evidence/AI_Risk_Register.csv")
GATE_PATH = Path("assurance/runs/latest_production_gate.json")
OUTPUT_PATH = Path("assurance/runs/latest_risk_reassessment.json")


CONTROL_TO_RISK = {
    "AI-DATA-001": "AI-RISK-001",
    "AI-ACCESS-001": "AI-RISK-002",
    "AI-LOG-001": "AI-RISK-003",
    "AI-OUTPUT-001": "AI-RISK-004",
    "AI-AUTH-001": "AI-RISK-005",
    "AI-CHANGE-001": "AI-RISK-006",
    "AI-HUMAN-001": "AI-RISK-007",
    "AI-IR-001": "AI-RISK-008",
    "AI-SESSION-001": "AI-RISK-009",
    "AI-MODEL-001": "AI-RISK-010",
    "AI-SUPPLY-001": "AI-RISK-011",
    "AI-PRIV-001": "AI-RISK-012",
}


def risk_rating(score):
    if score <= 4:
        return "Low"
    elif score <= 9:
        return "Medium"
    elif score <= 16:
        return "High"
    return "Critical"


with GATE_PATH.open() as file:
    gate = json.load(file)


with RISK_REGISTER.open(newline="") as file:
    reader = csv.DictReader(file)
    risks = list(reader)


risk_index = {
    risk["Risk ID"]: risk
    for risk in risks
}


reassessments = []


for failure in gate.get("failure_responses", []):

    control_id = failure["control_id"]

    risk_id = CONTROL_TO_RISK.get(control_id)

    if not risk_id:
        continue

    risk = risk_index.get(risk_id)

    if not risk:
        continue

    previous_likelihood = int(
        risk["Residual Likelihood"]
    )

    impact = int(
        risk["Residual Impact"]
    )

    previous_score = int(
        risk["Residual Score"]
    )

    previous_rating = risk[
        "Residual Rating"
    ]

    # Control failure increases likelihood by one level,
    # capped at 5.
    reassessed_likelihood = min(
        5,
        previous_likelihood + 1
    )

    reassessed_score = (
        reassessed_likelihood * impact
    )

    reassessed_rating = risk_rating(
        reassessed_score
    )

    reassessments.append(
        {
            "risk_id": risk_id,
            "risk_title": risk["Risk Title"],
            "control_id": control_id,
            "trigger": "CONTROL_REGRESSION",
            "previous_residual_likelihood":
                previous_likelihood,
            "reassessed_residual_likelihood":
                reassessed_likelihood,
            "residual_impact": impact,
            "previous_residual_score":
                previous_score,
            "reassessed_residual_score":
                reassessed_score,
            "previous_residual_rating":
                previous_rating,
            "reassessed_residual_rating":
                reassessed_rating,
            "risk_status":
                "ESCALATED_PENDING_REMEDIATION",
            "production_gate":
                failure["production_gate"]
        }
    )


result = {
    "evaluated_at": datetime.now(
        timezone.utc
    ).isoformat(),
    "system_id": "AI-SYS-001",
    "source_run": gate["current_run"],
    "production_gate_status":
        gate["production_gate_status"],
    "reassessments": reassessments
}


with OUTPUT_PATH.open("w") as file:
    json.dump(
        result,
        file,
        indent=2
    )


print("=" * 70)
print("AI RISK REASSESSMENT")
print("=" * 70)

print(
    f"Source Run:             "
    f"{result['source_run']}"
)

print(
    f"Production Gate Status: "
    f"{result['production_gate_status']}"
)

print()


if not reassessments:
    print(
        "No control regressions requiring "
        "risk reassessment were found."
    )

else:

    for item in reassessments:

        print(
            f"{item['risk_id']} - "
            f"{item['risk_title']}"
        )

        print(
            f"Trigger Control: "
            f"{item['control_id']}"
        )

        print(
            "Residual Likelihood: "
            f"{item['previous_residual_likelihood']} "
            "-> "
            f"{item['reassessed_residual_likelihood']}"
        )

        print(
            "Residual Score:      "
            f"{item['previous_residual_score']} "
            "-> "
            f"{item['reassessed_residual_score']}"
        )

        print(
            "Residual Rating:     "
            f"{item['previous_residual_rating']} "
            "-> "
            f"{item['reassessed_residual_rating']}"
        )

        print(
            f"Risk Status:         "
            f"{item['risk_status']}"
        )

        print("-" * 70)


print(
    f"Risk reassessment evidence saved to: "
    f"{OUTPUT_PATH}"
)
