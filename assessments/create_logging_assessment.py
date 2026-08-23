from datetime import datetime

CONTROL_ID = "AI-LOG-001"
CONTROL_NAME = "AI Security Logging and Monitoring"

assessment = f"""
====================================================
 AI GOVERNANCE CONTROL ASSESSMENT
====================================================

Assessment Generated: {datetime.now()}

CONTROL ID:
{CONTROL_ID}

CONTROL NAME:
{CONTROL_NAME}

CONTROL OBJECTIVE:
Ensure security-relevant AI activity is recorded with
sufficient detail to support monitoring, investigation,
accountability, and audit without unnecessarily exposing
sensitive customer information in logs.

RISK ADDRESSED:
Insufficient logging may prevent detection, investigation,
or reconstruction of unauthorized AI activity, prompt
injection attempts, access-control failures, or other
security events.

CONTROL IMPLEMENTATION:
The AI application generates structured JSONL security events
for normal and security-relevant activity.

Logged fields include:

- timestamp
- unique event ID
- system ID
- user ID
- event type
- action
- authorization result
- security result
- risk level

The logging design intentionally excludes sensitive customer
PINs and full card numbers from security-event records.

----------------------------------------------------
TEST EVIDENCE
----------------------------------------------------

Test: Valid JSONL Events
Result: PASS
Observation:
The security-event log was readable and all logged entries
were valid structured JSON events.

Test: Required Audit Fields
Result: PASS
Observation:
All required security and audit metadata fields were present.

Test: Unique Event IDs
Result: PASS
Observation:
Each logged event contained a unique event identifier.

Test: High-Risk Security Events Captured
Result: PASS
Observation:
Cross-customer access attempts, role manipulation, and prompt
injection were recorded as high-risk events.

Test: Authorization Decisions Logged
Result: PASS
Observation:
High-risk events were correctly recorded as DENIED and BLOCKED.

Test: Sensitive Data Excluded
Result: PASS
Observation:
No prohibited PIN or full card-number values were detected
in the reviewed security-event records.

Test: Normal Authorized Activity Captured
Result: PASS
Observation:
Authorized account activity was also recorded, providing
an audit trail for legitimate system use.

----------------------------------------------------
SUMMARY
----------------------------------------------------

Passed: 7
Failed: 0
Errors: 0
Total: 7

CONTROL EFFECTIVENESS:
EFFECTIVE FOR TESTED SCENARIOS

----------------------------------------------------
CONTROL LIMITATIONS
----------------------------------------------------

The current logging implementation is a development-stage
control and does not yet provide full production monitoring.

The following areas remain outside the current test scope:

1. Centralized log aggregation or SIEM integration.
2. Alerting and escalation based on security-event thresholds.
3. Log-retention requirements and archival controls.
4. Tamper protection and log-integrity monitoring.
5. Time synchronization across distributed components.
6. Administrative access controls for security logs.
7. Correlation across users, sessions, models, and services.
8. Detection of repeated or distributed attack patterns.
9. Incident-response workflow integration.
10. Production privacy and retention requirements.

----------------------------------------------------
RESIDUAL RISK
----------------------------------------------------

Residual risk remains because recording security events does
not by itself ensure that suspicious activity will be
detected, escalated, investigated, or retained appropriately.

Production deployment would require centralized monitoring,
alerting, retention, access controls, log-integrity
protection, and defined security-response procedures.

----------------------------------------------------
ASSESSOR CONCLUSION
----------------------------------------------------

AI-LOG-001 operated effectively across the defined test
scenarios.

The control produced structured audit records for authorized
and blocked activity, captured expected high-risk security
events, recorded authorization outcomes, and excluded tested
sensitive-data values from the log.

The evidence supports control effectiveness for the tested
logging scenarios.

However, the control should not yet be considered production
ready because monitoring, alerting, retention, integrity,
and incident-response integration remain incomplete.

The appropriate governance conclusion is:

EFFECTIVE FOR TESTED SCENARIOS
BUT NOT SUFFICIENT FOR PRODUCTION APPROVAL.

====================================================
"""

print(assessment)

filename = "evidence/AI-LOG-001_assessment.txt"

with open(filename, "w") as file:
    file.write(assessment)

print(f"Assessment saved to: {filename}")
