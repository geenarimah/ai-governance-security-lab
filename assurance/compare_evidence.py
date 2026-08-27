import json
import glob
import os
import sys
from pathlib import Path


BASELINE_PATH = Path(
    "assurance/baselines/assurance_run_baseline_v1.json"
)


def load_json(path):
    with open(path) as file:
        return json.load(file)


def latest_assurance_run():
    files = glob.glob("assurance/runs/AR-*.json")

    if not files:
        raise FileNotFoundError(
            "No assurance run evidence exists."
        )

    return max(files, key=os.path.getmtime)


baseline = load_json(BASELINE_PATH)

current_path = latest_assurance_run()
current = load_json(current_path)


baseline_controls = {
    item["control_id"]: item
    for item in baseline["results"]
}

current_controls = {
    item["control_id"]: item
    for item in current["results"]
}


regressions = []
improvements = []
unchanged = []
missing = []
new_controls = []


all_control_ids = sorted(
    set(baseline_controls) | set(current_controls)
)


for control_id in all_control_ids:

    baseline_result = baseline_controls.get(control_id)
    current_result = current_controls.get(control_id)

    if baseline_result is None:
        new_controls.append(control_id)
        continue

    if current_result is None:
        missing.append(control_id)
        continue

    before = baseline_result["result"]
    after = current_result["result"]

    if before == "PASS" and after != "PASS":
        regressions.append(
            {
                "control_id": control_id,
                "baseline": before,
                "current": after,
            }
        )

    elif before != "PASS" and after == "PASS":
        improvements.append(
            {
                "control_id": control_id,
                "baseline": before,
                "current": after,
            }
        )

    else:
        unchanged.append(
            {
                "control_id": control_id,
                "baseline": before,
                "current": after,
            }
        )


print("=" * 70)
print("AI ASSURANCE EVIDENCE COMPARISON")
print("=" * 70)

print(f"Baseline Run: {baseline['run_id']}")
print(f"Current Run:  {current['run_id']}")

print()

print(f"Regressions:  {len(regressions)}")
print(f"Improvements: {len(improvements)}")
print(f"Missing:      {len(missing)}")
print(f"New Controls: {len(new_controls)}")

print()


if regressions:
    print("REGRESSIONS DETECTED")
    print("-" * 70)

    for item in regressions:
        print(
            f"{item['control_id']}: "
            f"{item['baseline']} -> {item['current']}"
        )

else:
    print("NO CONTROL REGRESSIONS DETECTED")


if missing:
    print()
    print("MISSING CONTROLS")
    print("-" * 70)

    for control_id in missing:
        print(control_id)


if new_controls:
    print()
    print("NEW CONTROLS")
    print("-" * 70)

    for control_id in new_controls:
        print(control_id)


comparison_result = {
    "baseline_run": baseline["run_id"],
    "current_run": current["run_id"],
    "regressions": regressions,
    "improvements": improvements,
    "missing_controls": missing,
    "new_controls": new_controls,
    "comparison_status": (
        "FAIL"
        if regressions or missing
        else "PASS"
    ),
}


output_path = Path(
    "assurance/runs/latest_comparison.json"
)

with output_path.open("w") as file:
    json.dump(
        comparison_result,
        file,
        indent=2
    )


print()
print("=" * 70)
print(
    f"COMPARISON STATUS: "
    f"{comparison_result['comparison_status']}"
)
print("=" * 70)

print(
    f"Comparison evidence saved to: "
    f"{output_path}"
)


if comparison_result["comparison_status"] == "FAIL":
    sys.exit(1)
