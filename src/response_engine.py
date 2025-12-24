def execute_response(action, alert):
    if action == "BLOCK_IP":
        return f"Firewall rule added to block IP {alert['source_ip']}"

    if action == "ISOLATE_HOST":
        return f"Host communicating with {alert['source_ip']} isolated from network"

    return "No automated action taken"

