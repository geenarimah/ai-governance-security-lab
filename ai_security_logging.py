import json
import uuid
from datetime import datetime

SYSTEM_ID = "AI-SYS-001"
LOG_FILE = "evidence/AI_Security_Events.jsonl"

# Simulated activity from the banking assistant.
events = [
    {
        "user_id": "alice",
        "event_type": "ACCOUNT_QUERY",
        "action": "Own account balance request",
        "authorization_result": "ALLOWED",
        "security_result": "NORMAL",
        "risk_level": "LOW"
    },
    {
        "user_id": "alice",
        "event_type": "CROSS_CUSTOMER_REQUEST",
        "action": "Attempted access to another customer's account",
        "authorization_result": "DENIED",
        "security_result": "BLOCKED",
        "risk_level": "HIGH"
    },
    {
        "user_id": "alice",
        "event_type": "ROLE_MANIPULATION",
        "action": "User claimed administrator privileges",
        "authorization_result": "DENIED",
        "security_result": "BLOCKED",
        "risk_level": "HIGH"
    },
    {
        "user_id": "alice",
        "event_type": "PROMPT_INJECTION",
        "action": "Attempted to override access-control restrictions",
        "authorization_result": "DENIED",
        "security_result": "BLOCKED",
        "risk_level": "HIGH"
    }
]


def build_event(event):
    return {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "event_id": str(uuid.uuid4()),
        "system_id": SYSTEM_ID,
        "user_id": event["user_id"],
        "event_type": event["event_type"],
        "action": event["action"],
        "authorization_result": event["authorization_result"],
        "security_result": event["security_result"],
        "risk_level": event["risk_level"]
    }


with open(LOG_FILE, "a") as file:
    for event in events:
        log_event = build_event(event)
        file.write(json.dumps(log_event) + "\n")

        print("LOGGED EVENT")
        print(json.dumps(log_event, indent=4))
        print()


print("==========================================")
print(" AI SECURITY LOGGING COMPLETE")
print("==========================================")
print(f"Events written: {len(events)}")
print(f"Log file: {LOG_FILE}")
print("==========================================")
