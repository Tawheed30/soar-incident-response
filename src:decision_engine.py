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


  UW PICO 5.09                                                                                                     File: src/decision_engine.py                                                                                                     Modified  

import json

def decide_response(alert, rules_file):
    with open(rules_file, "r") as f:
        rules = json.load(f)

    return rules.get(alert["type"], "NO_ACTION")































































^G Get Help                               ^O WriteOut                               ^R Read File                              ^Y Prev Pg                                ^K Cut Text                               ^C Cur Pos                                
^X Exit                                   ^J Justify                                ^W Where is                               ^V Next Pg                                ^U UnCut Text                             ^T To Spell                               
