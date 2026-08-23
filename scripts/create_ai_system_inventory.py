import csv
from datetime import datetime

systems = [
    {
        "System ID": "AI-SYS-001",
        "System Name": "Internal Banking AI Assistant",
        "Business Purpose": (
            "Provide authenticated banking users with conversational "
            "access to authorized customer account information."
        ),
        "System Owner": "AI Application Team",
        "Risk Owner": "Security / AI Governance Team",
        "Model": "Qwen/Qwen2.5-1.5B-Instruct-GGUF",
        "Model Type": "Large Language Model",
        "Deployment": "Local llama.cpp inference server",
        "Interface": "Internal conversational banking assistant",
        "Intended Users": "Authenticated banking customers",
        "Data Processed": (
            "Customer name, account type, account balance, "
            "and authorized account context"
        ),
        "Restricted Data": (
            "PIN, full card number, credentials, and unauthorized "
            "customer records"
        ),
        "Decision Authority": (
            "Informational assistance only; no autonomous financial "
            "transaction authority"
        ),
        "Human Oversight": (
            "Security and AI governance teams review controls, "
            "testing, evidence, and material system changes"
        ),
            "Key Risks": (
        "AI-RISK-001; AI-RISK-002; AI-RISK-003; AI-RISK-004; "
        "AI-RISK-005; AI-RISK-006; AI-RISK-007; AI-RISK-008; "
        "AI-RISK-009; AI-RISK-010; AI-RISK-011; AI-RISK-012"
    ),

    "Implemented Controls": (
        "AI-DATA-001; AI-ACCESS-001; AI-LOG-001; AI-OUTPUT-001; "
        "AI-AUTH-001; AI-CHANGE-001; AI-HUMAN-001; AI-IR-001; "
        "AI-SESSION-001; AI-MODEL-001; AI-SUPPLY-001; AI-PRIV-001"
    ),
        "Risk Classification": "High",
        "Lifecycle Status": "Development / Testing",
        "Production Approved": "No",
        "Review Frequency": "Quarterly and after material changes",
        "Last Reviewed": datetime.now().strftime("%Y-%m-%d")
    }
]

filename = "evidence/AI_System_Inventory.csv"

with open(filename, "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=systems[0].keys())
    writer.writeheader()
    writer.writerows(systems)

print(f"AI system inventory created: {filename}")
print(f"Systems recorded: {len(systems)}")

print("\nAI SYSTEM SUMMARY")
print("=" * 60)

for system in systems:
    print(f"System ID:          {system['System ID']}")
    print(f"System Name:        {system['System Name']}")
    print(f"Model:              {system['Model']}")
    print(f"Risk Classification:{system['Risk Classification']}")
    print(f"Lifecycle Status:   {system['Lifecycle Status']}")
    print(f"Production Approved:{system['Production Approved']}")
    print(f"Controls:           {system['Implemented Controls']}")
