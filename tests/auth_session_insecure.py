users = {
    "alice": {
        "password": "TEST-ALICE-PASS",
        "role": "customer"
    },
    "kwame": {
        "password": "TEST-KWAME-PASS",
        "role": "customer"
    }
}

active_session = {
    "session_id": "SESSION-ALICE-001",
    "user_id": "alice",
    "authenticated": True
}


def access_ai(session, requested_user):
    if session.get("authenticated"):
        return {
            "allowed": True,
            "message": (
                f"AI access granted for requested user: {requested_user}"
            )
        }

    return {
        "allowed": False,
        "message": "AI access denied"
    }


tests = [
    {
        "name": "Valid Alice Session",
        "session": active_session,
        "requested_user": "alice",
        "should_allow": True
    },
    {
        "name": "Session User Switched to Kwame",
        "session": active_session,
        "requested_user": "kwame",
        "should_allow": False
    },
    {
        "name": "Forged Authenticated Session",
        "session": {
            "session_id": "FAKE-SESSION-999",
            "user_id": "kwame",
            "authenticated": True
        },
        "requested_user": "kwame",
        "should_allow": False
    },
    {
        "name": "Missing Session Identity Binding",
        "session": {
            "session_id": "SESSION-UNKNOWN-001",
            "authenticated": True
        },
        "requested_user": "alice",
        "should_allow": False
    }
]


passed = 0
failed = 0
errors = 0


print("=" * 60)
print("INSECURE AUTHENTICATION AND SESSION TEST")
print("=" * 60)

for test in tests:
    print(f"\nTEST: {test['name']}")
    print("-" * 60)

    try:
        result = access_ai(
            test["session"],
            test["requested_user"]
        )

        print(f"SESSION: {test['session']}")
        print(f"REQUESTED USER: {test['requested_user']}")
        print(f"APPLICATION RESULT: {result}")

        actual_allow = result["allowed"]

        if actual_allow == test["should_allow"]:
            print("RESULT: PASS")
            passed += 1
        else:
            print(
                "RESULT: FAIL - authentication/session control "
                "did not enforce expected identity binding"
            )
            failed += 1

    except Exception as exc:
        print(f"RESULT: ERROR - {exc}")
        errors += 1


print("\n" + "=" * 60)
print("TEST SUMMARY")
print("=" * 60)
print(f"PASSED: {passed}")
print(f"FAILED: {failed}")
print(f"ERRORS: {errors}")
print(f"TOTAL: {len(tests)}")
