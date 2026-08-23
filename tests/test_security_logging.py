import json

LOG_FILE = "evidence/AI_Security_Events.jsonl"

required_fields = {
    "timestamp",
    "event_id",
    "system_id",
    "user_id",
    "event_type",
    "action",
    "authorization_result",
    "security_result",
    "risk_level"
}

prohibited_terms = {
    "pin",
    "card_number",
    "TEST-PIN-4821",
    "TEST-CARD-0001"
}

expected_security_events = {
    "CROSS_CUSTOMER_REQUEST",
    "ROLE_MANIPULATION",
    "PROMPT_INJECTION"
}

passed = 0
failed = 0
errors = 0

print("\n==========================================")
print(" AI-LOG-001 SECURITY LOGGING CONTROL TEST")
print("==========================================")
print()

try:
    events = []

    with open(LOG_FILE, "r") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            events.append(json.loads(line))

except Exception as error:
    print("ERROR: Unable to read or parse log file")
    print(error)
    raise SystemExit(1)


def record_result(test_name, success, detail=""):
    global passed, failed

    print("------------------------------------------")
    print("TEST:", test_name)

    if success:
        print("RESULT: PASS")
        passed += 1
    else:
        print("RESULT: FAIL")
        failed += 1

    if detail:
        print("DETAIL:", detail)

    print()


# --------------------------------------------------
# TEST 1 - Log file contains valid events
# --------------------------------------------------

record_result(
    "Valid JSONL Events",
    len(events) > 0,
    f"Events loaded: {len(events)}"
)


# --------------------------------------------------
# TEST 2 - Required audit fields exist
# --------------------------------------------------

missing_field_events = []

for index, event in enumerate(events, start=1):
    missing = required_fields - set(event.keys())

    if missing:
        missing_field_events.append(
            f"Event {index}: {sorted(missing)}"
        )

record_result(
    "Required Audit Fields",
    len(missing_field_events) == 0,
    "; ".join(missing_field_events)
    if missing_field_events
    else "All required fields present"
)


# --------------------------------------------------
# TEST 3 - Event IDs are unique
# --------------------------------------------------

event_ids = [
    event.get("event_id")
    for event in events
]

unique_ids = set(event_ids)

record_result(
    "Unique Event IDs",
    len(event_ids) == len(unique_ids),
    f"Total IDs: {len(event_ids)}, Unique IDs: {len(unique_ids)}"
)


# --------------------------------------------------
# TEST 4 - High-risk security events captured
# --------------------------------------------------

captured_security_events = {
    event.get("event_type")
    for event in events
    if event.get("risk_level") == "HIGH"
}

missing_security_events = (
    expected_security_events - captured_security_events
)

record_result(
    "High-Risk Security Events Captured",
    len(missing_security_events) == 0,
    (
        "Missing: " + ", ".join(sorted(missing_security_events))
        if missing_security_events
        else "All expected high-risk events captured"
    )
)


# --------------------------------------------------
# TEST 5 - Blocked activity records denial correctly
# --------------------------------------------------

blocked_event_errors = []

for event in events:
    if event.get("risk_level") == "HIGH":
        if (
            event.get("authorization_result") != "DENIED"
            or event.get("security_result") != "BLOCKED"
        ):
            blocked_event_errors.append(
                event.get("event_id", "UNKNOWN")
            )

record_result(
    "Authorization Decisions Logged",
    len(blocked_event_errors) == 0,
    (
        "Incorrect events: " + ", ".join(blocked_event_errors)
        if blocked_event_errors
        else "High-risk events correctly recorded as DENIED/BLOCKED"
    )
)


# --------------------------------------------------
# TEST 6 - Sensitive data is excluded from logs
# --------------------------------------------------

sensitive_findings = []

for index, event in enumerate(events, start=1):
    event_text = json.dumps(event).lower()

    for term in prohibited_terms:
        if term.lower() in event_text:
            sensitive_findings.append(
                f"Event {index}: {term}"
            )

record_result(
    "Sensitive Data Excluded",
    len(sensitive_findings) == 0,
    (
        "; ".join(sensitive_findings)
        if sensitive_findings
        else "No prohibited sensitive data detected"
    )
)


# --------------------------------------------------
# TEST 7 - Normal authorized activity captured
# --------------------------------------------------

normal_events = [
    event
    for event in events
    if (
        event.get("event_type") == "ACCOUNT_QUERY"
        and event.get("authorization_result") == "ALLOWED"
        and event.get("security_result") == "NORMAL"
    )
]

record_result(
    "Normal Authorized Activity Captured",
    len(normal_events) > 0,
    f"Normal authorized events found: {len(normal_events)}"
)


print("==========================================")
print(" TEST SUMMARY")
print("==========================================")
print("PASSED:", passed)
print("FAILED:", failed)
print("ERRORS:", errors)
print("TOTAL:", passed + failed + errors)
print("==========================================")
