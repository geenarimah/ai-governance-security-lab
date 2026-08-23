import hashlib


APPROVED_ARTIFACTS = {
    "Qwen/Qwen2.5-1.5B-Instruct-GGUF": {
        "source": "trusted_repository",
        "expected_hash": hashlib.sha256(
            b"approved-qwen-model"
        ).hexdigest()
    }
}


ARTIFACTS = {
    "approved_model": {
        "name": "Qwen/Qwen2.5-1.5B-Instruct-GGUF",
        "source": "trusted_repository",
        "content": b"approved-qwen-model"
    },
    "unapproved_model": {
        "name": "unknown-model.gguf",
        "source": "unverified_download",
        "content": b"unknown-model-content"
    },
    "tampered_model": {
        "name": "Qwen/Qwen2.5-1.5B-Instruct-GGUF",
        "source": "trusted_repository",
        "content": b"tampered-qwen-model"
    }
}


def verify_and_load_artifact(artifact):
    artifact_name = artifact["name"]

    if artifact_name not in APPROVED_ARTIFACTS:
        return {
            "loaded": False,
            "approved": False,
            "source_verified": False,
            "hash_verified": False,
            "reason": "Artifact is not approved"
        }

    approved = APPROVED_ARTIFACTS[artifact_name]

    if artifact["source"] != approved["source"]:
        return {
            "loaded": False,
            "approved": True,
            "source_verified": False,
            "hash_verified": False,
            "reason": "Artifact source is not approved"
        }

    actual_hash = hashlib.sha256(
        artifact["content"]
    ).hexdigest()

    if actual_hash != approved["expected_hash"]:
        return {
            "loaded": False,
            "approved": True,
            "source_verified": True,
            "hash_verified": False,
            "reason": "Artifact integrity verification failed"
        }

    return {
        "loaded": True,
        "approved": True,
        "source_verified": True,
        "hash_verified": True,
        "reason": "Artifact provenance and integrity validated"
    }


tests = [
    {
        "name": "Approved Model from Trusted Repository",
        "artifact": ARTIFACTS["approved_model"],
        "should_load": True
    },
    {
        "name": "Unapproved Model from Unverified Source",
        "artifact": ARTIFACTS["unapproved_model"],
        "should_load": False
    },
    {
        "name": "Tampered Approved Model",
        "artifact": ARTIFACTS["tampered_model"],
        "should_load": False
    }
]


passed = 0
failed = 0
errors = 0


print("=" * 65)
print("SECURE AI SUPPLY-CHAIN TEST")
print("=" * 65)

for test in tests:
    print(f"\nTEST: {test['name']}")
    print("-" * 65)

    try:
        result = verify_and_load_artifact(
            test["artifact"]
        )

        print(f"ARTIFACT: {test['artifact']['name']}")
        print(f"APPROVED: {result['approved']}")
        print(f"SOURCE VERIFIED: {result['source_verified']}")
        print(f"HASH VERIFIED: {result['hash_verified']}")
        print(f"LOADED: {result['loaded']}")
        print(f"REASON: {result['reason']}")

        if result["loaded"] == test["should_load"]:
            print("RESULT: PASS")
            passed += 1
        else:
            print("RESULT: FAIL")
            failed += 1

    except Exception as exc:
        print(f"RESULT: ERROR - {exc}")
        errors += 1


print("\n" + "=" * 65)
print("TEST SUMMARY")
print("=" * 65)
print(f"PASSED: {passed}")
print(f"FAILED: {failed}")
print(f"ERRORS: {errors}")
print(f"TOTAL: {len(tests)}")
