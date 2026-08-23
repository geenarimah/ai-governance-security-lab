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
        "Inherent Score": 20,"Inherent Rating": "",
        "Mapped Control": "AI-DATA-001",
        "Control Status": "Implemented and Tested",
        "Residual Likelihood": 2,
        "Residual Impact": 5,
        "Residual Score": 10,
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
        "Inherent Score": 20,"Inherent Rating": "",
        "Mapped Control": "AI-ACCESS-001",
        "Control Status": "Implemented and Tested",
        "Residual Likelihood": 2,
        "Residual Impact": 5,
        "Residual Score": 10,
        "Residual Rating": "",
        "Risk Treatment": "Mitigate",
        "Risk Owner": "AI Application / IAM / Security Team",
        "Review Frequency": "Quarterly and after authorization changes",
        "Status": "Open - Controlled"
    }
]
# Calculate risk scores and ratings consistently
# using the approved AI risk scoring methodology.

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
    writer = csv.DictWriter(file, fieldnames=risks[0].keys())
    writer.writeheader()
    writer.writerows(risks)

print(f"Risk register created: {filename}")
print(f"Risks recorded: {len(risks)}")

print("\nRISK SUMMARY")
print("=" * 55)

for risk in risks:
    print(
        f"{risk['Risk ID']}: "
        f"Inherent {risk['Inherent Score']}/25 "
        f"-> Residual {risk['Residual Score']}/25 "
        f"({risk['Residual Rating']})"
    )
