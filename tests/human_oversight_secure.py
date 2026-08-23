MATERIAL_ACTIONS = {
    "balance_lookup": False,
    "account_closure": True,
    "large_transfer": True,
    "credential_reset": True
}


def process_ai_action(action, human_approved=False):
    material = MATERIAL_ACTIONS.get(action, False)

    if material and not human_approved:
        return {
            "executed": False,
            "material": True,
            "human_approved": False,
            "message": (
                "Action blocked pending required human approval"
            )
        }

    return {
        "executed": True,
        "material": material,
        "human_approved": human_approved,
        "message": f"Action executed: {action}"
    }


tests = [
    {
        "name": "Routine Balance Lookup",
        "action": "balance_lookup",
        "human_approved": False,
        "should_execute": True
    },
    {
        "name": "Account Closure Without Human Approval",
        "action": "account_closure",
        "human_approved": False,
        "should_execute": False
    },
    {
        "name": "Large Transfer Without Human Approval",
        "action": "large_transfer",
        "human_approved": False,
        "should_execute": False
    },
    {
        "name": "Credential Reset Without Human Approval",
        "action": "credential_reset",
        "human_approved": False,
        "should_execute": False
    },
    {
        "name": "Large Transfer With Human Approval",
        "action": "large_transfer",
        "human_approved": True,
        "should_execute": True
    }
]


passed = 0
failed = 0
errors = 0


print("=" * 65)
print("SECURE HUMAN OVERSIGHT TEST")
print("=" * 65)

for test in tests:
    print(f"\nTEST: {test['name']}")
    print("-" * 65)

    try:
        result = process_ai_action(
            test["action"],
            test["human_approved"]
        )

        print(f"ACTION: {test['action']}")
        print(f"MATERIAL: {result['material']}")
        print(f"HUMAN APPROVED: {test['human_approved']}")
        print(f"EXECUTED: {result['executed']}")
        print(f"MESSAGE: {result['message']}")

        if result["executed"] == test["should_execute"]:
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
