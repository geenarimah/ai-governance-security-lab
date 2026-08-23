USER_CONTEXTS = {
    "alice": {
        "name": "Alice Mensah",
        "balance": "GHS 12,500"
    },
    "kwame": {
        "name": "Kwame Asante",
        "balance": "GHS 47,800"
    }
}

shared_context = {}


def process_request(session_id, user_id, requested_user):
    """
    INSECURE DESIGN:
    A shared context is reused across sessions without
    binding stored context to the current authenticated user.
    """

    if not shared_context:
        shared_context.update(USER_CONTEXTS[user_id])

    return {
        "session_id": session_id,
        "authenticated_user": user_id,
        "requested_user": requested_user,
        "response_context": shared_context.copy()
    }


tests = [
    {
        "name": "Alice Initial Session",
        "session_id": "SESSION-ALICE-001",
        "user_id": "alice",
        "requested_user": "alice",
        "expected_name": "Alice Mensah"
    },
    {
        "name": "Kwame New Session After Alice",
        "session_id": "SESSION-KWAME-001",
        "user_id": "kwame",
        "requested_user": "kwame",
        "expected_name": "Kwame Asante"
    }
]


passed = 0
failed = 0
errors = 0


print("=" * 65)
print("INSECURE MULTI-USER SESSION ISOLATION TEST")
print("=" * 65)

for test in tests:
    print(f"\nTEST: {test['name']}")
    print("-" * 65)

    try:
        result = process_request(
            test["session_id"],
            test["user_id"],
            test["requested_user"]
        )

        actual_name = result["response_context"]["name"]

        print(f"SESSION ID: {result['session_id']}")
        print(f"AUTHENTICATED USER: {result['authenticated_user']}")
        print(f"REQUESTED USER: {result['requested_user']}")
        print(f"RESPONSE CONTEXT: {result['response_context']}")

        if actual_name == test["expected_name"]:
            print("RESULT: PASS")
            passed += 1
        else:
            print(
                "RESULT: FAIL - session context crossed user boundary"
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
