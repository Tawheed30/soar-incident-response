from alert_ingestor import load_alerts
from decision_engine import decide_response
from response_engine import execute_response
from reporter import generate_report

ALERT_FILE = "alerts/alerts.json"
RULE_FILE = "config/response_rules.json"

REQUIRED_ALERT_FIELDS = ("id", "type", "source_ip", "severity")

def main():
    alerts = load_alerts(ALERT_FILE)

    if not isinstance(alerts, list):
        print(f"Error: {ALERT_FILE} must contain a JSON array of alerts, got {type(alerts).__name__}. Aborting.")
        return

    for alert in alerts:
        if not isinstance(alert, dict) or any(field not in alert for field in REQUIRED_ALERT_FIELDS):
            print(f"Skipping malformed alert (expected fields {REQUIRED_ALERT_FIELDS}): {alert}")
            continue

        action = decide_response(alert, RULE_FILE)
        result = execute_response(action, alert)
        generate_report(alert, action, result)

if __name__ == "__main__":
    main()

