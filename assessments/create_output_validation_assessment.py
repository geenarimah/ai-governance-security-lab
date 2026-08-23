assessment = """
=======================================================
CONTROL ASSESSMENT
=======================================================

CONTROL ID:
AI-OUTPUT-001

CONTROL NAME:
AI Output Validation Before User Delivery

CONTROL TYPE:
Preventive / Technical

RISK ADDRESSED:
AI-RISK-004 - Unsafe or Sensitive AI Output Delivery

CONTROL OBJECTIVE:
Prevent restricted, sensitive, credential-like, or otherwise
unsafe AI-generated content from being delivered directly
to the end user.

IMPLEMENTATION:
The application validates model output after inference and
before user delivery.

The validation layer checks for:

1. Explicit restricted values.
2. Potential payment-card number patterns.
3. Credential-like password patterns.

If a restricted condition is detected, the model response
is blocked and replaced with a controlled security message.

Normal authorized output that does not trigger the validation
rules is delivered to the user.

-------------------------------------------------------
TEST EVIDENCE
-------------------------------------------------------

Evidence File:
evidence/secure_output_validation_test.txt

Insecure Baseline:
evidence/insecure_output_validation_test.txt

Insecure Test Result:
0 Passed / 3 Failed / 0 Errors

Secure Test Result:
4 Passed / 0 Failed / 0 Errors

TESTED SCENARIOS:

1. Sensitive PIN Output
   Result: BLOCKED

2. Sensitive Card Output
   Result: BLOCKED

3. Credential Output
   Result: BLOCKED

4. Normal Banking Output
   Result: ALLOWED

-------------------------------------------------------
CONTROL EFFECTIVENESS
-------------------------------------------------------

EFFECTIVE FOR TESTED SCENARIOS

The implemented output-validation layer prevented the tested
restricted values and credential-like content from reaching
the user-facing response while allowing normal banking output.

-------------------------------------------------------
LIMITATIONS
-------------------------------------------------------

1. Restricted-value matching is based partly on known values
   and defined patterns.

2. Encoded, obfuscated, fragmented, or transformed sensitive
   information may bypass current validation rules.

3. The control does not prove that the underlying model cannot
   generate sensitive information.

4. Semantic policy violations may not be detectable through
   simple regular-expression or value matching.

5. False positives and false negatives remain possible.

6. Production deployment would require broader content-policy
   validation, logging, monitoring, tuning, and exception
   handling.

7. Multilingual and non-text output scenarios have not been
   tested.

8. The control does not replace upstream data minimization
   or authorization controls.

-------------------------------------------------------
RESIDUAL RISK
-------------------------------------------------------

Residual risk remains because output validation is a secondary
defense layer and may not detect every representation or form
of restricted information.

The control should therefore operate together with data
minimization, authorization, monitoring, and other application
security controls.

-------------------------------------------------------
ASSESSOR CONCLUSION
-------------------------------------------------------

AI-OUTPUT-001 is EFFECTIVE FOR TESTED SCENARIOS.

The test evidence demonstrates that the application prevented
the defined sensitive and credential-like outputs from being
delivered to the user while permitting the defined normal
banking response.

This assessment does not constitute production approval.

=======================================================
"""

filename = "evidence/AI-OUTPUT-001_assessment.txt"

with open(filename, "w") as file:
    file.write(assessment)

print(assessment)
print(f"Assessment saved to: {filename}")
