# ATC RE&CT

Actionable Security Incident Response Playbooks.

![](images/logo_v1.png)

ATC RE&CT is a sub-project of [Atomic Threat Coverage](https://github.com/atc-project/atomic-threat-coverage) framework, related to Security Incident Response process.

It represents the following:

1. A framework for Incident Response techniques representation
2. A collection of Security Incident Response Playbooks
3. A data source of the [Atomic Threat Coverage](https://github.com/atc-project/atomic-threat-coverage) framework

## The Framework

is designed for describing and understanding existing Incident Response techniques.  
RE&CT's philosophy is based on the [MITRE's ATT&CK](https://attack.mitre.org/) framework.  
The cells repsresent [Response Action](#response-action).  
The collumns repsresent stages of [The Six Stages of Incident Response Process](https://www.cynet.com/incident-response/incident-response-sans-the-6-steps-in-depth/).  

| Preparation              | Identification                              | Containment                     | Eradication                                    | Recovery                                    | Lessons Learned                   | 
|--------------------------|---------------------------------------------|---------------------------------|------------------------------------------------|---------------------------------------------|-----------------------------------|
| [Practice]               | [Get original email]                        | [Block threat on network level] | [Delete malicious emails]                      | [Recovery reinstall host from golden image] | [Develop incident report]         |
|                          | [Extract observables from email]            | [Block domain on email]         | [Revoke compromised credentials]               |                                             | [Conduct lessons earned exercise] |
|                          | [Make sure email is a phishing]             | [Block ip on border firewall]   | [Report phishing attack to external companies] |                                             |                                   |
|                          | [Analyse obtained indicators of compromise] | [Block domain on dns]           | [Report incident to external companies]        |                                             |                                   |
|                          | [Find all phishing attack victims]          | [Block url on proxy]            |                                                |                                             |                                   |
|                          | [Analyse domain name]                       | [Block domain on ips]           |                                                |                                             |                                   |
|                          | [Analyse filehash]                          | [Block domain on ngfw]          |                                                |                                             |                                   |
|                          | [Analyse ip]                                | [Block ip on ips]               |                                                |                                             |                                   |
|                          | [Analyse macos macho]                       | [Block ip on ngfw]              |                                                |                                             |                                   |
|                          | [Analyse ms office file]                    | [Block url on ngfw]             |                                                |                                             |                                   |
|                          | [Analyse pdf]                               |                                 |                                                |                                             |                                   |
|                          | [Analyse unix elf]                          |                                 |                                                |                                             |                                   |
|                          | [Analyse uri]                               |                                 |                                                |                                             |                                   |
|                          | [Analyse windows pe]                        |                                 |                                                |                                             |                                   |
|                          | [Find files executed]                       |                                 |                                                |                                             |                                   |
|                          | [Find services executed]                    |                                 |                                                |                                             |                                   |
|                          | [Find emails opened]                        |                                 |                                                |                                             |                                   |
|                          | [Find registry keys modified]               |                                 |                                                |                                             |                                   |
|                          | [Find all hosts communicated with domain]   |                                 |                                                |                                             |                                   |
|                          | [Find all hosts communicated with ip]       |                                 |                                                |                                             |                                   |
|                          | [Find all hosts communicated with url]      |                                 |                                                |                                             |                                   |
|                          | [Find files created]                        |                                 |                                                |                                             |                                   |
|                          | [Find all victims in security alerts]       |                                 |                                                |                                             |                                   |
|                          | [Put compromised accounts on monitoring]    |                                 |                                                |                                             |                                   |

[Practice]: generated_analytics/markdown_documents/Response_Actions/RA_0041_eradication_report_incident_to_external_companies.md
[Get original email]: generated_analytics/markdown_documents/Response_Actions/RA_0001_identification_get_original_email.md
[Extract observables from email]: generated_analytics/markdown_documents/Response_Actions/RA_0002_identification_extract_observables_from_email.md
[Make sure email is a phishing]: generated_analytics/markdown_documents/Response_Actions/RA_0003_identification_make_sure_email_is_a_phishing.md
[Analyse obtained indicators of compromise]: generated_analytics/markdown_documents/Response_Actions/RA_0004_identification_analyse_obtained_indicators_of_compromise.md
[Find all phishing attack victims]: generated_analytics/markdown_documents/Response_Actions/RA_0005_identification_find_all_phishing_attack_victims.md
[Analyse domain name]: generated_analytics/markdown_documents/Response_Actions/RA_0015_identification_analyse_domain_name.md
[Analyse filehash]: generated_analytics/markdown_documents/Response_Actions/RA_0016_identification_analyse_filehash.md
[Analyse ip]: generated_analytics/markdown_documents/Response_Actions/RA_0017_identification_analyse_ip.md
[Analyse macos macho]: generated_analytics/markdown_documents/Response_Actions/RA_0018_identification_analyse_macos_macho.md
[Analyse ms office file]: generated_analytics/markdown_documents/Response_Actions/RA_0019_identification_analyse_ms_office_file.md
[Analyse pdf]: generated_analytics/markdown_documents/Response_Actions/RA_0020_identification_analyse_pdf.md
[Analyse unix elf]: generated_analytics/markdown_documents/Response_Actions/RA_0021_identification_analyse_unix_elf.md
[Analyse uri]: generated_analytics/markdown_documents/Response_Actions/RA_0022_identification_analyse_uri.md
[Analyse windows pe]: generated_analytics/markdown_documents/Response_Actions/RA_0023_identification_analyse_windows_pe.md
[Find files executed]: generated_analytics/markdown_documents/Response_Actions/RA_0024_identification_find_files_executed.md
[Find services executed]: generated_analytics/markdown_documents/Response_Actions/RA_0025_identification_find_services_executed.md
[Find emails opened]: generated_analytics/markdown_documents/Response_Actions/RA_0026_identification_find_emails_opened.md
[Find registry keys modified]: generated_analytics/markdown_documents/Response_Actions/RA_0027_identification_find_registry_keys_modified.md
[Find all hosts communicated with domain]: generated_analytics/markdown_documents/Response_Actions/RA_0030_identification_find_all_hosts_communicated_with_domain.md
[Find all hosts communicated with ip]: generated_analytics/markdown_documents/Response_Actions/RA_0031_identification_find_all_hosts_communicated_with_ip.md
[Find all hosts communicated with url]: generated_analytics/markdown_documents/Response_Actions/RA_0032_identification_find_all_hosts_communicated_with_url.md
[Find files created]: generated_analytics/markdown_documents/Response_Actions/RA_0033_identification_find_files_created.md
[Find all victims in security alerts]: generated_analytics/markdown_documents/Response_Actions/RA_0034_identification_find_all_victims_in_security_alerts.md
[Put compromised accounts on monitoring]: generated_analytics/markdown_documents/Response_Actions/RA_0040_identification_put_compromised_accounts_on_monitoring.md
[Block threat on network level]: generated_analytics/markdown_documents/Response_Actions/RA_0028_containment_block_threat_on_network_level.md
[Block domain on email]: generated_analytics/markdown_documents/Response_Actions/RA_0006_containment_block_domain_on_email.md
[Block ip on border firewall]: generated_analytics/markdown_documents/Response_Actions/RA_0007_containment_block_ip_on_border_firewall.md
[Block domain on dns]: generated_analytics/markdown_documents/Response_Actions/RA_0008_containment_block_domain_on_dns.md
[Block url on proxy]: generated_analytics/markdown_documents/Response_Actions/RA_0009_containment_block_url_on_proxy.md
[Block domain on ips]: generated_analytics/markdown_documents/Response_Actions/RA_0035_containment_block_domain_on_ips.md
[Block domain on ngfw]: generated_analytics/markdown_documents/Response_Actions/RA_0036_containment_block_domain_on_ngfw.md
[Block ip on ips]: generated_analytics/markdown_documents/Response_Actions/RA_0037_containment_block_ip_on_ips.md
[Block ip on ngfw]: generated_analytics/markdown_documents/Response_Actions/RA_0038_containment_block_ip_on_ngfw.md
[Block url on ngfw]: generated_analytics/markdown_documents/Response_Actions/RA_0039_containment_block_url_on_ngfw.md
[Delete malicious emails]: generated_analytics/markdown_documents/Response_Actions/RA_0010_eradication_delete_malicious_emails.md
[Revoke compromised credentials]: generated_analytics/markdown_documents/Response_Actions/RA_0011_eradication_revoke_compromised_credentials.md
[Report phishing attack to external companies]: generated_analytics/markdown_documents/Response_Actions/RA_0012_eradication_report_phishing_attack_to_external_companies.md
[Report incident to external companies]: generated_analytics/markdown_documents/Response_Actions/RA_0041_eradication_report_incident_to_external_companies.md
[Recovery reinstall host from golden image]: generated_analytics/markdown_documents/Response_Actions/RA_0029_recovery_reinstall_host_from_golden_image.md
[Develop incident report]: generated_analytics/markdown_documents/Response_Actions/RA_0013_lessons_learned_develop_incident_report.md
[Conduct lessons earned exercise]: generated_analytics/markdown_documents/Response_Actions/RA_0014_lessons_learned_conduct_lessons_learned_exercise.md

## Actionable Playbooks

The ATC RE&CT project inherits the "Actionable Analytics" paradigm from the parent project, which means that the analytics are:

- **human-readable** (`.markdown`) for sharing/using in operations
- **machine-readable** (`.yaml`) for automatic processing/integrations
- **executable** by Incident Response Platform ([TheHive Case Templates](analytics/generated/thehive_templates/) only, at the moment)

Simply saying, the analytics are stored in `.yaml` files, that are automatically converted to `.markdown` documents (with [jinja](https://palletsprojects.com/p/jinja/)) and `.json` TheHive Case Templates.

### Response Action

is a description of a specific atomic procedure/task that has to be executed during the Incident Response. It is an initial entity that is used to construct Response Playbooks and TheHive Case Templates' tasks. 

Here is an example of Response Action:

<details>
  <summary>Initial YAML file (click to expand)</summary>
  <img src="images/ra_yaml_v3.png" />
</details>

<details>
  <summary>Automatically created Markdown file (click to expand)</summary>
  <img src="images/ra_markdown_v3.png" />
</details>

Each Response Action mapped to a specific stage of [The Six Stages of Incident Response Process](https://www.cynet.com/incident-response/incident-response-sans-the-6-steps-in-depth/).

### Response Playbook

is an Incident Response plan, that represents a complete list of procedures/tasks (Response Actions) that has to be executed to respond to a specific threat with optional mapping to the [MITRE's ATT&CK](https://attack.mitre.org/) or [Misinfosec's  AMITT](https://github.com/misinfosecproject/amitt_framework) frameworks.

Here is an example of Response Playbook:

<details>
  <summary>Initial YAML file (click to expand)</summary>
  <img src="images/rp_yaml_v3.png" />
</details>

<details>
  <summary>Automatically created Markdown file (click to expand)</summary>
  <img src="images/rp_markdown_v3.png" />
</details>

Response Playbook could include a description of the workflow, specific conditions/requirements or details on the order of Response Actions execution.

### TheHive Case Templates

are built on top of the Response Playbooks. Each task in a Case Template is a Response Action (with full description). 

Here is the example of an imported TheHive Case Template:

<details>
  <summary>Imported TheHive Case Template, made on top of a Response Playbook (click to expand)</summary>
  <img src="images/thehive_case_template_v1.png" />
</details>

<details>
  <summary>One of the Tasks in TheHive Case, made on top of a Response Action (click to expand)</summary>
  <img src="images/thehive_case_task_v1.png" />
</details>

TheHive Case Templates could be found in `generated_analytics/thehive_templates` directory and could be imported to TheHive via its web interface.

## Data source of the ATC framework

ATC RE&CT project plays a role of data source for the [Atomic Threat Coverage](https://github.com/atc-project/atomic-threat-coverage) framework, that uses it to generate markdown and confluence knowledge bases, ATT&CK Navigator profiles, Elasticsearch indexes and [other](https://github.com/atc-project/atomic-threat-coverage#how-it-works) analytics. 

Originally it was a part of the ATC, but we decided to move it into a separate project to make it easier to maintain and provide an option for integration with other projects in this area. 

## Usage

1. Make sure you are compliant with the [requirements](#requirements)

2. Modify existing `.yaml` files, or develop your own analytics using the templates of [Response Actions](response_actions/respose_action.yml.template) or [Response Playbooks](response_playbooks/respose_playbook.yml.template). They should be stored in the directories according to their type.

3. When `.yaml` files are ready, convert them to `.markdown` documents and TheHive templates using the following commands:
    ```
    python3 main.py --markdown --auto --init
    python3 main.py --thehive
    ```
    You will find the outcome in the `generated_analytics` directory.

### Requirements

- Python 3.7
- [PyYAML](https://pypi.org/project/PyYAML/) and [jinja2](https://pypi.org/project/Jinja2/) Python libraries. They could be installed with the next command:
    ```
    python3 -m pip install -r requirements.txt
    ```

## Contacts

- Folow us on [Twitter](https://twitter.com/atc_project) for updates
- Join discussions in [Slack](https://join.slack.com/t/atomicthreatcoverage/shared_invite/enQtNTMwNDUyMjY2MTE5LTk1ZTY4NTBhYjFjNjhmN2E3OTMwYzc4MTEyNTVlMTVjMDZmMDg2OWYzMWRhMmViMjM5YmM1MjhkOWFmYjE5MjA) or [Telegram](https://t.me/atomic_threat_coverage) 

## Authors

- Jakob Weinzettl, [@mrblacyk](https://github.com/mrblacyk)
- Mateusz Wydra, [@sn0w0tter](https://github.com/sn0w0tter)
- Daniil Yugoslavskiy, [@yugoslavskiy](https://github.com/yugoslavskiy)

## Contributors

Would you like to become one? You are very welcome! Use [CONTRIBUTING](https://github.com/atc-project/atomic-threat-coverage/blob/master/CONTRIBUTING.md) guidelines to contribute to the main project.

## License

See the [LICENSE](LICENSE) file.