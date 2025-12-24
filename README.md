Last login: Wed Dec 24 02:00:30 on ttys003
mohammedtawheed@Mohammeds-MacBook-Pro-2 mitre-soc-simulator % soar-incident-response/
│
├── alerts/
│   └── alerts.json
│
├── src/
│   ├── alert_ingestor.py
│   ├── decision_engine.py
│   ├── response_engine.py
│   ├── reporter.py
│   └── main.py
│
├── reports/
│   └── incident_report.txt
│
├── config/
│   └── response_rules.json
│
├── README.md
├── requirements.txt
└── .gitignore

zsh: no such file or directory: soar-incident-response/
zsh: command not found: │
zsh: command not found: ├──
zsh: command not found: │
zsh: command not found: │
zsh: command not found: ├──
zsh: command not found: │
zsh: command not found: │
zsh: command not found: │
zsh: command not found: │
zsh: command not found: │
zsh: command not found: │
zsh: command not found: ├──
zsh: command not found: │
zsh: command not found: │
zsh: command not found: ├──
zsh: command not found: │
zsh: command not found: │
zsh: command not found: ├──
zsh: command not found: ├──
zsh: command not found: └──
mohammedtawheed@Mohammeds-MacBook-Pro-2 mitre-soc-simulator % cd
mohammedtawheed@Mohammeds-MacBook-Pro-2 ~ % ls
Applications			detector.py			lbtds.txt			mitre_mapping.json		network-ids.py			parse_logs.txt			readme.md
auth.log			detector.py.save		Library				mitre-soc-simulator		OneDrive			Pictures			soc-log-threat-detection
authlog.py			Documents			log_parser.py			Movies				pandas.txt			proj 4 				Terminal Saved Output.txt
Desktop				Downloads			logger.py			Music				parse_log.txt			Public
mohammedtawheed@Mohammeds-MacBook-Pro-2 ~ % cd mohammedtawheed
cd: no such file or directory: mohammedtawheed
mohammedtawheed@Mohammeds-MacBook-Pro-2 ~ % cd documents
mohammedtawheed@Mohammeds-MacBook-Pro-2 documents % ls
Documents - MOHAMMED’s MacBook Pro	soar
mohammedtawheed@Mohammeds-MacBook-Pro-2 documents % cd soar
mohammedtawheed@Mohammeds-MacBook-Pro-2 soar % mkdir soar-incident-response
cd soar-incident-response

mohammedtawheed@Mohammeds-MacBook-Pro-2 soar-incident-response % mkdir alerts src reports config

mohammedtawheed@Mohammeds-MacBook-Pro-2 soar-incident-response % touch alerts/alerts.json
touch config/response_rules.json
touch reports/incident_report.txt

touch src/alert_ingestor.py
touch src/decision_engine.py
touch src/response_engine.py
touch src/reporter.py
touch src/main.py

touch README.md
touch requirements.txt
touch .gitignore

mohammedtawheed@Mohammeds-MacBook-Pro-2 soar-incident-response % nano alerts/alerts.json

mohammedtawheed@Mohammeds-MacBook-Pro-2 soar-incident-response % nano config/response_rules.json

mohammedtawheed@Mohammeds-MacBook-Pro-2 soar-incident-response % nano src/alert_ingestor.py

mohammedtawheed@Mohammeds-MacBook-Pro-2 soar-incident-response % nano src/decision_engine.py

mohammedtawheed@Mohammeds-MacBook-Pro-2 soar-incident-response % nano src/response_engine.py

mohammedtawheed@Mohammeds-MacBook-Pro-2 soar-incident-response % nano src/reporter.py

mohammedtawheed@Mohammeds-MacBook-Pro-2 soar-incident-response % nano src/main.py

mohammedtawheed@Mohammeds-MacBook-Pro-2 soar-incident-response % python3 src/main.py

