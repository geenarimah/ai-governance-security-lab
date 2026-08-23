import csv

controls = [
    {
        "Control ID": "AI-DATA-001",
        "Control Name": "Sensitive Data Minimization Before LLM Processing",
        "Risk ID": "AI-RISK-001",
        "Risk Description": "Sensitive authentication or payment data may be disclosed by the AI system.",
        "Control Objective": "Prevent restricted data from reaching the LLM unless explicitly authorized.",
        "Control Type": "Preventive / Technical",
        "Implementation": "Application allowlists permitted fields and removes PIN and full card-number fields before LLM processing.",
        "Test Procedure": "Direct request, prompt injection, transformation, reverse-PIN and card-number adversarial tests.",
        "Evidence": "secure_data_minimization_test.txt; ai_control_evidence.json; AI-DATA-001_assessment.txt",
        "Test Result": "5 Passed / 0 Failed / 0 Errors",
        "Control Effectiveness": "Effective for tested scenarios",
        "Residual Risk": "Encoding, reconstruction, authorization, logging and future model-change risks remain.",
        "Control Owner": "AI Application / Security Team",
        "Review Frequency": "Quarterly and after material model/application changes",
        "NIST AI RMF Mapping": "MAP / MEASURE / MANAGE",
        "ISO/IEC 42001 Mapping": "Risk management / AI system controls",
        "Status": "Implemented and Tested"
    },
    {
        "Control ID": "AI-ACCESS-001",
        "Control Name": "User-Level Authorization Before LLM Processing",
        "Risk ID": "AI-RISK-002",
        "Risk Description": "Users may obtain another customer's information through the AI interface.",
        "Control Objective": "Ensure the LLM receives only information the authenticated user is authorized to access.",
        "Control Type": "Preventive / Technical",
        "Implementation": "Application-layer authorization selects the authenticated user's record before constructing LLM context.",
        "Test Procedure": "Own-account, cross-customer, role-manipulation and prompt-injection tests.",
        "Evidence": "secure_access_control_v2_test.txt; AI-ACCESS-001_assessment.txt",
        "Test Result": "4 Passed / 0 Failed / 0 Errors",
        "Control Effectiveness": "Effective for tested scenarios",
        "Residual Risk": "Production identity, session, RBAC/ABAC, logging and indirect retrieval risks remain.",
        "Control Owner": "AI Application / IAM / Security Team",
        "Review Frequency": "Quarterly and after authorization changes",
        "NIST AI RMF Mapping": "GOVERN / MAP / MANAGE",
        "ISO/IEC 42001 Mapping": "Access control / risk treatment / AI system operation",
        "Status": "Implemented and Tested"
    },
    {

        "Control ID": "AI-LOG-001",
        "Control Name": "AI Security Logging and Monitoring",
        "Risk ID": "AI-RISK-003",
        "Risk Description": (
            "Security-relevant AI activity may not be detected, "
            "investigated, reconstructed, or escalated because of "
            "insufficient logging and monitoring."
        ),
        "Control Objective": (
            "Record security-relevant AI activity with sufficient "
            "metadata to support monitoring, investigation, "
            "accountability, and audit."
        ),
        "Control Type": "Detective / Technical",
        "Implementation": (
            "The application generates structured JSONL security events "
            "containing timestamps, unique event IDs, system and user IDs, "
            "event types, authorization outcomes, security results, and "
            "risk levels while excluding tested sensitive values."
        ),
        "Test Procedure": (
            "Validate JSONL events, required audit fields, unique event IDs, "
            "high-risk event capture, authorization outcomes, sensitive-data "
            "exclusion, and normal authorized activity."
        ),
        "Evidence": (
            "AI_Security_Events.jsonl; "
            "AI-LOG-001_test.txt; "
            "AI-LOG-001_assessment.txt"
        ),
        "Test Result": "7 Passed / 0 Failed / 0 Errors",
        "Control Effectiveness": "Effective for tested scenarios",
        "Residual Risk": (
            "Centralized monitoring, alerting, retention, integrity "
            "protection, SIEM integration, and incident-response "
            "integration remain incomplete."
        ),
        "Control Owner": "Security Operations / AI Governance Team",
        "Review Frequency": (
            "Quarterly and after material logging or monitoring changes"
        ),
        "NIST AI RMF Mapping": "GOVERN / MEASURE / MANAGE",
        "ISO/IEC 42001 Mapping": (
            "Monitoring / logging / AI system operation"
        ),
            "Status": "Implemented and Tested"
},
{
    "Control ID": "AI-OUTPUT-001",
    "Control Name": "AI Output Validation Before User Delivery",
    "Risk ID": "AI-RISK-004",
    "Risk Description": (
        "AI-generated responses may contain restricted, sensitive, "
        "credential-like, malformed, or otherwise unsafe content that "
        "could be delivered directly to an end user."
    ),
    "Control Objective": (
        "Prevent restricted, sensitive, credential-like, or unsafe "
        "AI-generated content from being delivered directly to the user."
    ),
    "Control Type": "Preventive / Technical",
    "Implementation": (
        "The application validates model output after inference and before "
        "user delivery using restricted-value checks, payment-card pattern "
        "detection, and credential-like password detection. Responses that "
        "fail validation are blocked and replaced with a controlled message."
    ),
    "Test Procedure": (
        "Test sensitive PIN output, payment-card output, credential output, "
        "and normal authorized banking output to verify restricted content "
        "is blocked while legitimate output remains available."
    ),
    "Evidence": (
        "insecure_output_validation_test.txt; "
        "secure_output_validation_test.txt; "
        "AI-OUTPUT-001_assessment.txt"
    ),
    "Test Result": "4 Passed / 0 Failed / 0 Errors",
    "Control Effectiveness": "Effective for tested scenarios",
    "Residual Risk": (
        "Encoded, obfuscated, fragmented, transformed, multilingual, or "
        "semantic policy violations may bypass current validation rules. "
        "False positives and false negatives remain possible."
    ),
    "Control Owner": "AI Application / Security Team",
    "Review Frequency": (
        "Quarterly and after material model, prompt, or output-policy changes"
    ),
    "NIST AI RMF Mapping": "MEASURE / MANAGE",
    "ISO/IEC 42001 Mapping": (
        "AI system operation / risk treatment / output controls"
    ),
        "Status": "Implemented and Tested"
},
{
    "Control ID": "AI-AUTH-001",
    "Control Name": "Authentication and Session Assurance Before AI Access",
    "Risk ID": "AI-RISK-005",
    "Risk Description": (
        "Weak authentication or session handling may allow unauthorized "
        "AI access through forged, altered, reused, or improperly validated "
        "session information."
    ),
    "Control Objective": (
        "Ensure AI access is granted only through a valid, trusted, active, "
        "authenticated session that is correctly bound to the requesting "
        "user identity."
    ),
    "Control Type": "Preventive / Technical",
    "Implementation": (
        "The application validates the supplied session ID against a trusted "
        "server-side session store, verifies authenticated and active session "
        "state, enforces session-to-user identity binding, and rejects forged "
        "or identity-mismatched sessions before AI access."
    ),
    "Test Procedure": (
        "Test a valid authenticated session, cross-user identity switching, "
        "a forged authenticated session, and a session missing identity "
        "binding."
    ),
    "Evidence": (
        "insecure_auth_session_test.txt; "
        "secure_auth_session_test.txt; "
        "AI-AUTH-001_assessment.txt"
    ),
    "Test Result": "4 Passed / 0 Failed / 0 Errors",
    "Control Effectiveness": "Effective for tested scenarios",
    "Residual Risk": (
        "Password authentication, MFA, session expiration, revocation, "
        "token confidentiality, replay protection, token theft, concurrent "
        "session abuse, and production IAM integration remain incomplete."
    ),
    "Control Owner": "IAM / AI Application / Security Team",
    "Review Frequency": (
        "Quarterly and after material authentication or session changes"
    ),
    "NIST AI RMF Mapping": "GOVERN / MAP / MANAGE",
    "ISO/IEC 42001 Mapping": (
        "Access control / identity management / AI system operation"
    ),
        "Status": "Implemented and Tested"
},
{
    "Control ID": "AI-CHANGE-001",
    "Control Name": "AI Model and Configuration Change Management",
    "Risk ID": "AI-RISK-006",
    "Risk Description": (
        "Unauthorized, unapproved, or poorly controlled changes to the AI "
        "model, system prompt, configuration, validation logic, or related "
        "security settings may weaken previously tested controls or alter "
        "system behavior."
    ),
    "Control Objective": (
        "Ensure material AI model, prompt, configuration, and security-control "
        "changes are reviewed, approved, validated, versioned, and controlled "
        "before implementation."
    ),
    "Control Type": "Preventive / Governance / Technical",
    "Implementation": (
        "The application requires approval before applying changes, prevents "
        "tested security-control disablement, restricts model replacement to "
        "approved models, blocks direct version overrides, and applies a "
        "controlled version increment to approved changes."
    ),
    "Test Procedure": (
        "Test an approved prompt update, output-validation disablement, "
        "unauthorized model replacement, direct version override, and an "
        "unapproved prompt change."
    ),
    "Evidence": (
        "insecure_change_management_test.txt; "
        "secure_change_management_test.txt; "
        "AI-CHANGE-001_assessment.txt"
    ),
    "Test Result": "5 Passed / 0 Failed / 0 Errors",
    "Control Effectiveness": "Effective for tested scenarios",
    "Residual Risk": (
        "Formal approver workflows, separation of duties, regression gates, "
        "rollback, configuration integrity, model provenance verification, "
        "emergency-change procedures, CI/CD controls, and auditable change "
        "history remain incomplete."
    ),
    "Control Owner": "AI Application / AI Governance / Security Team",
    "Review Frequency": (
        "Quarterly and after material model, prompt, configuration, "
        "or deployment changes"
    ),
    "NIST AI RMF Mapping": "GOVERN / MAP / MEASURE / MANAGE",
    "ISO/IEC 42001 Mapping": (
        "Change management / AI system operation / risk treatment"
    ),
        "Status": "Implemented and Tested"
},
{
    "Control ID": "AI-HUMAN-001",
    "Control Name": "Human Oversight and Escalation for Material AI Decisions",
    "Risk ID": "AI-RISK-007",
    "Risk Description": (
        "Material AI-driven actions may proceed without appropriate human "
        "review, approval, escalation, or accountability, increasing the "
        "risk of unauthorized or harmful outcomes."
    ),
    "Control Objective": (
        "Ensure material AI-driven actions do not proceed without explicit "
        "human review and approval."
    ),
    "Control Type": "Preventive / Governance / Technical",
    "Implementation": (
        "The application classifies defined actions as material or "
        "non-material. Material actions are blocked unless explicit human "
        "approval is present, while routine informational actions may proceed."
    ),
    "Test Procedure": (
        "Test routine balance lookup, account closure without approval, "
        "large transfer without approval, credential reset without approval, "
        "and large transfer with human approval."
    ),
    "Evidence": (
        "insecure_human_oversight_test.txt; "
        "secure_human_oversight_test.txt; "
        "AI-HUMAN-001_assessment.txt"
    ),
    "Test Result": "5 Passed / 0 Failed / 0 Errors",
    "Control Effectiveness": "Effective for tested scenarios",
    "Residual Risk": (
        "Reviewer authentication, separation of duties, approval evidence, "
        "multi-level workflows, approval expiration, emergency override, "
        "centralized logging, and review-quality assurance remain incomplete."
    ),
    "Control Owner": "AI Governance / Business Operations / Security Team",
    "Review Frequency": (
        "Quarterly and after material changes to AI decision authority "
        "or human-approval workflows"
    ),
    "NIST AI RMF Mapping": "GOVERN / MAP / MANAGE",
    "ISO/IEC 42001 Mapping": (
        "Human oversight / accountability / AI system operation"
    ),
        "Status": "Implemented and Tested"
},
{
    "Control ID": "AI-IR-001",
    "Control Name": "AI-Specific Incident Response and Evidence Preservation",
    "Risk ID": "AI-RISK-008",
    "Risk Description": (
        "High-risk AI security events may not be contained, escalated, "
        "investigated, or supported by preserved evidence, increasing the "
        "impact and duration of security incidents."
    ),
    "Control Objective": (
        "Ensure high-risk AI security events trigger a defined incident-response "
        "process including incident creation, containment, escalation, and "
        "evidence preservation."
    ),
    "Control Type": "Detective / Corrective / Governance / Technical",
    "Implementation": (
        "The application evaluates AI security events by risk level. High-risk "
        "events trigger incident creation, assignment of an incident identifier, "
        "containment, escalation, evidence preservation, and initiation of a "
        "security response. Low-risk normal activity does not create an incident."
    ),
    "Test Procedure": (
        "Test high-risk prompt injection, high-risk cross-customer access, "
        "and normal authorized activity to verify appropriate incident creation, "
        "containment, escalation, and evidence preservation."
    ),
    "Evidence": (
        "insecure_incident_response_test.txt; "
        "secure_incident_response_test.txt; "
        "AI-IR-001_assessment.txt"
    ),
    "Test Result": "3 Passed / 0 Failed / 0 Errors",
    "Control Effectiveness": "Effective for tested scenarios",
    "Residual Risk": (
        "Integrated containment, authenticated responders, immutable evidence "
        "storage, chain of custody, notification procedures, recovery testing, "
        "case management, escalation channels, incident metrics, and "
        "post-incident review remain incomplete."
    ),
    "Control Owner": "Security Operations / Incident Response / AI Governance Team",
    "Review Frequency": (
        "Quarterly and after material incident-response process changes "
        "or significant AI security incidents"
    ),
    "NIST AI RMF Mapping": "GOVERN / MEASURE / MANAGE",
    "ISO/IEC 42001 Mapping": (
        "Incident management / monitoring / AI system operation"
    ),
        "Status": "Implemented and Tested"
},
{
    "Control ID": "AI-SESSION-001",
    "Control Name": "Multi-User Session and Context Isolation",
    "Risk ID": "AI-RISK-009",
    "Risk Description": (
        "Session or conversational context may cross user boundaries, "
        "allowing one authenticated user to receive another user's context "
        "or reuse a session bound to a different identity."
    ),
    "Control Objective": (
        "Ensure each authenticated user receives only session context bound "
        "to that user's identity and prevent cross-user session reuse or "
        "context crossover."
    ),
    "Control Type": "Preventive / Technical",
    "Implementation": (
        "The application maintains isolated session context indexed by "
        "session ID, binds each session to an authenticated user, verifies "
        "requested identity against authenticated identity, and blocks "
        "cross-user session reuse and context access."
    ),
    "Test Procedure": (
        "Test separate Alice and Kwame sessions, cross-user session reuse, "
        "and cross-user context requests to verify session and context "
        "isolation."
    ),
    "Evidence": (
        "insecure_session_isolation_test.txt; "
        "secure_session_isolation_test.txt; "
        "AI-SESSION-001_assessment.txt"
    ),
    "Test Result": "4 Passed / 0 Failed / 0 Errors",
    "Control Effectiveness": "Effective for tested scenarios",
    "Residual Risk": (
        "Secure session generation, expiration, revocation, replay "
        "protection, distributed session handling, privilege-change "
        "controls, transport protection, and production IAM integration "
        "remain incomplete."
    ),
    "Control Owner": "AI Application / IAM / Security Team",
    "Review Frequency": (
        "Quarterly and after material session-management, IAM, "
        "or conversational-context changes"
    ),
    "NIST AI RMF Mapping": "GOVERN / MAP / MANAGE",
    "ISO/IEC 42001 Mapping": (
        "Access control / session management / AI system operation"
    ),
        "Status": "Implemented and Tested"
},
{
    "Control ID": "AI-MODEL-001",
    "Control Name": "Model Risk and Behavioral Limitation Management",
    "Risk ID": "AI-RISK-010",
    "Risk Description": (
        "AI model limitations such as hallucination, unsupported factual "
        "claims, behavioral instability, or model drift may cause users "
        "to receive inaccurate or misleading information."
    ),
    "Control Objective": (
        "Reduce the risk that unsupported model-generated factual claims "
        "are delivered to users as if they were grounded in available "
        "system context."
    ),
    "Control Type": "Preventive / Detective / Governance / Technical",
    "Implementation": (
        "The application performs a grounding check before user delivery, "
        "allows claims supported by available context, blocks unsupported "
        "factual claims, permits appropriate uncertainty, and returns a "
        "controlled response when grounding validation fails."
    ),
    "Test Procedure": (
        "Test a supported balance statement, unsupported credit score, "
        "unsupported recent transaction, and appropriate uncertainty to "
        "verify grounding enforcement."
    ),
    "Evidence": (
        "insecure_model_risk_test.txt; "
        "secure_model_risk_test.txt; "
        "AI-MODEL-001_assessment.txt"
    ),
    "Test Result": "4 Passed / 0 Failed / 0 Errors",
    "Control Effectiveness": "Effective for tested scenarios",
    "Residual Risk": (
        "Authoritative source validation, claim-level verification, retrieval "
        "quality assessment, citation validation, drift monitoring, broader "
        "hallucination testing, multilingual evaluation, and documented model "
        "limitations remain incomplete."
    ),
    "Control Owner": "AI Application / AI Governance / Model Risk Team",
    "Review Frequency": (
        "Quarterly and after material model, retrieval, prompt, "
        "or grounding-control changes"
    ),
    "NIST AI RMF Mapping": "MAP / MEASURE / MANAGE",
    "ISO/IEC 42001 Mapping": (
        "Model evaluation / performance monitoring / AI system operation"
    ),
        "Status": "Implemented and Tested"
},
{
    "Control ID": "AI-SUPPLY-001",
    "Control Name": "AI Model and Software Supply-Chain Assurance",
    "Risk ID": "AI-RISK-011",
    "Risk Description": (
        "AI models, software artifacts, dependencies, or third-party "
        "components may be untrusted, tampered with, vulnerable, or "
        "insufficiently governed, introducing security and operational risk."
    ),
    "Control Objective": (
        "Ensure AI model and software artifacts are loaded only when their "
        "approval status, source provenance, and integrity have been validated."
    ),
    "Control Type": "Preventive / Governance / Technical",
    "Implementation": (
        "The application uses an approved-artifact registry, verifies the "
        "artifact source, calculates a SHA-256 hash, compares it with the "
        "approved expected hash, and blocks artifacts that fail approval, "
        "provenance, or integrity checks."
    ),
    "Test Procedure": (
        "Test an approved model from a trusted repository, an unapproved "
        "model from an unverified source, and a tampered approved model."
    ),
    "Evidence": (
        "insecure_supply_chain_test.txt; "
        "secure_supply_chain_test.txt; "
        "AI-SUPPLY-001_assessment.txt"
    ),
    "Test Result": "3 Passed / 0 Failed / 0 Errors",
    "Control Effectiveness": "Effective for tested scenarios",
    "Residual Risk": (
        "Digital-signature verification, authenticated repositories, "
        "dependency and vulnerability analysis, SBOM controls, supplier "
        "due diligence, license review, provenance documentation, and "
        "continuous upstream monitoring remain incomplete."
    ),
    "Control Owner": "AI Application / Security / Third-Party Risk Team",
    "Review Frequency": (
        "Quarterly and after material model, dependency, supplier, "
        "repository, or software-component changes"
    ),
    "NIST AI RMF Mapping": "GOVERN / MAP / MEASURE / MANAGE",
    "ISO/IEC 42001 Mapping": (
        "Third-party risk / supply-chain assurance / AI system operation"
    ),
        "Status": "Implemented and Tested"
},
{
    "Control ID": "AI-PRIV-001",
    "Control Name": "AI Privacy and Data Governance Enforcement",
    "Risk ID": "AI-RISK-012",
    "Risk Description": (
        "Personal, sensitive, or restricted data may be processed by the AI "
        "without adequate purpose limitation, minimization, classification, "
        "retention, deletion, or broader privacy-governance controls."
    ),
    "Control Objective": (
        "Ensure personal and sensitive data is processed by the AI only for "
        "an approved purpose and limited to the minimum data required for "
        "that purpose."
    ),
    "Control Type": "Preventive / Governance / Technical",
    "Implementation": (
        "The application defines approved processing purposes, maps each "
        "purpose to permitted fields, applies basic data classification, "
        "excludes unnecessary personal and restricted data, and rejects "
        "unapproved processing purposes before AI processing."
    ),
    "Test Procedure": (
        "Test a balance inquiry, account-type inquiry, and unapproved "
        "marketing purpose to verify purpose limitation and data minimization."
    ),
    "Evidence": (
        "insecure_privacy_governance_test.txt; "
        "secure_privacy_governance_test.txt; "
        "AI-PRIV-001_assessment.txt"
    ),
    "Test Result": "3 Passed / 0 Failed / 0 Errors",
    "Control Effectiveness": "Effective for tested scenarios",
    "Residual Risk": (
        "Formal data classification, lawful-processing review, retention and "
        "deletion controls, data lineage, data-subject rights handling, "
        "cross-border review, privacy impact assessment, records of processing, "
        "and ongoing privacy monitoring remain incomplete."
    ),
    "Control Owner": "Privacy / Data Governance / AI Governance Team",
    "Review Frequency": (
        "Quarterly and after material data, purpose, privacy, "
        "or AI-processing changes"
    ),
    "NIST AI RMF Mapping": "GOVERN / MAP / MANAGE",
    "ISO/IEC 42001 Mapping": (
        "Data governance / privacy / AI system operation"
    ),
    "Status": "Implemented and Tested"
}
]

filename = "evidence/AI_Control_Register.csv"
with open(filename, "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=controls[0].keys())
    writer.writeheader()
    writer.writerows(controls)

print(f"Control register created: {filename}")
print(f"Controls recorded: {len(controls)}")
