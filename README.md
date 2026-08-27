# AI Governance and Security Lab

## What This Demonstrates

This project demonstrates practical AI governance and AI security assurance across the full control lifecycle:

- AI system inventory and use-case risk assessment
- 5×5 inherent and residual risk scoring
- preventive, detective, and governance control design
- adversarial testing of AI security controls
- evidence-based control effectiveness assessment
- model, access, privacy, logging, output, session, supply-chain, and human-oversight controls
- automated regression testing across 12 controls
- baseline evidence comparison and control regression detection
- production assurance gating
- risk reassessment after control failure
- remediation verification and recovery

The emphasis is not on making an LLM appear safe through prompting alone. Controls are enforced at the application and governance layers, tested adversarially, and tied back
to risks, evidence, and production decisions.

## Assurance Architecture

```text
AI System / Use Case
        ↓
Risk Identification
        ↓
Control Design
        ↓
Technical Implementation
        ↓
Adversarial Testing
        ↓
Evidence Collection
        ↓
Control Effectiveness Assessment
        ↓
Residual Risk
        ↓
Production Decision
        ↓
Continuous Assurance
        ↓
Regression Detection
        ↓
Control Failure Response
        ↓
Risk Reassessment
        ↓
Remediation Verification
```

The lab therefore treats AI governance as an ongoing assurance process rather than a one-time documentation exercise.
> **Synthetic Data Notice**
>
> All customer names, credentials, PINs, card numbers, identifiers,
> account balances, addresses, authentication data, and security events
> used in this repository are fictional test data created solely for
> controlled security and governance testing. No real customer,
> production, banking, or credential data is used.

This project demonstrates how AI governance requirements can be translated into technical controls, adversarial testing, evidence collection, risk assessment, and
production-readiness decisions.

The lab uses a simulated internal banking AI assistant running locally with:

- Qwen2.5-1.5B-Instruct-GGUF
- llama.cpp
- Python
- structured governance evidence
- adversarial and negative testing

The objective is not to prove production readiness.

The objective is to demonstrate a practical governance process:

AI system → risk → control → insecure baseline → secure implementation → test evidence → control assessment → residual risk → production decision

---

## AI System

**System ID:** AI-SYS-001
**System Name:** Internal Banking AI Assistant
**Lifecycle:** Development / Testing
**Production Approved:** No

The simulated assistant provides authenticated users with conversational access to authorized customer account information.

The system has no autonomous transaction authority.

---

## Governance Coverage

The lab currently includes 12 identified risks and 12 implemented and tested controls.

| Risk | Control | Area |
|---|---|---|
| AI-RISK-001 | AI-DATA-001 | Sensitive Data Minimization |
| AI-RISK-002 | AI-ACCESS-001 | User-Level Authorization |
| AI-RISK-003 | AI-LOG-001 | Security Logging |
| AI-RISK-004 | AI-OUTPUT-001 | Output Validation |
| AI-RISK-005 | AI-AUTH-001 | Authentication and Session Assurance |
| AI-RISK-006 | AI-CHANGE-001 | Model and Configuration Change Management |
| AI-RISK-007 | AI-HUMAN-001 | Human Oversight |
| AI-RISK-008 | AI-IR-001 | AI Incident Response |
| AI-RISK-009 | AI-SESSION-001 | Multi-User Session Isolation |
| AI-RISK-010 | AI-MODEL-001 | Model Risk and Grounding |
| AI-RISK-011 | AI-SUPPLY-001 | AI Supply-Chain Assurance |
| AI-RISK-012 | AI-PRIV-001 | Privacy and Data Governance |

---

## Control Design Approach

### 1. Sensitive Data Minimization

Sensitive authentication and payment information is removed before LLM processing.

This demonstrates the principle that sensitive information should not be placed into model context when it is not required.

### 2. Authorization

Authorization is enforced at the application layer rather than through prompt instructions.

The model receives only information the authenticated user is authorized to access.

### 3. Security Logging

Structured security events are generated for normal and high-risk AI activity.

Events include identifiers, timestamps, authorization outcomes, security results, and risk levels.

### 4. Output Validation

Model responses are checked before user delivery for restricted or unsafe values.

### 5. Authentication and Session Assurance

AI access requires a validated session that is bound to the authenticated identity.

