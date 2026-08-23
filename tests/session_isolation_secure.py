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

session_store = {}


def process_request(session_id, user_id, requested_user):
    """
    SECURE DESIGN:
    Session context is isolated by session ID and bound
    to the authenticated user.
    """

    if requested_user != user_id:
        return {
            "allowed": False,
            "session_id": session_id,
            "authenticated_user": user_id,
            "requested_user": requested_user,
            "response_context": None,
            "reason": "Requested user does not match authenticated user"
        }

    if session_id in session_store:
        session = session_store[session_id]

        if session["user_id"] != user_id:
            return {
                "allowed": False,
                "session_id": session_id,
                "authenticated_user": user_id,
                "requested_user": requested_user,
                "response_context": None,
                "reason": "Session is already bound to another user"
            }

    else:
        session_store[session_id] = {
            "user_id": user_id,
            "context": USER_CONTEXTS[user_id].copy()
        }

    return {
        "allowed": True,
        "session_id": session_id,
        "authenticated_user": user_id,
        "requested_user": requested_user,
        "response_context": session_store[session_id]["context"].copy(),
        "reason": "Session and user context validated"
    }


tests = [
    {
        "name": "Alice Initial Session",
        "session_id": "SESSION-ALICE-001",
        "user_id": "alice",
        "requested_user": "alice",
        "should_allow": True,
        "expected_name": "Alice Mensah"
    },
    {
        "name": "Kwame Separate Session",
        "session_id": "SESSION-KWAME-001",
        "user_id": "kwame",
        "requested_user": "kwame",
        "should_allow": True,
        "expected_name": "Kwame Asante"
    },
    {
        "name": "Kwame Attempts Alice Session",
        "session_id": "SESSION-ALICE-001",
        "user_id": "kwame",
        "requested_user": "kwame",
        "should_allow": False,
        "expected_name": None
    },
    {
        "name": "Alice Requests Kwame Context",
        "session_id": "SESSION-ALICE-001",
        "user_id": "alice",
        "requested_user": "kwame",
        "should_allow": False,
        "expected_name": None
    }
]


passed = 0
failed = 0
errors = 0


print("=" * 65)
print("SECURE MULTI-USER SESSION ISOLATION TEST")
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

        print(f"SESSION ID: {result['session_id']}")
        print(f"AUTHENTICATED USER: {result['authenticated_user']}")
        print(f"REQUESTED USER: {result['requested_user']}")
        print(f"ALLOWED: {result['allowed']}")
        print(f"RESPONSE CONTEXT: {result['response_context']}")
        print(f"REASON: {result['reason']}")

        correct_allow = result["allowed"] == test["should_allow"]

        if result["allowed"]:
            actual_name = result["response_context"]["name"]
            correct_context = actual_name == test["expected_name"]
        else:
            correct_context = result["response_context"] is None

        if correct_allow and correct_context:
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
