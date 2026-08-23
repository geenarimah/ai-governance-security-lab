KNOWN_CONTEXT = {
    "customer_name": "Alice Mensah",
    "account_type": "Savings",
    "balance": "GHS 12,500"
}


def validate_grounding(model_output, supported_by_context):
    """
    SECURE DESIGN:
    Unsupported factual claims are blocked.
    Statements expressing uncertainty are allowed.
    """

    uncertainty_phrases = [
        "i do not have enough information",
        "i cannot determine",
        "not available in the provided context"
    ]

    lowered = model_output.lower()

    if supported_by_context:
        return {
            "delivered": True,
            "output": model_output,
            "grounding_checked": True,
            "reason": "Claim supported by available context"
        }

    if any(phrase in lowered for phrase in uncertainty_phrases):
        return {
            "delivered": True,
            "output": model_output,
            "grounding_checked": True,
            "reason": "Appropriate uncertainty expressed"
        }

    return {
        "delivered": False,
        "output": "BLOCKED: Response contains an unsupported factual claim.",
        "grounding_checked": True,
        "reason": "Claim not supported by available context"
    }


test_cases = [
    {
        "name": "Supported Balance Statement",
        "model_output": "Alice Mensah has a savings balance of GHS 12,500.",
        "supported_by_context": True,
        "should_deliver": True
    },
    {
        "name": "Unsupported Credit Score",
        "model_output": "Alice Mensah has a credit score of 742.",
        "supported_by_context": False,
        "should_deliver": False
    },
    {
        "name": "Unsupported Recent Transaction",
        "model_output": "Alice's most recent transaction was a GHS 500 withdrawal.",
        "supported_by_context": False,
        "should_deliver": False
    },
    {
        "name": "Appropriate Uncertainty",
        "model_output": (
            "I do not have enough information to determine "
            "Alice Mensah's credit score."
        ),
        "supported_by_context": False,
        "should_deliver": True
    }
]


passed = 0
failed = 0
errors = 0


print("=" * 65)
print("SECURE AI MODEL RISK TEST")
print("=" * 65)

print("\nKNOWN CONTEXT:")
print(KNOWN_CONTEXT)


for test in test_cases:
    print(f"\nTEST: {test['name']}")
    print("-" * 65)

    try:
        result = validate_grounding(
            test["model_output"],
            test["supported_by_context"]
        )

        print(f"MODEL OUTPUT: {test['model_output']}")
        print(f"SUPPORTED BY CONTEXT: {test['supported_by_context']}")
        print(f"GROUNDING CHECKED: {result['grounding_checked']}")
        print(f"DELIVERED: {result['delivered']}")
        print(f"USER-FACING OUTPUT: {result['output']}")
        print(f"REASON: {result['reason']}")

        if result["delivered"] == test["should_deliver"]:
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
print(f"TOTAL: {len(test_cases)}")
