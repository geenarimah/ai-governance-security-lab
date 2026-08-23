CUSTOMER_RECORD = {
    "name": "Alice Mensah",
    "account_type": "Savings",
    "balance": "GHS 12,500",
    "date_of_birth": "1987-04-15",
    "phone_number": "TEST-PHONE-001",
    "home_address": "TEST-ADDRESS-001, Accra",
    "national_id": "TEST-NATIONAL-ID-001"
}


PURPOSE_RULES = {
    "balance_inquiry": [
        "name",
        "balance"
    ],
    "account_type_inquiry": [
        "name",
        "account_type"
    ]
}


DATA_CLASSIFICATION = {
    "name": "Personal",
    "account_type": "Internal",
    "balance": "Financial",
    "date_of_birth": "Personal",
    "phone_number": "Personal",
    "home_address": "Personal",
    "national_id": "Restricted"
}


def prepare_ai_context(record, purpose):
    """
    SECURE DESIGN:
    Data is selected according to the defined purpose before
    being sent into the AI workflow.
    """

    if purpose not in PURPOSE_RULES:
        return {
            "allowed": False,
            "purpose": purpose,
            "privacy_checked": True,
            "data_sent": {},
            "reason": "Purpose is not approved"
        }

    allowed_fields = PURPOSE_RULES[purpose]

    filtered_data = {
        field: record[field]
        for field in allowed_fields
        if field in record
    }

    return {
        "allowed": True,
        "purpose": purpose,
        "privacy_checked": True,
        "data_sent": filtered_data,
        "reason": "Purpose limitation and data minimization enforced"
    }


tests = [
    {
        "name": "Balance Inquiry",
        "purpose": "balance_inquiry",
        "expected_fields": {
            "name",
            "balance"
        }
    },
    {
        "name": "Account Type Inquiry",
        "purpose": "account_type_inquiry",
        "expected_fields": {
            "name",
            "account_type"
        }
    },
    {
        "name": "Unapproved Purpose",
        "purpose": "marketing_profile",
        "expected_fields": set()
    }
]


passed = 0
failed = 0
errors = 0


print("=" * 65)
print("SECURE AI PRIVACY AND DATA GOVERNANCE TEST")
print("=" * 65)

print("\nDATA CLASSIFICATION:")
for field, classification in DATA_CLASSIFICATION.items():
    print(f"{field}: {classification}")


for test in tests:
    print(f"\nTEST: {test['name']}")
    print("-" * 65)

    try:
        result = prepare_ai_context(
            CUSTOMER_RECORD,
            test["purpose"]
        )

        actual_fields = set(result["data_sent"].keys())

        print(f"PURPOSE: {result['purpose']}")
        print(f"PRIVACY CHECKED: {result['privacy_checked']}")
        print(f"ALLOWED: {result['allowed']}")
        print(f"DATA SENT: {result['data_sent']}")
        print(f"REASON: {result['reason']}")

        if actual_fields == test["expected_fields"]:
            print("RESULT: PASS")
            passed += 1
        else:
            print(
                "RESULT: FAIL - data sent did not match "
                "approved purpose requirements"
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
