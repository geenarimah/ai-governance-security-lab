SECURITY_EVENTS = [
    {
        "event_id": "EVT-001",
        "event_type": "PROMPT_INJECTION",
        "risk_level": "HIGH",
        "details": "User attempted to override AI restrictions."
    },
    {
        "event_id": "EVT-002",
        "event_type": "CROSS_CUSTOMER_ACCESS",
        "risk_level": "HIGH",
        "details": "User attempted to access another customer's information."
    },
    {
        "event_id": "EVT-003",
        "event_type": "NORMAL_QUERY",
        "risk_level": "LOW",
        "details": "Authorized balance inquiry."
    }
]


def handle_incident(event):
    """
    INSECURE DESIGN:
    Events are received but no formal incident-response
    process is enforced.
    """

    return {
        "incident_created": False,
        "contained": False,
        "escalated": False,
        "evidence_preserved": False,
        "status": "No formal response"
    }


tests = [
    {
        "name": "High-Risk Prompt Injection",
        "event": SECURITY_EVENTS[0],
        "should_create_incident": True
    },
    {
        "name": "High-Risk Cross-Customer Access",
        "event": SECURITY_EVENTS[1],
        "should_create_incident": True
    },
    {
        "name": "Normal Authorized Query",
        "event": SECURITY_EVENTS[2],
        "should_create_incident": False
    }
]


passed = 0
failed = 0
errors = 0


print("=" * 65)
print("INSECURE AI INCIDENT RESPONSE TEST")
print("=" * 65)

for test in tests:
    print(f"\nTEST: {test['name']}")
    print("-" * 65)

    try:
        result = handle_incident(test["event"])

        print(f"EVENT: {test['event']}")
        print(f"INCIDENT CREATED: {result['incident_created']}")
        print(f"CONTAINED: {result['contained']}")
        print(f"ESCALATED: {result['escalated']}")
        print(f"EVIDENCE PRESERVED: {result['evidence_preserved']}")
        print(f"STATUS: {result['status']}")

        actual = result["incident_created"]

        if actual == test["should_create_incident"]:
            print("RESULT: PASS")
            passed += 1
        else:
            print(
                "RESULT: FAIL - security event did not trigger "
                "required incident-response handling"
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
