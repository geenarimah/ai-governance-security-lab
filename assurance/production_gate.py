import json
import sys
from datetime import datetime, timezone
from pathlib import Path


COMPARISON_PATH = Path(
    "assurance/runs/latest_comparison.json"
)

OUTPUT_PATH = Path(
    "assurance/runs/latest_production_gate.json"
)


CONTROL_FAILURE_RESPONSES = {
    "AI-DATA-001": {
        "severity": "CRITICAL",
        "response": (
            "Block AI processing involving restricted data, "
            "investigate data-flow failure, remediate the control, "
            "and require successful retesting before deployment."
        ),
        "production_gate": "BLOCK"
    },

    "AI-ACCESS-001": {
        "severity": "CRITICAL",
        "response": (
            "Disable affected AI access path, investigate authorization "
            "failure, remediate identity or authorization logic, and "
            "require successful retesting."
        ),
        "production_gate": "BLOCK"
    },

    "AI-OUTPUT-001": {
        "severity": "HIGH",
        "response": (
            "Block affected AI output capability, investigate the "
            "validation regression, restore or strengthen output controls, "
            "and require successful retesting."
        ),
        "production_gate": "BLOCK"
    }
}


def load_json(path):
    with path.open() as file:
        return json.load(file)


comparison = load_json(COMPARISON_PATH)

regressions = comparison.get(
    "regressions",
    []
)

missing_controls = comparison.get(
    "missing_controls",
    []
)


gate_reasons = []
failure_responses = []


for regression in regressions:

    control_id = regression["control_id"]

    policy = CONTROL_FAILURE_RESPONSES.get(
        control_id,
        {
            "severity": "HIGH",
            "response": (
                "Investigate control regression, remediate the "
                "control, and require successful retesting."
            ),
            "production_gate": "BLOCK"
        }
    )

    failure_responses.append(
        {
            "control_id": control_id,
            "baseline_result": regression["baseline"],
            "current_result": regression["current"],
            "severity": policy["severity"],
            "required_response": policy["response"],
            "production_gate": policy["production_gate"]
        }
    )

    if policy["production_gate"] == "BLOCK":
        gate_reasons.append(
            f"{control_id} regression"
        )


for control_id in missing_controls:

    gate_reasons.append(
        f"{control_id} missing from current assurance run"
    )

    failure_responses.append(
        {
            "control_id": control_id,
            "severity": "HIGH",
            "required_response": (
                "Restore the missing control test or control implementation "
                "and complete successful assurance testing."
            ),
            "production_gate": "BLOCK"
        }
    )


if gate_reasons:
    gate_status = "BLOCKED"
else:
    gate_status = "PASS"


result = {
    "evaluated_at": datetime.now(
        timezone.utc
    ).isoformat(),
    "system_id": "AI-SYS-001",
    "baseline_run": comparison["baseline_run"],
    "current_run": comparison["current_run"],
    "comparison_status": comparison[
        "comparison_status"
    ],
    "production_gate_status": gate_status,
    "gate_reasons": gate_reasons,
    "failure_responses": failure_responses,
    "production_approved": False
}


with OUTPUT_PATH.open("w") as file:
    json.dump(
        result,
        file,
        indent=2
    )


print("=" * 70)
print("AI PRODUCTION GATE")
print("=" * 70)

print(
    f"Baseline Run:           "
    f"{result['baseline_run']}"
)

print(
    f"Current Run:            "
    f"{result['current_run']}"
)

print(
    f"Comparison Status:      "
    f"{result['comparison_status']}"
)

print(
    f"Production Gate Status: "
    f"{result['production_gate_status']}"
)

print()


if failure_responses:

    print("CONTROL FAILURE RESPONSES")
    print("-" * 70)

    for item in failure_responses:

        print(
            f"{item['control_id']} "
            f"[{item['severity']}]"
        )

        print(
            f"Required Response: "
            f"{item['required_response']}"
        )

        print(
            f"Production Gate: "
            f"{item['production_gate']}"
        )

        print()


if gate_reasons:

    print("PRODUCTION BLOCK REASONS")
    print("-" * 70)

    for reason in gate_reasons:
        print(f"- {reason}")


print()
print("=" * 70)

if gate_status == "BLOCKED":
    print(
        "DECISION: PRODUCTION DEPLOYMENT BLOCKED"
    )
else:
    print(
        "DECISION: ASSURANCE GATE PASSED"
    )

print("=" * 70)

print(
    f"Gate evidence saved to: "
    f"{OUTPUT_PATH}"
)


if gate_status == "BLOCKED":
    sys.exit(1)
