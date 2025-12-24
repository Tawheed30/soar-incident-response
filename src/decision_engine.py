import json

def decide_response(alert, rules_file):
    with open(rules_file, "r") as f:
        rules = json.load(f)

    return rules.get(alert["type"], "NO_ACTION")

