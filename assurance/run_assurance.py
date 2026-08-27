import json
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path


CONTROL_TESTS = [
    {
        "control_id": "AI-DATA-001",
        "name": "Sensitive Data Minimization",
        "command": ["python3", "tests/red_team_tests_v4.py"],
    },
    {
        "control_id": "AI-ACCESS-001",
        "name": "User-Level Authorization",
        "command": ["python3", "controls/access_control_secure_v2.py"],
    },
    {
        "control_id": "AI-LOG-001",
        "name": "AI Security Logging and Monitoring",
        "command": ["python3", "tests/test_security_logging.py"],
    },
    {
        "control_id": "AI-OUTPUT-001",
        "name": "AI Output Validation",
        "command": ["python3", "tests/output_validation_secure.py"],
    },
    {
        "control_id": "AI-AUTH-001",
        "name": "Authentication and Session Assurance",
        "command": ["python3", "tests/auth_session_secure.py"],
    },
    {
        "control_id": "AI-CHANGE-001",
        "name": "AI Change Management",
        "command": ["python3", "tests/change_management_secure.py"],
    },
    {
        "control_id": "AI-HUMAN-001",
        "name": "Human Oversight",
        "command": ["python3", "tests/human_oversight_secure.py"],
    },
    {
        "control_id": "AI-IR-001",
        "name": "AI Incident Response",
        "command": ["python3", "tests/incident_response_secure.py"],
    },
    {
        "control_id": "AI-SESSION-001",
        "name": "Session and Context Isolation",
        "command": ["python3", "tests/session_isolation_secure.py"],
    },
    {
        "control_id": "AI-MODEL-001",
        "name": "AI Model Risk Management",
        "command": ["python3", "tests/model_risk_secure.py"],
    },
    {
        "control_id": "AI-SUPPLY-001",
        "name": "AI Supply-Chain Assurance",
        "command": ["python3", "tests/supply_chain_secure.py"],
    },
    {
        "control_id": "AI-PRIV-001",
        "name": "AI Privacy and Data Governance",
        "command": ["python3", "tests/privacy_governance_secure.py"],
    },
]


def extract_number(label, output):
    match = re.search(
        rf"{label}\s*:\s*(\d+)",
        output,
        re.IGNORECASE
    )

    if match:
        return int(match.group(1))

    return None


def run_control(control):
    print("-" * 70)
    print(f"{control['control_id']} - {control['name']}")
    print("-" * 70)

    try:
        completed = subprocess.run(
            control["command"],
            capture_output=True,
            text=True,
            timeout=420
        )

        output = completed.stdout + completed.stderr

        passed = extract_number("PASSED", output)
        failed = extract_number("FAILED", output)
        errors = extract_number("ERRORS", output)
        total = extract_number("TOTAL", output)

        if failed == 0 and errors == 0 and passed is not None:
            assurance_result = "PASS"
        elif failed is not None or errors is not None:
            assurance_result = "FAIL"
        else:
            assurance_result = "ERROR"

        print(f"Result: {assurance_result}")

        if total is not None:
            print(
                f"Tests: {passed} passed / "
                f"{failed} failed / "
                f"{errors} errors / "
                f"{total} total"
            )

        return {
            "control_id": control["control_id"],
            "control_name": control["name"],
            "command": " ".join(control["command"]),
            "result": assurance_result,
            "passed": passed,
            "failed": failed,
            "errors": errors,
            "total": total,
            "return_code": completed.returncode,
            "output": output,
        }

    except subprocess.TimeoutExpired:
        print("Result: ERROR - TEST TIMEOUT")

        return {
            "control_id": control["control_id"],
            "control_name": control["name"],
            "command": " ".join(control["command"]),
            "result": "ERROR",
            "passed": None,
            "failed": None,
            "errors": 1,
            "total": None,
            "return_code": None,
            "output": "Test exceeded 180-second timeout.",
        }

    except Exception as exc:
        print(f"Result: ERROR - {exc}")

        return {
            "control_id": control["control_id"],
            "control_name": control["name"],
            "command": " ".join(control["command"]),
            "result": "ERROR",
            "passed": None,
            "failed": None,
            "errors": 1,
            "total": None,
            "return_code": None,
            "output": str(exc),
        }


timestamp = datetime.now(timezone.utc)
run_id = timestamp.strftime("AR-%Y%m%d-%H%M%S")

results = []

print("=" * 70)
print("AI CONTINUOUS ASSURANCE RETEST")
print("=" * 70)
print(f"Run ID: {run_id}")
print(f"Controls scheduled: {len(CONTROL_TESTS)}")
print("=" * 70)

for control in CONTROL_TESTS:
    results.append(run_control(control))


controls_passed = sum(
    1 for result in results
    if result["result"] == "PASS"
)

controls_failed = sum(
    1 for result in results
    if result["result"] == "FAIL"
)

controls_error = sum(
    1 for result in results
    if result["result"] == "ERROR"
)


if controls_failed == 0 and controls_error == 0:
    suite_result = "PASS"
else:
    suite_result = "FAIL"


assurance_run = {
    "run_id": run_id,
    "captured_at": timestamp.isoformat(),
    "system_id": "AI-SYS-001",
    "suite_version": "1.0",
    "suite_result": suite_result,
    "controls_scheduled": len(CONTROL_TESTS),
    "controls_passed": controls_passed,
    "controls_failed": controls_failed,
    "controls_error": controls_error,
    "production_status": "NOT_APPROVED_FOR_PRODUCTION",
    "results": results,
}


output_directory = Path("assurance/runs")
output_directory.mkdir(parents=True, exist_ok=True)

output_path = output_directory / f"{run_id}.json"

with output_path.open("w") as file:
    json.dump(assurance_run, file, indent=2)


print()
print("=" * 70)
print("ASSURANCE RUN SUMMARY")
print("=" * 70)
print(f"Run ID:            {run_id}")
print(f"Controls Passed:   {controls_passed}")
print(f"Controls Failed:   {controls_failed}")
print(f"Control Errors:    {controls_error}")
print(f"Suite Result:      {suite_result}")
print("Production Status: NOT_APPROVED_FOR_PRODUCTION")
print("=" * 70)
print(f"Evidence saved to: {output_path}")
