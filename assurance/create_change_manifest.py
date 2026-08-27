import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path


SYSTEM_ID = "AI-SYS-001"

MODEL = {
    "name": "Qwen/Qwen2.5-1.5B-Instruct-GGUF",
    "deployment": "Local llama.cpp inference server",
    "model_version": "Qwen2.5-1.5B"
}

VERSIONS = {
    "prompt_version": "1.0",
    "test_data_version": "1.0",
    "control_suite_version": "1.0"
}


def get_git_commit():
    try:
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except Exception:
        return "UNKNOWN"


def get_git_status():
    try:
        result = subprocess.run(
            ["git", "status", "--porcelain"],
            capture_output=True,
            text=True,
            check=True
        )

        if result.stdout.strip():
            return "UNCOMMITTED_CHANGES"

        return "CLEAN"

    except Exception:
        return "UNKNOWN"


manifest = {
    "manifest_version": "1.0",
    "system_id": SYSTEM_ID,
    "captured_at": datetime.now(timezone.utc).isoformat(),
    "model": MODEL,
    "versions": VERSIONS,
    "git_commit": get_git_commit(),
    "git_working_tree": get_git_status(),
    "change_reason": "Initial continuous-assurance baseline",
    "production_status": "NOT_APPROVED_FOR_PRODUCTION"
}


output_path = Path("assurance/change_manifest.json")

with output_path.open("w") as file:
    json.dump(manifest, file, indent=2)


print("=" * 60)
print("AI ASSURANCE CHANGE MANIFEST")
print("=" * 60)

print(f"System ID:             {manifest['system_id']}")
print(f"Model:                 {manifest['model']['name']}")
print(f"Prompt Version:        {manifest['versions']['prompt_version']}")
print(f"Test Data Version:     {manifest['versions']['test_data_version']}")
print(f"Control Suite Version: {manifest['versions']['control_suite_version']}")
print(f"Git Commit:            {manifest['git_commit']}")
print(f"Git Working Tree:      {manifest['git_working_tree']}")
print(f"Production Status:     {manifest['production_status']}")

print("=" * 60)
print(f"Manifest saved to: {output_path}")