### 6. Change Management

Material model, prompt, configuration, and security-control changes require approval and validation before application.

### 7. Human Oversight

Defined material AI-driven actions require explicit human approval before execution.

### 8. Incident Response

High-risk AI security events trigger defined incident creation, containment, escalation, and evidence-preservation actions.

### 9. Session and Context Isolation

User sessions maintain isolated context and prevent cross-user session reuse or context crossover.

### 10. Model Risk Management

Unsupported factual claims are blocked while supported information and appropriate uncertainty are permitted.

### 11. Supply-Chain Assurance

Model and software artifacts are checked for approval, source provenance, and integrity before loading.

### 12. Privacy and Data Governance

AI processing is restricted to approved purposes and the minimum data required for those purposes.

---

## Testing Strategy

The lab intentionally uses insecure implementations where appropriate to establish a baseline.

Examples of demonstrated failures include:

- sensitive-value leakage despite prompt instructions
- cross-customer data access
- missing security-event response
- unsafe output delivery
- forged sessions
- unauthorized configuration changes
- material actions without human approval
- missing incident-response handling
- cross-user session leakage
- unsupported factual claims
- unverified or tampered model artifacts
- unnecessary personal-data processing

Secure implementations are then tested against defined normal and adversarial scenarios.

Passing a test means the control operated as expected for the tested scenario.

It does not mean the control or system is production secure.

---

## Risk Methodology

The project uses a 5 × 5 likelihood and impact methodology.

### Likelihood

1. Rare
2. Unlikely
3. Possible
4. Likely
5. Almost Certain

### Impact

1. Insignificant
2. Minor
3. Moderate
4. Major
5. Severe

### Ratings

- 1–4: Low
- 5–9: Medium
- 10–16: High
- 17–25: Critical

Inherent risk represents exposure before control treatment.

Residual risk represents remaining exposure after implemented controls and available evidence.

---

## Evidence Structure

Key governance artifacts are stored in the `evidence/` directory.

Examples include:

```text
AI_System_Inventory.csv
AI_Risk_Register.csv
AI_Control_Register.csv
AI_Risk_Scoring_Methodology.txt
AI-SYS-001_Use_Case_Risk_Assessment.txt
AI_Governance_Lab_Final_Summary.txt
---

## Continuous Assurance and Production Gating

The lab includes a continuous-assurance workflow that evaluates whether changes introduce control regressions before an AI system can pass an assurance gate.

### Assurance Workflow

```text
Change / version state
        ↓
Automated control retest
        ↓
Evidence generation
        ↓
Baseline comparison
        ↓
Regression detection
        ↓
Defined control failure response
        ↓
Production gate decision
        ↓
Risk reassessment
        ↓
Remediation verification
```

The current assurance suite automatically retests 12 implemented controls across:

- sensitive-data minimization
- authorization
- security logging
- output validation
- authentication and session assurance
- change management
- human oversight
- incident response
- session isolation
- model risk
- software and model supply-chain assurance
- privacy and data governance

### Controlled Regression Exercise

A controlled regression was introduced into `AI-OUTPUT-001` by temporarily weakening the restricted-output validation logic.

Baseline state:

- 12 controls passed
- 0 controls failed
- assurance suite: PASS

After the controlled change:

- `AI-OUTPUT-001`: PASS → FAIL
- 11 controls passed
- 1 control failed
- evidence comparison detected the regression
- production assurance gate was automatically BLOCKED

The control failure was mapped to `AI-RISK-004 — Unsafe or Sensitive AI Output Delivery`.

Risk reassessment increased:

- residual likelihood: 2 → 3
- residual score: 10 → 15
- risk status: `ESCALATED_PENDING_REMEDIATION`

The secure output-validation control was then restored and retested.

Recovery state:

- 12 controls passed
- 0 controls failed
- 0 control errors
- 0 regressions detected
- assurance gate: PASS
- remediation status: `REMEDIATION_VERIFIED`

Passing the assurance gate does not constitute production authorization. The system remains `NOT_APPROVED_FOR_PRODUCTION` because broader production-readiness requirements and 
formal risk acceptance remain outside the scope of this lab.

### Continuous Assurance Command

The full assurance workflow can be executed with:

```bash
python3 assurance/continuous_assurance.py