Traceback (most recent call last):
  File "/Users/mohammedtawheed/Documents/soar/soar-incident-response/src/main.py", line 18, in <module>
    main()
  File "/Users/mohammedtawheed/Documents/soar/soar-incident-response/src/main.py", line 10, in main
    alerts = load_alerts(ALERT_FILE)
  File "/Users/mohammedtawheed/Documents/soar/soar-incident-response/src/alert_ingestor.py", line 5, in load_alerts
    return json.load(f)
  File "/Applications/Xcode.app/Contents/Developer/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/json/__init__.py", line 293, in load
    return loads(fp.read(),
  File "/Applications/Xcode.app/Contents/Developer/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/json/__init__.py", line 346, in loads
    return _default_decoder.decode(s)
  File "/Applications/Xcode.app/Contents/Developer/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/json/decoder.py", line 337, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
  File "/Applications/Xcode.app/Contents/Developer/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/json/decoder.py", line 355, in raw_decode
    raise JSONDecodeError("Expecting value", s, err.value) from None
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
mohammedtawheed@Mohammeds-MacBook-Pro-2 soar-incident-response % nano alerts/alerts.json

mohammedtawheed@Mohammeds-MacBook-Pro-2 soar-incident-response % cat alerts/alerts.json

[
  {
    "id": "A-1001",
    "type": "Brute Force",
    "source_ip": "45.77.22.11",
    "severity": "HIGH"
  },
  {
    "id": "A-1002",
    "type": "Malware Activity",
    "source_ip": "91.202.44.88",
    "severity": "CRITICAL"
  }
]

mohammedtawheed@Mohammeds-MacBook-Pro-2 soar-incident-response % python3 src/main.py

Incident ID: A-1001
Type: Brute Force
Severity: HIGH
Source IP: 45.77.22.11
Action Taken: BLOCK_IP
Result: Firewall rule added to block IP 45.77.22.11
----------------------------------

Incident ID: A-1002
Type: Malware Activity
Severity: CRITICAL
Source IP: 91.202.44.88
Action Taken: ISOLATE_HOST
Result: Host communicating with 91.202.44.88 isolated from network
----------------------------------

mohammedtawheed@Mohammeds-MacBook-Pro-2 soar-incident-response % nano src/mitre_mapper.py

mohammedtawheed@Mohammeds-MacBook-Pro-2 soar-incident-response % nano src/reporter.py

mohammedtawheed@Mohammeds-MacBook-Pro-2 soar-incident-response % python3 src/main.py

Incident ID: A-1001
Type: Brute Force
Severity: HIGH
Source IP: 45.77.22.11
MITRE ATT&CK: T1110 – Brute Force
Action Taken: BLOCK_IP
Result: Firewall rule added to block IP 45.77.22.11
----------------------------------

Incident ID: A-1002
Type: Malware Activity
Severity: CRITICAL
Source IP: 91.202.44.88
MITRE ATT&CK: T1059 – Command and Scripting Interpreter
Action Taken: ISOLATE_HOST
Result: Host communicating with 91.202.44.88 isolated from network
----------------------------------

mohammedtawheed@Mohammeds-MacBook-Pro-2 soar-incident-response % nano README.md

mohammedtawheed@Mohammeds-MacBook-Pro-2 soar-incident-response % nano usecase
mohammedtawheed@Mohammeds-MacBook-Pro-2 soar-incident-response % git init
git add .
git commit -m "Initial commit: Automated SOAR incident response system"

Initialized empty Git repository in /Users/mohammedtawheed/Documents/soar/soar-incident-response/.git/
[main (root-commit) e72b3a9] Initial commit: Automated SOAR incident response system
 23 files changed, 1726 insertions(+)
 create mode 100644 .DS_Store
 create mode 100644 .gitignore
 create mode 100644 README.md
 create mode 100644 alerts.json
 create mode 100644 alerts/alerts.json
 create mode 100644 alerts/alerts.jsony
 create mode 100644 alerts:alerts.json
 create mode 100644 config/response_rules.json
 create mode 100644 reports/incident_report.txt
 create mode 100644 requirements.txt
 create mode 100644 response_rules.json
 create mode 100644 src/alert_ingestor.py
 create mode 100644 src/decision_engine.py
 create mode 100644 src/main.py
 create mode 100644 src/mitre_mapper.py
 create mode 100644 src/reporter.py
 create mode 100644 src/response_engine.py
 create mode 100644 src:alert_ingestor.py
 create mode 100644 src:decision_engine.py
 create mode 100644 src:main.py
 create mode 100644 src:mitre_mapper.py
 create mode 100644 src:reporter.py
 create mode 100644 src:response_engine.py
mohammedtawheed@Mohammeds-MacBook-Pro-2 soar-incident-response % nano .gitignore

mohammedtawheed@Mohammeds-MacBook-Pro-2 soar-incident-response % rm -f .DS_Store
rm -f alerts.json
rm -f alerts/alerts.jsony
rm -f alerts:alerts.json
rm -f response_rules.json

rm -f src:alert_ingestor.py
rm -f src:decision_engine.py
rm -f src:main.py
rm -f src:mitre_mapper.py
rm -f src:reporter.py
rm -f src:response_engine.py

mohammedtawheed@Mohammeds-MacBook-Pro-2 soar-incident-response % ls -R

alerts			config			README.md		reports			requirements.txt	src

./alerts:
alerts.json

./config:
response_rules.json

./reports:
incident_report.txt

./src:
alert_ingestor.py	decision_engine.py	main.py			mitre_mapper.py		reporter.py		response_engine.py
mohammedtawheed@Mohammeds-MacBook-Pro-2 soar-incident-response % git add .
git commit -m "Cleanup: finalize SOAR incident response project structure"

[main 29d89fe] Cleanup: finalize SOAR incident response project structure
 13 files changed, 237 insertions(+), 1588 deletions(-)
 delete mode 100644 alerts.json
 delete mode 100644 alerts/alerts.jsony
 delete mode 100644 alerts:alerts.json
 delete mode 100644 response_rules.json
 delete mode 100644 src:alert_ingestor.py
 delete mode 100644 src:decision_engine.py
 delete mode 100644 src:main.py
 delete mode 100644 src:mitre_mapper.py
 delete mode 100644 src:reporter.py
 delete mode 100644 src:response_engine.py
mohammedtawheed@Mohammeds-MacBook-Pro-2 soar-incident-response % git branch -M main
git remote add origin git@github.com:Tawheed30/soar-incident-response.git
git push -u origin main

Enumerating objects: 33, done.
Counting objects: 100% (33/33), done.
Delta compression using up to 11 threads
Compressing objects: 100% (29/29), done.
Writing objects: 100% (33/33), 7.28 KiB | 2.43 MiB/s, done.
Total 33 (delta 17), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (17/17), done.
To github.com:Tawheed30/soar-incident-response.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.
mohammedtawheed@Mohammeds-MacBook-Pro-2 soar-incident-response % git rm --cached .DS_Store

rm '.DS_Store'
mohammedtawheed@Mohammeds-MacBook-Pro-2 soar-incident-response % git commit -m "Remove macOS .DS_Store from repository"

[main 52df598] Remove macOS .DS_Store from repository
 1 file changed, 0 insertions(+), 0 deletions(-)
 delete mode 100644 .DS_Store
mohammedtawheed@Mohammeds-MacBook-Pro-2 soar-incident-response % git push

Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Delta compression using up to 11 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (2/2), 252 bytes | 252.00 KiB/s, done.
Total 2 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To github.com:Tawheed30/soar-incident-response.git
   29d89fe..52df598  main -> main
mohammedtawheed@Mohammeds-MacBook-Pro-2 soar-incident-response % nano README.md

mohammedtawheed@Mohammeds-MacBook-Pro-2 soar-incident-response % git push

Everything up-to-date
mohammedtawheed@Mohammeds-MacBook-Pro-2 soar-incident-response % git status

On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")
mohammedtawheed@Mohammeds-MacBook-Pro-2 soar-incident-response % git add README.md

mohammedtawheed@Mohammeds-MacBook-Pro-2 soar-incident-response % git commit -m "Clean README documentation"

[main 1d7c54f] Clean README documentation
 1 file changed, 3 insertions(+), 231 deletions(-)
mohammedtawheed@Mohammeds-MacBook-Pro-2 soar-incident-response % git push

Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 11 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 382 bytes | 382.00 KiB/s, done.
Total 3 (delta 2), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To github.com:Tawheed30/soar-incident-response.git
   52df598..1d7c54f  main -> main
mohammedtawheed@Mohammeds-MacBook-Pro-2 soar-incident-response % nano README.md


  UW PICO 5.09                                                                                                           File: README.md                                                                                                            Modified  

# Automated SOAR Incident Response System

## Overview
A Python-based Security Orchestration, Automation, and Response (SOAR) system that ingests security alerts, maps them to MITRE ATT&CK techniques, executes automated response playbooks, and generates SOC-style incident reports.

## Features
- Alert ingestion (JSON-based)
- Automated response decision engine
- Incident response actions (IP blocking, host isolation)
- MITRE ATT&CK technique mapping
- SOC-style incident reporting

## Architecture
Alert → Decision Engine → Response Engine → Reporting

## Project Structure
soar-incident-response/
├──    alerts/
│    └──    alerts.json          # Sample security alerts (input)
├──    config/
│    └──    response_rules.json  # Response playbooks and actions
├──    reports/
│    └──    incident_report.txt  # Generated incident reports
├──    src/
│    ├──    alert_ingestor.py    # Loads and parses alerts
│    ├──    decision_engine.py  # Determines response actions
│    ├──    response_engine.py  # Executes response playbooks
│    ├──    mitre_mapper.py     # Maps alerts to MITRE ATT&CK
│    ├──    reporter.py         # Generates incident reports
│    └──    main.py             # Application entry point
├──    README.md
├──    requirements.txt
└──    .gitignore





































^G Get Help                               ^O WriteOut                               ^R Read File                              ^Y Prev Pg                                ^K Cut Text                               ^C Cur Pos                                
^X Exit                                   ^J Justify                                ^W Where is                               ^V Next Pg                                ^U UnCut Text                             ^T To Spell                               
