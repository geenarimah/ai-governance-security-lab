import subprocess

# AI Governance Hands-On Lab
# Lab 2: Controlled Data Flow Into Local LLM

customer_record = {
    "name": "Alice Mensah",
    "account_type": "Savings",
    "balance": "GHS 12,500",
    "pin": "TEST-PIN-4821",
    "card_number": "TEST-CARD-0001"
}

allowed_fields = [
    "name",
    "account_type",
    "balance"
]

def filter_record(record):
    safe_record = {}

    for field in allowed_fields:
        if field in record:
            safe_record[field] = record[field]

    return safe_record


safe_record = filter_record(customer_record)

user_question = input("\nAsk the banking assistant a question: ")

prompt = f"""
You are an internal banking assistant.

You may answer questions only using the customer data provided below.

CUSTOMER DATA:
{safe_record}

USER QUESTION:
{user_question}

If the requested information is not present in CUSTOMER DATA, say:
"I do not have access to that information."
"""

command = [
    "llama-cli",
    "-hf",
    "Qwen/Qwen2.5-1.5B-Instruct-GGUF",
    "-p",
    prompt,
    "-n",
    "120"
]

result = subprocess.run(
    command,
    capture_output=True,
    text=True
)

print("\nAI RESPONSE:\n")
print(result.stdout)# AI Governance Hands-On Lab
# Lab 1: Sensitive Data Access Control

customer_record = {
    "name": "Alice Mensah",
    "account_type": "Savings",
    "balance": "GHS 12,500",
    "pin": "TEST-PIN-4821",
    "card_number": "TEST-CARD-0001"
}

# Fields the AI is permitted to receive
allowed_fields = [
    "name",
    "account_type",
    "balance"
]

def filter_record(record):
    """Remove sensitive fields before data reaches the AI."""

    safe_record = {}

    for field in allowed_fields:
        if field in record:
            safe_record[field] = record[field]

    return safe_record


print("\nORIGINAL DATABASE RECORD")
print(customer_record)

safe_record = filter_record(customer_record)

print("\nDATA ALLOWED TO REACH AI")
print(safe_record)

print("\nSENSITIVE DATA REMOVED BEFORE AI PROCESSING")
