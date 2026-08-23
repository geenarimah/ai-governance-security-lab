CUSTOMER_RECORD = {
    "name": "Alice Mensah",
    "account_type": "Savings",
    "balance": "GHS 12,500",
    "date_of_birth": "1987-04-15",
    "phone_number": "TEST-PHONE-001",
    "home_address": "TEST-ADDRESS-001, Accra",
    "national_id": "TEST-NATIONAL-ID-001"
}


def prepare_ai_context(record, purpose):
    """
    INSECURE DESIGN:
    The application sends the entire customer record to the AI
    without enforcing purpose limitation or data classification.
    """

    return {
        "purpose": purpose,
        "data_sent": record.copy(),
        "privacy_checked": False
    }


tests = [
    {
        "name": "Balance Inquiry",
        "purpose": "balance_inquiry",
        "forbidden_fields": [
            "date_of_birth",
            "phone_number",
            "home_address",
            "national_id"
        ]
    },
    {
        "name": "Account Type Inquiry",
        "purpose": "account_type_inquiry",
        "forbidden_fields": [
            "date_of_birth",
            "phone_number",
            "home_address",
            "national_id"
        ]
    }
]


passed = 0
failed = 0
errors = 0


print("=" * 65)
print("INSECURE AI PRIVACY AND DATA GOVERNANCE TEST")
print("=" * 65)

for test in tests:
    print(f"\nTEST: {test['name']}")
    print("-" * 65)

    try:
        result = prepare_ai_context(
            CUSTOMER_RECORD,
            test["purpose"]
        )

        print(f"PURPOSE: {result['purpose']}")
        print(f"PRIVACY CHECKED: {result['privacy_checked']}")
        print(f"DATA SENT: {result['data_sent']}")

        exposed = [
            field
            for field in test["forbidden_fields"]
            if field in result["data_sent"]
        ]

        if exposed:
            print(
                "RESULT: FAIL - unnecessary personal data "
                f"was sent: {exposed}"
            )
            failed += 1
        else:
            print("RESULT: PASS")
            passed += 1

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
