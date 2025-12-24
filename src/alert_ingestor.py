import json

def load_alerts(file_path):
    with open(file_path, "r") as f:
        return json.load(f)

