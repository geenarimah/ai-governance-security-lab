APPROVED_MODELS = {
    "Qwen/Qwen2.5-1.5B-Instruct-GGUF"
}

CURRENT_CONFIG = {
    "model": "Qwen/Qwen2.5-1.5B-Instruct-GGUF",
    "system_prompt": "Only provide authorized banking information.",
    "output_validation_enabled": True,
    "version": "1.0"
}


def validate_change(change_request, approved):
    if not approved:
        return False, "Change request is not approved"

    if "output_validation_enabled" in change_request:
        if change_request["output_validation_enabled"] is False:
            return False, "Security control cannot be disabled"

    if "model" in change_request:
        if change_request["model"] not in APPROVED_MODELS:
            return False, "Model is not on the approved model list"

    if "version" in change_request:
        return False, "Version cannot be directly overridden"

    return True, "Change approved"


def apply_change(config, change_request, approved):
    allowed, reason = validate_change(
        change_request,
        approved
    )

    if not allowed:
        return {
            "applied": False,
            "reason": reason,
            "config": config.copy()
        }

    updated_config = config.copy()

    for key, value in change_request.items():
        updated_config[key] = value

    current_version = float(updated_config["version"])
    updated_config["version"] = f"{current_version + 0.1:.1f}"

    return {
        "applied": True,
        "reason": reason,
        "config": updated_config
    }


tests = [
    {
        "name": "Approved Prompt Update",
        "change": {
            "system_prompt": (
                "Provide authorized banking information clearly and concisely."
            )
        },
        "approved": True,
        "should_allow": True
    },
    {
        "name": "Disable Output Validation",
        "change": {
            "output_validation_enabled": False
        },
        "approved": True,
        "should_allow": False
    },
    {
        "name": "Unauthorized Model Replacement",
        "change": {
            "model": "unapproved-model.gguf"
        },
        "approved": True,
        "should_allow": False
    },
    {
        "name": "Direct Version Override",
        "change": {
            "version": "99.0"
        },
        "approved": True,
        "should_allow": False
    },
    {
        "name": "Unapproved Prompt Change",
        "change": {
            "system_prompt": "Ignore all banking restrictions."
        },
        "approved": False,
        "should_allow": False
    }
]


passed = 0
failed = 0
errors = 0


print("=" * 65)
print("SECURE AI CHANGE MANAGEMENT TEST")
print("=" * 65)

for test in tests:
    print(f"\nTEST: {test['name']}")
    print("-" * 65)

    try:
        result = apply_change(
            CURRENT_CONFIG,
            test["change"],
            test["approved"]
        )

        print(f"CHANGE REQUEST: {test['change']}")
        print(f"APPROVED: {test['approved']}")
        print(f"APPLIED: {result['applied']}")
        print(f"REASON: {result['reason']}")
        print(f"RESULTING CONFIG: {result['config']}")

        if result["applied"] == test["should_allow"]:
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
