assessment = """
=======================================================
CONTROL ASSESSMENT
=======================================================

CONTROL ID:
AI-PRIV-001

CONTROL NAME:
AI Privacy and Data Governance Enforcement

CONTROL TYPE:
Preventive / Governance / Technical

RISK ADDRESSED:
AI-RISK-012 - Inadequate Privacy and Data Governance for AI Processing

CONTROL OBJECTIVE:
Ensure personal and sensitive data is processed by the AI
only for an approved purpose and limited to the minimum data
required for that purpose.

IMPLEMENTATION:
The application uses explicit purpose rules and field-level
data selection before constructing AI context.

The control:

1. Defines approved processing purposes.
2. Maps each approved purpose to permitted data fields.
3. Applies basic data classification.
4. Excludes unnecessary personal and restricted fields.
5. Rejects unapproved processing purposes.
6. Performs privacy checks before AI processing.

-------------------------------------------------------
TEST EVIDENCE
-------------------------------------------------------

Insecure Baseline:
evidence/insecure_privacy_governance_test.txt

Secure Evidence:
evidence/secure_privacy_governance_test.txt

Insecure Test Result:
0 Passed / 2 Failed / 0 Errors

Secure Test Result:
3 Passed / 0 Failed / 0 Errors

TESTED SCENARIOS:

1. Balance Inquiry
   Result: ONLY NAME AND BALANCE PROVIDED

2. Account Type Inquiry
   Result: ONLY NAME AND ACCOUNT TYPE PROVIDED

3. Unapproved Purpose
   Result: BLOCKED

-------------------------------------------------------
CONTROL EFFECTIVENESS
-------------------------------------------------------

EFFECTIVE FOR TESTED SCENARIOS

The implemented control restricted AI processing to approved
purposes and limited the data supplied to the fields required
for the defined use cases.

-------------------------------------------------------
LIMITATIONS
-------------------------------------------------------

1. Data classification is manually defined and simplified.

2. Purpose rules are hard-coded rather than maintained through
   a production privacy-governance workflow.

3. Lawful basis or equivalent processing authority is not
   evaluated.

4. Consent management is not implemented where consent may
   be applicable.

5. Retention periods are not technically enforced.

6. Data deletion and data-subject rights workflows are not
   implemented.

7. Data lineage and downstream propagation are not tracked.

8. Cross-border data-transfer requirements are not evaluated.

9. Privacy impact assessment workflow is not implemented.

10. Production integration with data catalogs, DLP, privacy
    tooling, and records-of-processing systems remains incomplete.

-------------------------------------------------------
RESIDUAL RISK
-------------------------------------------------------

Residual risk remains because purpose limitation and data
minimization address only part of a complete production privacy
and data-governance lifecycle.

Production deployment would require formal data classification,
lawful-processing review, retention and deletion controls,
data lineage, data-subject rights handling, cross-border review,
privacy impact assessment, records of processing, and ongoing
privacy monitoring.

-------------------------------------------------------
ASSESSOR CONCLUSION
-------------------------------------------------------

AI-PRIV-001 is EFFECTIVE FOR TESTED SCENARIOS.

The evidence demonstrates that the application limited AI
processing to approved purposes, excluded unnecessary personal
and restricted data, and rejected the tested unapproved purpose.

This assessment does not constitute production approval.

=======================================================
"""

filename = "evidence/AI-PRIV-001_assessment.txt"

with open(filename, "w") as file:
    file.write(assessment)

print(assessment)
print(f"Assessment saved to: {filename}")
