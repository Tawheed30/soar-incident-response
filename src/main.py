from alert_ingestor import load_alerts
from decision_engine import decide_response
from response_engine import execute_response
from reporter import generate_report

ALERT_FILE = "alerts/alerts.json"
RULE_FILE = "config/response_rules.json"

def main():
    alerts = load_alerts(ALERT_FILE)

    for alert in alerts:
        action = decide_response(alert, RULE_FILE)
        result = execute_response(action, alert)
        generate_report(alert, action, result)

if __name__ == "__main__":
    main()

