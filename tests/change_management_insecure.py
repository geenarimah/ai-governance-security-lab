CURRENT_CONFIG = {
    "model": "Qwen/Qwen2.5-1.5B-Instruct-GGUF",
    "system_prompt": "Only provide authorized banking information.",
    "output_validation_enabled": True,
    "version": "1.0"
}


def apply_change(config, change_request):
    """
    INSECURE DESIGN:
    Any requested change is applied immediately.
    No approval, validation, version control, or rollback check.
    """

    for key, value in change_request.items():
        config[key] = value

    return config


tests = [
    {
        "name": "Approved-Looking Prompt Update",
        "change": {
            "system_prompt": (
                "Provide authorized banking information clearly and concisely."
            )
        },
        "should_allow": True
    },
    {
        "name": "Disable Output Validation",
        "change": {
            "output_validation_enabled": False
        },
        "should_allow": False
    },
    {
        "name": "Unauthorized Model Replacement",
        "change": {
            "model": "unapproved-model.gguf"
        },
        "should_allow": False
    },
    {
        "name": "Direct Version Override",
        "change": {
            "version": "99.0"
        },
        "should_allow": False
    }
]


passed = 0
failed = 0
errors = 0


print("=" * 65)
print("INSECURE AI CHANGE MANAGEMENT TEST")
print("=" * 65)

for test in tests:
    print(f"\nTEST: {test['name']}")
    print("-" * 65)

    try:
        test_config = CURRENT_CONFIG.copy()

        before = test_config.copy()
        after = apply_change(
            test_config,
            test["change"]
        )

        change_applied = any(
            before.get(key) != after.get(key)
            for key in test["change"]
        )

        actual_allow = change_applied

        print(f"CHANGE REQUEST: {test['change']}")
        print(f"CONFIG BEFORE: {before}")
        print(f"CONFIG AFTER:  {after}")

        if actual_allow == test["should_allow"]:
            print("RESULT: PASS")
            passed += 1
        else:
            print(
                "RESULT: FAIL - change was applied without "
                "required governance controls"
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
