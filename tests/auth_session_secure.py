VALID_SESSIONS = {
    "SESSION-ALICE-001": {
        "user_id": "alice",
        "authenticated": True,
        "active": True
    },
    "SESSION-KWAME-001": {
        "user_id": "kwame",
        "authenticated": True,
        "active": True
    }
}


def validate_session(session):
    session_id = session.get("session_id")

    if not session_id:
        return {
            "valid": False,
            "reason": "Missing session ID"
        }

    trusted_session = VALID_SESSIONS.get(session_id)

    if not trusted_session:
        return {
            "valid": False,
            "reason": "Unknown or forged session"
        }

    if not trusted_session.get("authenticated"):
        return {
            "valid": False,
            "reason": "Session is not authenticated"
        }

    if not trusted_session.get("active"):
        return {
            "valid": False,
            "reason": "Session is inactive"
        }

    supplied_user = session.get("user_id")
    trusted_user = trusted_session.get("user_id")

    if supplied_user != trusted_user:
        return {
            "valid": False,
            "reason": "Session identity mismatch"
        }

    return {
        "valid": True,
        "user_id": trusted_user,
        "reason": "Validated session"
    }


def access_ai(session, requested_user):
    validation = validate_session(session)

    if not validation["valid"]:
        return {
            "allowed": False,
            "message": "AI access denied",
            "reason": validation["reason"]
        }

    authenticated_user = validation["user_id"]

    if requested_user != authenticated_user:
        return {
            "allowed": False,
            "message": "AI access denied",
            "reason": "Requested identity does not match authenticated identity"
        }

    return {
        "allowed": True,
        "message": (
            f"AI access granted for authenticated user: "
            f"{authenticated_user}"
        ),
        "reason": "Authenticated session and identity binding validated"
    }


tests = [
    {
        "name": "Valid Alice Session",
        "session": {
            "session_id": "SESSION-ALICE-001",
            "user_id": "alice"
        },
        "requested_user": "alice",
        "should_allow": True
    },
    {
        "name": "Session User Switched to Kwame",
        "session": {
            "session_id": "SESSION-ALICE-001",
            "user_id": "alice"
        },
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
            "session_id": "SESSION-ALICE-001"
        },
        "requested_user": "alice",
        "should_allow": False
    }
]


passed = 0
failed = 0
errors = 0


print("=" * 60)
print("SECURE AUTHENTICATION AND SESSION TEST")
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
            print("RESULT: FAIL")
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
