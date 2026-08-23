import csv


def calculate_risk_score(likelihood, impact):
    return likelihood * impact


def risk_rating(score):
    if score <= 4:
        return "Low"
    elif score <= 9:
        return "Medium"
    elif score <= 16:
        return "High"
    else:
        return "Critical"


risks = [
    {
        "Risk ID": "AI-RISK-001",
        "Risk Title": "Sensitive Data Disclosure Through LLM",
        "Risk Description": (
            "Sensitive authentication or payment information may be "
            "exposed, transformed, reconstructed, or disclosed through "
            "the AI system."
        ),
        "Risk Category": "Data Protection / AI Security",
        "Threat Scenario": (
            "A user attempts to obtain restricted PIN or payment data "
            "through direct requests, prompt injection, or transformation."
        ),
        "Affected Asset": "Customer data / AI application",
        "Inherent Likelihood": 4,
        "Inherent Impact": 5,
        "Inherent Score": 0,
        "Inherent Rating": "",
        "Mapped Control": "AI-DATA-001",
        "Control Status": "Implemented and Tested",
        "Residual Likelihood": 2,
        "Residual Impact": 5,
        "Residual Score": 0,
        "Residual Rating": "",
        "Risk Treatment": "Mitigate",
        "Risk Owner": "AI Application / Security Team",
        "Review Frequency": "Quarterly and after material changes",
        "Status": "Open - Controlled"
    },
    {
        "Risk ID": "AI-RISK-002",
        "Risk Title": "Unauthorized Cross-Customer Data Access",
        "Risk Description": (
            "An authenticated user may attempt to access another "
            "customer's information through the AI interface."
        ),
        "Risk Category": "Authorization / AI Security",
        "Threat Scenario": (
            "A user requests another customer's data directly or uses "
            "role manipulation or prompt injection to bypass restrictions."
        ),
        "Affected Asset": "Customer account information",
        "Inherent Likelihood": 4,
        "Inherent Impact": 5,
        "Inherent Score": 0,
        "Inherent Rating": "",
        "Mapped Control": "AI-ACCESS-001",
        "Control Status": "Implemented and Tested",
        "Residual Likelihood": 2,
        "Residual Impact": 5,
        "Residual Score": 0,
        "Residual Rating": "",
        "Risk Treatment": "Mitigate",
        "Risk Owner": "AI Application / IAM / Security Team",
        "Review Frequency": "Quarterly and after authorization changes",
        "Status": "Open - Controlled"
    },
    {
        "Risk ID": "AI-RISK-003",
        "Risk Title": "Insufficient AI Security Logging and Monitoring",
        "Risk Description": (
            "Security-relevant AI activity may not be detected, "
            "investigated, reconstructed, or escalated because of "
            "insufficient logging and monitoring."
        ),
        "Risk Category": "Monitoring / AI Security",
        "Threat Scenario": (
            "Unauthorized access attempts, prompt injection, role "
            "manipulation, or other malicious AI activity occurs but "
            "is not adequately logged, detected, or investigated."
        ),
        "Affected Asset": "AI application / security audit trail",
        "Inherent Likelihood": 4,
        "Inherent Impact": 4,
        "Inherent Score": 0,
        "Inherent Rating": "",
        "Mapped Control": "AI-LOG-001",
        "Control Status": "Implemented and Tested",
        "Residual Likelihood": 2,
        "Residual Impact": 4,
        "Residual Score": 0,
        "Residual Rating": "",
        "Risk Treatment": "Mitigate",
        "Risk Owner": "Security Operations / AI Governance Team",
        "Review Frequency": (
            "Quarterly and after material logging or monitoring changes"
        ),
        "Status": "Open - Controlled"
    },
        {
        "Risk ID": "AI-RISK-004",
        "Risk Title": "Unsafe or Sensitive AI Output Delivery",
        "Risk Description": (
            "AI-generated responses may contain restricted, sensitive, "
            "credential-like, malformed, or otherwise unsafe content that "
            "could be delivered directly to an end user."
        ),
        "Risk Category": "Output Security / AI Safety",
        "Threat Scenario": (
            "The model generates sensitive or unsafe content and the "
            "application delivers the response without adequate output "
            "validation or blocking."
        ),
        "Affected Asset": "Customer data / user-facing AI response",
        "Inherent Likelihood": 4,
        "Inherent Impact": 5,
        "Inherent Score": 0,
        "Inherent Rating": "",
        "Mapped Control": "AI-OUTPUT-001",
        "Control Status": "Implemented and Tested",
        "Residual Likelihood": 2,
        "Residual Impact": 5,
        "Residual Score": 0,
        "Residual Rating": "",
        "Risk Treatment": "Mitigate",
        "Risk Owner": "AI Application / Security Team",
        "Review Frequency": (
            "Quarterly and after material model, prompt, or output-policy changes"
        ),
            "Status": "Open - Controlled"
        },
        {
    "Risk ID": "AI-RISK-005",
    "Risk Title": "Authentication or Session Compromise Leading to Unauthorized AI Access",
    "Risk Description": (
        "Weak authentication or session handling may allow an attacker "
        "or unauthorized user to obtain AI access under another user's "
        "identity or through a forged or improperly validated session."
    ),
    "Risk Category": "Identity and Access / AI Security",
    "Threat Scenario": (
        "An attacker forges, alters, reuses, or misrepresents session "
        "information and the AI application accepts the session without "
        "adequate server-side validation and identity binding."
    ),
    "Affected Asset": "User identity / AI application / customer data",
    "Inherent Likelihood": 4,
    "Inherent Impact": 5,
    "Inherent Score": 0,
    "Inherent Rating": "",
    "Mapped Control": "AI-AUTH-001",
    "Control Status": "Implemented and Tested",
    "Residual Likelihood": 2,
    "Residual Impact": 5,
    "Residual Score": 0,
    "Residual Rating": "",
    "Risk Treatment": "Mitigate",
    "Risk Owner": "IAM / AI Application / Security Team",
    "Review Frequency": (
        "Quarterly and after material authentication or session changes"
    ),
        "Status": "Open - Controlled"
},
{
    "Risk ID": "AI-RISK-006",
    "Risk Title": "Uncontrolled AI Model or Configuration Change",
    "Risk Description": (
        "Unauthorized, unapproved, or poorly controlled changes to the AI "
        "model, system prompt, configuration, validation logic, or related "
        "security settings may weaken previously tested controls or alter "
        "system behavior."
    ),
    "Risk Category": "Change Management / AI Governance",
    "Threat Scenario": (
        "A model, prompt, configuration, or security-related setting is "
        "changed without adequate approval, validation, version control, "
        "testing, or rollback capability."
    ),
    "Affected Asset": "AI model / configuration / security controls",
    "Inherent Likelihood": 4,
    "Inherent Impact": 5,
    "Inherent Score": 0,
    "Inherent Rating": "",
    "Mapped Control": "AI-CHANGE-001",
    "Control Status": "Implemented and Tested",
    "Residual Likelihood": 2,
    "Residual Impact": 5,
    "Residual Score": 0,
    "Residual Rating": "",
    "Risk Treatment": "Mitigate",
    "Risk Owner": "AI Application / AI Governance / Security Team",
    "Review Frequency": (
        "Quarterly and after material model, prompt, configuration, "
        "or deployment changes"
    ),
        "Status": "Open - Controlled"
},
{
    "Risk ID": "AI-RISK-007",
    "Risk Title": "Insufficient Human Oversight of Material AI Decisions",
    "Risk Description": (
        "Material AI-driven actions may proceed without appropriate human "
        "review, approval, escalation, or accountability, increasing the "
        "risk of unauthorized or harmful outcomes."
    ),
    "Risk Category": "Human Oversight / AI Governance",
    "Threat Scenario": (
        "The AI application initiates or executes a material action such as "
        "an account closure, large transfer, or credential reset without "
        "required human review or approval."
    ),
    "Affected Asset": "Customer accounts / financial actions / user credentials",
    "Inherent Likelihood": 4,
    "Inherent Impact": 5,
    "Inherent Score": 0,
    "Inherent Rating": "",
    "Mapped Control": "AI-HUMAN-001",
    "Control Status": "Implemented and Tested",
    "Residual Likelihood": 2,
    "Residual Impact": 5,
    "Residual Score": 0,
    "Residual Rating": "",
    "Risk Treatment": "Mitigate",
    "Risk Owner": "AI Governance / Business Operations / Security Team",
    "Review Frequency": (
        "Quarterly and after material changes to AI decision authority "
        "or human-approval workflows"
    ),
        "Status": "Open - Controlled"
},
{
    "Risk ID": "AI-RISK-008",
    "Risk Title": "Inadequate Response to AI Security Incidents",
    "Risk Description": (
        "High-risk AI security events may not be contained, escalated, "
        "investigated, or supported by preserved evidence, increasing the "
        "impact and duration of security incidents."
    ),
    "Risk Category": "Incident Response / AI Security",
    "Threat Scenario": (
        "A high-risk AI security event such as prompt injection or "
        "cross-customer access occurs, but the organization fails to create "
        "an incident, contain the activity, escalate the event, or preserve "
        "evidence for investigation."
    ),
    "Affected Asset": (
        "AI application / customer data / security evidence / operations"
    ),
    "Inherent Likelihood": 4,
    "Inherent Impact": 5,
    "Inherent Score": 0,
    "Inherent Rating": "",
    "Mapped Control": "AI-IR-001",
    "Control Status": "Implemented and Tested",
    "Residual Likelihood": 2,
    "Residual Impact": 5,
    "Residual Score": 0,
    "Residual Rating": "",
    "Risk Treatment": "Mitigate",
    "Risk Owner": "Security Operations / Incident Response / AI Governance Team",
    "Review Frequency": (
        "Quarterly and after material incident-response process changes "
        "or significant AI security incidents"
    ),
        "Status": "Open - Controlled"
},
{
    "Risk ID": "AI-RISK-009",
    "Risk Title": "Cross-User Session or Context Leakage",
    "Risk Description": (
        "Session or conversational context may cross user boundaries, allowing "
        "one authenticated user to receive another user's context or reuse a "
        "session that is bound to a different identity."
    ),
    "Risk Category": "Session Security / AI Security",
    "Threat Scenario": (
        "A user reuses another user's session identifier, requests another "
        "user's context, or receives context left in shared application state "
        "because session and identity boundaries are not adequately isolated."
    ),
    "Affected Asset": (
        "User session / conversational context / customer information"
    ),
    "Inherent Likelihood": 4,
    "Inherent Impact": 5,
    "Inherent Score": 0,
    "Inherent Rating": "",
    "Mapped Control": "AI-SESSION-001",
    "Control Status": "Implemented and Tested",
    "Residual Likelihood": 2,
    "Residual Impact": 5,
    "Residual Score": 0,
    "Residual Rating": "",
    "Risk Treatment": "Mitigate",
    "Risk Owner": "AI Application / IAM / Security Team",
    "Review Frequency": (
        "Quarterly and after material session-management, IAM, "
        "or conversational-context changes"
    ),
        "Status": "Open - Controlled"
},
{
    "Risk ID": "AI-RISK-010",
    "Risk Title": "Unmanaged AI Model Limitations and Behavioral Risk",
    "Risk Description": (
        "AI model limitations such as hallucination, unsupported factual "
        "claims, behavioral instability, or model drift may cause users "
        "to receive inaccurate or misleading information."
    ),
    "Risk Category": "Model Risk / AI Reliability",
    "Threat Scenario": (
        "The AI model generates a factual statement that is not supported "
        "by available authoritative context, and the application presents "
        "that statement to the user as if it were reliable."
    ),
    "Affected Asset": (
        "User decisions / customer information / AI application reliability"
    ),
    "Inherent Likelihood": 4,
    "Inherent Impact": 5,
    "Inherent Score": 0,
    "Inherent Rating": "",
    "Mapped Control": "AI-MODEL-001",
    "Control Status": "Implemented and Tested",
    "Residual Likelihood": 2,
    "Residual Impact": 5,
    "Residual Score": 0,
    "Residual Rating": "",
    "Risk Treatment": "Mitigate",
    "Risk Owner": "AI Application / AI Governance / Model Risk Team",
    "Review Frequency": (
        "Quarterly and after material model, retrieval, prompt, "
        "or grounding-control changes"
    ),
        "Status": "Open - Controlled"
},
{
    "Risk ID": "AI-RISK-011",
    "Risk Title": "Unmanaged Third-Party AI and Software Supply-Chain Risk",
    "Risk Description": (
        "AI models, software artifacts, dependencies, or third-party "
        "components may be untrusted, tampered with, vulnerable, or "
        "insufficiently governed, introducing security and operational risk."
    ),
    "Risk Category": "Third-Party / Supply Chain / AI Security",
    "Threat Scenario": (
        "The AI application loads an unapproved, tampered, or improperly "
        "sourced model or software artifact because provenance, approval, "
        "and integrity controls are not adequately enforced."
    ),
    "Affected Asset": (
        "AI model / software dependencies / application integrity / customer data"
    ),
    "Inherent Likelihood": 4,
    "Inherent Impact": 5,
    "Inherent Score": 0,
    "Inherent Rating": "",
    "Mapped Control": "AI-SUPPLY-001",
    "Control Status": "Implemented and Tested",
    "Residual Likelihood": 2,
    "Residual Impact": 5,
    "Residual Score": 0,
    "Residual Rating": "",
    "Risk Treatment": "Mitigate",
    "Risk Owner": "AI Application / Security / Third-Party Risk Team",
    "Review Frequency": (
        "Quarterly and after material model, dependency, supplier, "
        "repository, or software-component changes"
    ),
        "Status": "Open - Controlled"
},
{
    "Risk ID": "AI-RISK-012",
    "Risk Title": "Inadequate Privacy and Data Governance for AI Processing",
    "Risk Description": (
        "Personal, sensitive, or restricted data may be processed by the AI "
        "without adequate purpose limitation, minimization, classification, "
        "retention, deletion, or broader privacy-governance controls."
    ),
    "Risk Category": "Privacy / Data Governance / AI Risk",
    "Threat Scenario": (
        "The AI application processes unnecessary personal or restricted data "
        "for an approved or unapproved purpose because privacy and data-governance "
        "requirements are not adequately enforced before AI processing."
    ),
    "Affected Asset": (
        "Personal data / restricted data / customer privacy / regulatory compliance"
    ),
    "Inherent Likelihood": 4,
    "Inherent Impact": 5,
    "Inherent Score": 0,
    "Inherent Rating": "",
    "Mapped Control": "AI-PRIV-001",
    "Control Status": "Implemented and Tested",
    "Residual Likelihood": 2,
    "Residual Impact": 5,
    "Residual Score": 0,
    "Residual Rating": "",
    "Risk Treatment": "Mitigate",
    "Risk Owner": "Privacy / Data Governance / AI Governance Team",
    "Review Frequency": (
        "Quarterly and after material data, purpose, privacy, "
        "or AI-processing changes"
    ),
    "Status": "Open - Controlled"
}
]



for risk in risks:
    inherent_score = calculate_risk_score(
        risk["Inherent Likelihood"],
        risk["Inherent Impact"]
    )

    residual_score = calculate_risk_score(
        risk["Residual Likelihood"],
        risk["Residual Impact"]
    )

    risk["Inherent Score"] = inherent_score
    risk["Inherent Rating"] = risk_rating(inherent_score)

    risk["Residual Score"] = residual_score
    risk["Residual Rating"] = risk_rating(residual_score)


filename = "evidence/AI_Risk_Register.csv"

with open(filename, "w", newline="") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=risks[0].keys()
    )
    writer.writeheader()
    writer.writerows(risks)


print(f"Risk register created: {filename}")
print(f"Risks recorded: {len(risks)}")

print("\nRISK SUMMARY")
print("=" * 65)

for risk in risks:
    print(
        f"{risk['Risk ID']}: "
        f"Inherent {risk['Inherent Score']}/25 "
        f"({risk['Inherent Rating']}) "
        f"-> Residual {risk['Residual Score']}/25 "
        f"({risk['Residual Rating']})"
    )
