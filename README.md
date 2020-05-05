🇷🇺 [Русская версия](README_RU.md)  

# RE&CT

![](docs/images/logo_v2.png)

The project represents the following:

1. A [framework](https://atc-project.github.io/atc-react/) — knowledge base of actionable Incident Response techniques
2. A community-driven [collection](docs/Response_Playbooks) of Security Incident Response Playbooks
3. A data source of the [Atomic Threat Coverage](https://github.com/atc-project/atomic-threat-coverage) framework

## The RE&CT Framework

is designed for accumulating, describing and categorizing actionable Incident Response techniques. 

RE&CT's philosophy is based on the [MITRE's ATT&CK](https://attack.mitre.org/) framework.  
The columns represent [Incident Response stages](https://atc-project.github.io/atc-react/responsestages/).  
The cells repsresent [Response Actions](#response-action).  

![](docs/images/react_navigator_export_v2.svg)

The main use cases:

- Prioritization of Incident Response capabilities development
- Gap analysis — determine "coverage" of existing Incident Response capabilities

The main resources:

- RE&CT [website](https://atc-project.github.io/atc-react/) is the best place for getting details about existing analytics  
- [RE&CT Navigator](https://atc-project.github.io/react-navigator/) (modified [ATT&CK Navigator](https://github.com/mitre-attack/attack-navigator)) for visualization and observing the big picture  

## Actionable Analytics

The ATC RE&CT project inherits the "Actionable Analytics" paradigm from the [ATC](https://github.com/atc-project/atomic-threat-coverage) project, which means that the analytics are:

- **human-readable** (`.md`) for sharing/using in operations
- **machine-readable** (`.yml`) for automatic processing/integrations
- **executable** by Incident Response Platform ([TheHive Case Templates](docs/thehive_templates/) only, at the moment)

Simply saying, the analytics are stored in `.yml` files, that are automatically converted to `.md` documents (with [jinja](https://palletsprojects.com/p/jinja/)) and `.json` TheHive Case Templates.

### Response Action

is a description of a specific atomic procedure/task that has to be executed during the Incident Response. It is an initial entity that is used to construct Response Playbooks.  

Here is an example of Response Action:

<details>
  <summary>Initial YAML file (click to expand)</summary>
  <img src="docs/images/ra_yaml_v4.png" />
</details>

<details>
  <summary>Automatically created Markdown file (click to expand)</summary>
  <img src="docs/images/ra_markdown_v4.png" />
</details>

<details>
  <summary>Automatically created (by main ATC project) Confluence page (click to expand)</summary>
  <img src="docs/images/ra_confluence_v2.png" />
</details>

Each Response Action mapped to a specific [Incident Response stage](https://atc-project.github.io/atc-react/responsestages/).  
The first digit of the Response Action ID reflects a stage number.  
The second digit of the Response Action ID reflects a category it belongs to:

- **0**: General
- **1**: Network
- **2**: Email
- **3**: File
- **4**: Process
- **5**: Configuration
- **6**: Identity

This way, using Response Action ID, you can see the Stage and Category it belongs to.  
For example, [RA**22**02: Collect an email message](docs/Response_Actions/RA_2202_collect_email_message.md) is related to Stage **2** (Identification) and Category **2** (Email).

The categorization aims to improve Incident Response process maturity assessment and roadmap development.

### Response Playbook

is an Incident Response plan, that represents a complete list of procedures/tasks (Response Actions) that has to be executed to respond to a specific threat with optional mapping to the [MITRE's ATT&CK](https://attack.mitre.org/) or [Misinfosec's  AMITT](https://github.com/misinfosecproject/amitt_framework) frameworks.

Here is an example of Response Playbook:

<details>
  <summary>Initial YAML file (click to expand)</summary>
  <img src="docs/images/rp_yaml_v4.png" />
</details>

<details>
  <summary>Automatically created Markdown file (click to expand)</summary>
  <img src="docs/images/rp_markdown_v5.png" />
</details>

<details>
  <summary>Automatically created (by main ATC project) Confluence page (click to expand)</summary>
  <img src="docs/images/rp_confluence_v1.png" />
</details>

Response Playbook could include a description of the workflow, specific conditions/requirements, details on the order of Response Actions execution, or any other relevant information.

### TheHive Case Templates

are built on top of the Response Playbooks. Each task in a Case Template is a Response Action (with full description). 

Here is the example of an imported TheHive Case Template:

<details>
  <summary>Imported TheHive Case Template, made on top of a Response Playbook (click to expand)</summary>
  <img src="docs/images/thehive_case_template_v1.png" />
</details>

<details>
  <summary>One of the Tasks in TheHive Case, made on top of a Response Action (click to expand)</summary>
  <img src="docs/images/thehive_case_task_v1.png" />
</details>

TheHive Case Templates could be found in `docs/thehive_templates` directory and could be imported to TheHive via its web interface.

## Data source of the ATC framework

ATC RE&CT project plays a role of data source for the [Atomic Threat Coverage](https://github.com/atc-project/atomic-threat-coverage) framework, that uses it to generate Markdown and Confluence knowledge bases, ATT&CK Navigator profiles, Elasticsearch indexes and [other](https://github.com/atc-project/atomic-threat-coverage#how-it-works) analytics. 

Originally analytics related to Incident Response were part of the ATC, but we decided to move it into a separate project to make it easier to maintain and provide an option for integration with other projects in this area. 

## Usage

1. Make sure you are compliant with the [requirements](#requirements)

2. Modify existing `.yml` files, or develop your own analytics using the templates of [Response Actions](response_actions/respose_action.yml.template) or [Response Playbooks](response_playbooks/respose_playbook.yml.template). They should be stored in the directories according to their type.

3. When `.yml` files are ready, convert them to `.md` documents, TheHive templates and [RE&CT Navigator](https://github.com/atc-project/react-navigator) profile using the following commands:
    ```
    python3 main.py --markdown --auto --init
    python3 main.py --thehive
    python3 main.py -NAV
    ```
    You will find the outcome in the `docs` directory.

4. Generate your own (private) website with your analytics, using [mkdocs](https://www.mkdocs.org/):
    ```
    python3 main.py -MK         # automatic mkdocs config (navigation) generation
    python3 -m mkdocs build
    ```
    The website will be stored in the `site` directory.  You can preview it with the following command:
    ```
    python3 -m mkdocs serve
    ```

### Requirements

- Python 3.7
- [PyYAML](https://pypi.org/project/PyYAML/), [mkdocs](https://pypi.org/project/mkdocs/), [jinja2](https://pypi.org/project/Jinja2/) and [stix2](https://pypi.org/project/stix2/) (optionally)  Python libraries. They could be installed with the following command:
    ```
    python3 -m pip install -r requirements.txt
    ```

## Contacts

- Folow us on [Twitter](https://twitter.com/atc_project) for updates
- Join discussions in [Slack](https://join.slack.com/t/atomicthreatcoverage/shared_invite/enQtNTMwNDUyMjY2MTE5LTk1ZTY4NTBhYjFjNjhmN2E3OTMwYzc4MTEyNTVlMTVjMDZmMDg2OWYzMWRhMmViMjM5YmM1MjhkOWFmYjE5MjA) or [Telegram](https://t.me/atomic_threat_coverage) 

## Authors

- Jakob Weinzettl, [@mrblacyk](https://github.com/mrblacyk)
- Mateusz Wydra, [@sn0w0tter](https://github.com/sn0w0tter)
- Daniil Yugoslavskiy, [@yugoslavskiy](https://twitter.com/yugoslavskiy)

## Contributors

Would you like to become one? You are very welcome! Our [CONTRIBUTING](CONTRIBUTING.md) guideline is a good starting point.

## Roadmap

The roadmap and related discussions could be found in the project [issues](https://github.com/atc-project/atc-react/issues).

## License

See the [LICENSE](LICENSE) file.
