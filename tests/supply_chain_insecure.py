ARTIFACTS = {
    "approved_model": {
        "name": "Qwen/Qwen2.5-1.5B-Instruct-GGUF",
        "source": "trusted_repository",
        "expected_hash": "abc123"
    },
    "unapproved_model": {
        "name": "unknown-model.gguf",
        "source": "unverified_download",
        "expected_hash": "unknown"
    }
}


def load_artifact(artifact):
    """
    INSECURE DESIGN:
    The application loads AI model/software artifacts without
    enforcing provenance, approval, or integrity verification.
    """

    return {
        "loaded": True,
        "approved_source": artifact["source"] == "trusted_repository",
        "hash_verified": False,
        "artifact_name": artifact["name"]
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
        "name": "Approved Model Without Integrity Verification",
        "artifact": ARTIFACTS["approved_model"],
        "should_load": False
    }
]


passed = 0
failed = 0
errors = 0


print("=" * 65)
print("INSECURE AI SUPPLY-CHAIN TEST")
print("=" * 65)

for index, test in enumerate(tests):
    print(f"\nTEST: {test['name']}")
    print("-" * 65)

    try:
        result = load_artifact(test["artifact"])

        print(f"ARTIFACT: {result['artifact_name']}")
        print(f"APPROVED SOURCE: {result['approved_source']}")
        print(f"HASH VERIFIED: {result['hash_verified']}")
        print(f"LOADED: {result['loaded']}")

        # For the third scenario, lack of integrity verification
        # should prevent loading even though the source is approved.
        if index == 2:
            actual_should_load = (
                result["loaded"] and result["hash_verified"]
            )
        else:
            actual_should_load = result["loaded"]

        if actual_should_load == test["should_load"]:
            print("RESULT: PASS")
            passed += 1
        else:
            print(
                "RESULT: FAIL - artifact was accepted without "
                "required supply-chain assurance"
            )
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
