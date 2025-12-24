from mitre_mapper import map_to_mitre

def generate_report(alert, action, result):
    mitre = map_to_mitre(alert["type"])

    report = (
        f"Incident ID: {alert['id']}\n"
        f"Type: {alert['type']}\n"
        f"Severity: {alert['severity']}\n"
        f"Source IP: {alert['source_ip']}\n"
        f"MITRE ATT&CK: {mitre}\n"
        f"Action Taken: {action}\n"
        f"Result: {result}\n"
        "----------------------------------\n"
    )

    print(report)

    with open("reports/incident_report.txt", "a") as f:
        f.write(report)

