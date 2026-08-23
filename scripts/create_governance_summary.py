summary = """
============================================================
AI GOVERNANCE LAB - FINAL GOVERNANCE SUMMARY
============================================================

SYSTEM ID:
AI-SYS-001

SYSTEM NAME:
Internal Banking AI Assistant

MODEL:
Qwen/Qwen2.5-1.5B-Instruct-GGUF

DEPLOYMENT:
Local llama.cpp inference server

LIFECYCLE STATUS:
Development / Testing

PRODUCTION APPROVED:
No

============================================================
PROJECT OBJECTIVE
============================================================

This lab demonstrates how AI governance requirements can be
translated into technical controls, adversarial testing,
evidence collection, risk assessment, and system-level
governance decisions.

The project was designed around a simulated internal banking
AI assistant handling authenticated customer-account queries.

The governance approach follows the chain:

AI system
-> identified risk
-> implemented control
-> insecure baseline
-> secure test
-> retained evidence
-> control assessment
-> residual risk
-> production decision

============================================================
CONTROL AND RISK COVERAGE
============================================================

1. AI-DATA-001
   Risk: AI-RISK-001
   Control: Sensitive Data Minimization Before LLM Processing

2. AI-ACCESS-001
   Risk: AI-RISK-002
   Control: User-Level Authorization Before LLM Processing

3. AI-LOG-001
   Risk: AI-RISK-003
   Control: AI Security Logging and Monitoring

4. AI-OUTPUT-001
   Risk: AI-RISK-004
   Control: AI Output Validation Before User Delivery

5. AI-AUTH-001
   Risk: AI-RISK-005
   Control: Authentication and Session Assurance Before AI Access

6. AI-CHANGE-001
   Risk: AI-RISK-006
   Control: AI Model and Configuration Change Management

7. AI-HUMAN-001
   Risk: AI-RISK-007
   Control: Human Oversight and Escalation for Material AI Decisions

8. AI-IR-001
   Risk: AI-RISK-008
   Control: AI-Specific Incident Response and Evidence Preservation

9. AI-SESSION-001
   Risk: AI-RISK-009
   Control: Multi-User Session and Context Isolation

10. AI-MODEL-001
    Risk: AI-RISK-010
    Control: Model Risk and Behavioral Limitation Management

11. AI-SUPPLY-001
    Risk: AI-RISK-011
    Control: AI Model and Software Supply-Chain Assurance

12. AI-PRIV-001
    Risk: AI-RISK-012
    Control: AI Privacy and Data Governance Enforcement

============================================================
TESTING APPROACH
============================================================

The lab intentionally implemented insecure versions first
where appropriate.

These baselines demonstrated failures such as:

- prompt-only protection leaking sensitive values
- unauthorized cross-customer access
- missing security-event handling
- unsafe or unsupported output delivery
- forged or identity-mismatched sessions
- uncontrolled model/configuration changes
- material actions without human approval
- security incidents without response handling
- cross-user session/context crossover
- unsupported factual claims
- unapproved or tampered model artifacts
- unnecessary personal-data processing

Secure implementations were then tested against defined
adversarial and normal scenarios.

All twelve implemented controls passed their defined secure
test scenarios.

============================================================
RISK MANAGEMENT
============================================================

Risk scoring uses a documented 5x5 likelihood and impact
methodology.

Risk ratings:

1-4   LOW
5-9   MEDIUM
10-16 HIGH
17-25 CRITICAL

Inherent risk represents exposure before control treatment.

Residual risk represents remaining exposure after implemented
controls and supporting evidence.

Most identified risks remain HIGH after treatment because the
lab demonstrates control effectiveness for tested scenarios
but does not claim complete production maturity.

============================================================
KEY GOVERNANCE PRINCIPLES DEMONSTRATED
============================================================

1. Prompt instructions are not authorization controls.

2. Sensitive data should be excluded before model processing
   whenever it is not required.

3. Authorization must be enforced outside the LLM.

4. Output controls and model-grounding controls address
   different risks.

5. Logging is not the same as monitoring or incident response.

6. Passing test cases does not prove production security.

7. Human oversight must be tied to material decision authority.

8. Model and configuration changes require governance controls.

9. AI model provenance and artifact integrity matter.

10. Privacy requires purpose limitation in addition to general
    data minimization.

11. Risk scores must be supported by a defined methodology.

12. Governance decisions must be based on evidence,
    limitations, and residual risk.

============================================================
EVIDENCE PRODUCED
============================================================

Primary governance artifacts include:

- AI_System_Inventory.csv
- AI_Risk_Register.csv
- AI_Control_Register.csv
- AI_Risk_Scoring_Methodology.txt
- AI-SYS-001_Use_Case_Risk_Assessment.txt

Individual control assessments and insecure/secure test
evidence are retained in the evidence directory.

============================================================
SYSTEM-LEVEL DECISION
============================================================

AI-SYS-001 is NOT APPROVED FOR PRODUCTION.

The system demonstrates a sound initial governance and
technical-control architecture across twelve identified
risk areas.

However, the assessments identify remaining production
requirements including:

- production authentication and session lifecycle
- centralized monitoring and SIEM integration
- formal change-management lifecycle
- production human-review workflows
- complete incident-response lifecycle
- production session isolation and IAM integration
- full model-risk management
- formal third-party risk management
- mature privacy and data-governance lifecycle
- broader operational resilience and assurance controls

Residual risk has therefore not been formally accepted for
production use.

============================================================
PORTFOLIO / INTERVIEW POSITIONING
============================================================

This project demonstrates practical capability in:

- AI governance
- AI risk assessment
- control design
- adversarial testing
- evidence-based control assessment
- residual-risk analysis
- AI security architecture
- model-risk management
- privacy and data governance
- third-party and supply-chain assurance
- incident response
- human oversight
- change management
- governance reporting

It also demonstrates the ability to connect technical AI
behavior with governance frameworks and production-readiness
decisions rather than treating AI governance as documentation
alone.

============================================================
"""

filename = "evidence/AI_Governance_Lab_Final_Summary.txt"

with open(filename, "w") as file:
    file.write(summary)

print(summary)
print(f"Summary saved to: {filename}")
