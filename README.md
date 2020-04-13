# ATC RE&CT

![](images/logo_v1.png)

The project represents the following:

1. A framework for Incident Response techniques representation
2. A [collection](https://github.com/atc-project/atc-response/tree/master/generated_analytics/markdown_documents/Response_Playbooks) of Security Incident Response Playbooks
3. A data source of the [Atomic Threat Coverage](https://github.com/atc-project/atomic-threat-coverage) framework

## The Framework

is designed for describing and understanding existing Incident Response techniques.  
RE&CT's philosophy is based on the [MITRE's ATT&CK](https://attack.mitre.org/) framework.  
The collumns repsresent stages of [The Six Stages of Incident Response Process](https://www.cynet.com/incident-response/incident-response-sans-the-6-steps-in-depth/).  
The cells repsresent [Response Actions](#response-action).  

| Preparation              | Identification                              | Containment                     | Eradication                                    | Recovery                                    | Lessons Learned                   | 
|--------------------------|---------------------------------------------|---------------------------------|------------------------------------------------|---------------------------------------------|-----------------------------------|
| [Take trainings]         | [Get original email]                        | [Block domain on email]         | [Delete malicious emails]                      | [Reinstall host from golden image]          | [Develop incident report]         |
| [Practice]               | [Extract observables from email]            | [Block IP on border firewall]   | [Revoke compromised credentials]               |                                             | [Conduct lessons earned exercise] |
|                          | [Make sure email is a phishing]             | [Block domain on DNS]           | [Report phishing attack to external companies] |                                             |                                   |
|                          | [Analyse domain name]                       | [Block URL on Proxy]            | [Report incident to external companies]        |                                             |                                   |
|                          | [Analyse filehash]                          | [Block domain on IPS]           |                                                |                                             |                                   |
|                          | [Analyse IP]                                | [Block domain on NGFW]          |                                                |                                             |                                   |
|                          | [Analyse macOS macho]                       | [Block IP on IPS]               |                                                |                                             |                                   |
|                          | [Analyse MS Office file]                    | [Block IP on NGFW]              |                                                |                                             |                                   |
|                          | [Analyse PDF]                               | [Block URL on NGFW]             |                                                |                                             |                                   |
|                          | [Analyse Unix ELF]                          |                                 |                                                |                                             |                                   |
|                          | [Analyse URI]                               |                                 |                                                |                                             |                                   |
|                          | [Analyse MS Windows PE]                     |                                 |                                                |                                             |                                   |
|                          | [Find files executed]                       |                                 |                                                |                                             |                                   |
|                          | [Find services executed]                    |                                 |                                                |                                             |                                   |
|                          | [Find users opened email]                   |                                 |                                                |                                             |                                   |
|                          | [Find registry keys modified]               |                                 |                                                |                                             |                                   |
|                          | [List hosts communicated with domain]       |                                 |                                                |                                             |                                   |
|                          | [List hosts communicated with IP]           |                                 |                                                |                                             |                                   |
|                          | [List hosts communicated with URL]          |                                 |                                                |                                             |                                   |
|                          | [Find files created]                        |                                 |                                                |                                             |                                   |
|                          | [Find all victims in security alerts]       |                                 |                                                |                                             |                                   |
|                          | [Put compromised accounts on monitoring]    |                                 |                                                |                                             |                                   |
|                          |                                             |                                 |                                                |                                             |                                   |
|                          |                                             |                                 |                                                |                                             |                                   |

[Take trainings]: generated_analytics/markdown_documents/Response_Actions/RA_1102_take_trainings.md
[Practice]: generated_analytics/markdown_documents/Response_Actions/RA_1101_practice.md
[Get original email]: generated_analytics/markdown_documents/Response_Actions/RA_2302_get_original_email.md
[Extract observables from email]: generated_analytics/markdown_documents/Response_Actions/RA_2101_extract_observables_from_email.md
[Make sure email is a phishing]: generated_analytics/markdown_documents/Response_Actions/RA_2102_make_sure_email_is_a_phishing.md
[Analyse domain name]: generated_analytics/markdown_documents/Response_Actions/RA_2204_analyse_domain_name.md
[Analyse filehash]: generated_analytics/markdown_documents/Response_Actions/RA_2404_analyse_filehash.md
[Analyse IP]: generated_analytics/markdown_documents/Response_Actions/RA_2205_analyse_ip.md
[Analyse macOS macho]: generated_analytics/markdown_documents/Response_Actions/RA_2405_analyse_macos_macho.md
[Analyse MS Office file]: generated_analytics/markdown_documents/Response_Actions/RA_2406_analyse_ms_office_file.md
[Analyse PDF]: generated_analytics/markdown_documents/Response_Actions/RA_2407_analyse_pdf.md
[Analyse Unix ELF]: generated_analytics/markdown_documents/Response_Actions/RA_2408_analyse_unix_elf.md
[Analyse URI]: generated_analytics/markdown_documents/Response_Actions/RA_2206_analyse_uri.md
[Analyse MS Windows PE]: generated_analytics/markdown_documents/Response_Actions/RA_2402_analyse_windows_pe.md
[Find files executed]: generated_analytics/markdown_documents/Response_Actions/RA_2403_find_files_executed.md
[Find services executed]: generated_analytics/markdown_documents/Response_Actions/RA_2501_find_services_executed.md
[Find users opened email]: generated_analytics/markdown_documents/Response_Actions/RA_2301_find_users_opened_email.md
[Find registry keys modified]: generated_analytics/markdown_documents/Response_Actions/RA_2601_find_registry_keys_modified.md
[List hosts communicated with domain]: generated_analytics/markdown_documents/Response_Actions/RA_2201_list_hosts_communicated_with_domain.md
[List hosts communicated with IP]: generated_analytics/markdown_documents/Response_Actions/RA_2202_list_hosts_communicated_with_ip.md
[List hosts communicated with URL]: generated_analytics/markdown_documents/Response_Actions/RA_2203_list_hosts_communicated_with_url.md
[Find files created]: generated_analytics/markdown_documents/Response_Actions/RA_2401_find_files_created.md
[Find all victims in security alerts]: generated_analytics/markdown_documents/Response_Actions/RA_2104_find_all_victims_in_security_alerts.md
[Put compromised accounts on monitoring]: generated_analytics/markdown_documents/Response_Actions/RA_2103_put_compromised_accounts_on_monitoring.md
[Block domain on email]: generated_analytics/markdown_documents/Response_Actions/RA_3201_block_domain_on_email.md
[Block IP on border firewall]: generated_analytics/markdown_documents/Response_Actions/RA_3202_block_ip_on_border_firewall.md
[Block domain on DNS]: generated_analytics/markdown_documents/Response_Actions/RA_3203_block_domain_on_dns.md
[Block URL on Proxy]: generated_analytics/markdown_documents/Response_Actions/RA_3204_block_url_on_proxy.md
[Block domain on IPS]: generated_analytics/markdown_documents/Response_Actions/RA_3205_block_domain_on_ips.md
[Block domain on NGFW]: generated_analytics/markdown_documents/Response_Actions/RA_3206_block_domain_on_ngfw.md
[Block IP on IPS]: generated_analytics/markdown_documents/Response_Actions/RA_3207_block_ip_on_ips.md
[Block IP on NGFW]: generated_analytics/markdown_documents/Response_Actions/RA_3208_block_ip_on_ngfw.md
[Block URL on NGFW]: generated_analytics/markdown_documents/Response_Actions/RA_3209_block_url_on_ngfw.md
[Delete malicious emails]: generated_analytics/markdown_documents/Response_Actions/RA_4301_delete_malicious_emails.md
[Revoke compromised credentials]: generated_analytics/markdown_documents/Response_Actions/RA_4701_revoke_compromised_credentials.md
[Report phishing attack to external companies]: generated_analytics/markdown_documents/Response_Actions/RA_4101_report_phishing_attack_to_external_companies.md
[Report incident to external companies]: generated_analytics/markdown_documents/Response_Actions/RA_4102_report_incident_to_external_companies.md
[Reinstall host from golden image]: generated_analytics/markdown_documents/Response_Actions/RA_5101_reinstall_host_from_golden_image.md
[Develop incident report]: generated_analytics/markdown_documents/Response_Actions/RA_6101_develop_incident_report.md
[Conduct lessons earned exercise]: generated_analytics/markdown_documents/Response_Actions/RA_6102_conduct_lessons_learned_exercise.md


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