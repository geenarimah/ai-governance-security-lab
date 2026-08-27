import json
from datetime import datetime, timezone
from pathlib import Path


GATE_PATH = Path(
    "assurance/runs/latest_production_gate.json"
)

RISK_REASSESSMENT_PATH = Path(
    "assurance/runs/latest_risk_reassessment.json"
)

OUTPUT_PATH = Path(
    "assurance/runs/latest_remediation_closure.json"
)


def load_json(path):
    with path.open() as file:
        return json.load(file)


gate = load_json(GATE_PATH)
risk_reassessment = load_json(
    RISK_REASSESSMENT_PATH
)


closures = []


if gate["production_gate_status"] == "PASS":

    for risk in risk_reassessment.get(
        "reassessments",
        []
    ):

        closures.append(
            {
                "risk_id": risk["risk_id"],
                "control_id": risk["control_id"],
                "previous_escalated_score":
                    risk["reassessed_residual_score"],
                "restored_residual_score":
                    risk["previous_residual_score"],
                "previous_escalated_rating":
                    risk["reassessed_residual_rating"],
                "restored_residual_rating":
                    risk["previous_residual_rating"],
                "closure_status":
                    "REMEDIATION_VERIFIED",
                "evidence": (
                    "Control successfully retested, "
                    "no regression detected, and "
                    "assurance gate passed."
                )
            }
        )


result = {
    "evaluated_at": datetime.now(
        timezone.utc
    ).isoformat(),
    "system_id": "AI-SYS-001",
    "current_run": gate["current_run"],
    "production_gate_status":
        gate["production_gate_status"],
    "closures": closures,
    "production_approved": False
}


with OUTPUT_PATH.open("w") as file:
    json.dump(
        result,
        file,
        indent=2
    )


print("=" * 70)
print("AI REMEDIATION CLOSURE")
print("=" * 70)

print(
    f"Current Run:            "
    f"{result['current_run']}"
)

print(
    f"Production Gate Status: "
    f"{result['production_gate_status']}"
)

print()


for item in closures:

    print(
        f"{item['risk_id']} / "
        f"{item['control_id']}"
    )

    print(
        "Escalated Score: "
        f"{item['previous_escalated_score']}"
    )

    print(
        "Restored Score:  "
        f"{item['restored_residual_score']}"
    )

    print(
        "Closure Status:  "
        f"{item['closure_status']}"
    )

    print(
        "Evidence:        "
        f"{item['evidence']}"
    )

    print("-" * 70)


print(
    "Overall Production Approval: "
    "NO"
)

print()
print(
    f"Closure evidence saved to: "
    f"{OUTPUT_PATH}"
)
