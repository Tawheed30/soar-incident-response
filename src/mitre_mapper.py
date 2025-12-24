def map_to_mitre(alert_type):
    mapping = {
        "Brute Force": "T1110 – Brute Force",
        "Malware Activity": "T1059 – Command and Scripting Interpreter"
    }
    return mapping.get(alert_type, "Unknown Technique")

