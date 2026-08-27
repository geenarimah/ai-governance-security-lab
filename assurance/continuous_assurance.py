import subprocess
import sys


STEPS = [
    ("Create Change Manifest", ["python3", "assurance/create_change_manifest.py"]),
    ("Run Assurance Suite", ["python3", "assurance/run_assurance.py"]),
    ("Compare Evidence", ["python3", "assurance/compare_evidence.py"]),
    ("Evaluate Production Gate", ["python3", "assurance/production_gate.py"]),
]


def run_step(name, command):
    print()
    print("=" * 70)
    print(name.upper())
    print("=" * 70)

    result = subprocess.run(command)

    return result.returncode


print("=" * 70)
print("AI CONTINUOUS ASSURANCE PIPELINE")
print("=" * 70)

pipeline_failed = False

for name, command in STEPS:
    code = run_step(name, command)

    if code != 0:
        print()
        print(f"{name}: FAILED")
        pipeline_failed = True
        break

    print()
    print(f"{name}: PASSED")


print()
print("=" * 70)
print("PIPELINE SUMMARY")
print("=" * 70)

if pipeline_failed:
    print("CONTINUOUS ASSURANCE RESULT: FAIL")
    print("ACTION: PRODUCTION PATH REMAINS BLOCKED")
    sys.exit(1)
else:
    print("CONTINUOUS ASSURANCE RESULT: PASS")
    print("ASSURANCE GATE: PASSED")
    print("OVERALL PRODUCTION APPROVAL: NO")
