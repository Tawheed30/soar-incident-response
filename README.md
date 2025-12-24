# Automated SOAR Incident Response System

## Overview
A Python-based Security Orchestration, Automation, and Response (SOAR) system that ingests security alerts, maps them to MITRE ATT&CK techniques, executes automated response playbooks, and generates SOC-style incident reports.

## Features
- Alert ingestion (JSON-based)
- Automated response decision engine
- Incident response actions (IP blocking, host isolation)
- MITRE ATT&CK technique mapping
- Incident reporting

## Architecture
Alert → Decision Engine → Response Engine → Reporting

## Run
```bash
python3 src/main.py

