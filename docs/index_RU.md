🇬🇧 [English version](index.md)  

# RE&CT

![](images/logo_v2.png)

Фреймворк создан для накопления, описания и классификации действенных техник реагирования на инциденты.  

Философия RE&CT основана на подходе фреймворка [MITRE ATT&CK](https://attack.mitre.org/).  
Столбцы представляют собой [Стадии Реагирования (Response Stages)](https://atc-project.github.io/atc-react/responsestages/).  
Ячейки представляют собой [Действия Реагирования (Response Actions)](#response-action).  

Основные варианты использования:

- Приоритизация задач по созданию и совершенствованию процесса реагирования на инциденты, включая развитие компетенций, внедрение технических средств, разработку регламентов и т.д.
- Анализ недочетов — определение "степени покрытия" матрицы RE&CT уже реализованными функциями реагирования на инциденты

Основные ресурсы:

- [RE&CT Navigator](https://atc-project.github.io/react-navigator/) (модифицированный [ATT&CK Navigator](https://github.com/mitre-attack/attack-navigator)) для визуализации и анализа общей картины  
- Автоматически сгенерированный [веб-сайт](https://atc-project.github.io/atc-react/) фреймворка RE&CT — лучшее место для детального изучения существующих техник реагирования на инциденты  
- Автоматически сгенерированная [база знаний в Atlassian Confluence](https://atomicthreatcoverage.atlassian.net/wiki/spaces/REACT/pages/755469668/Response+Stages) — демонстрация функции по экспорта аналитики  


| Preparation                                                   | Identification                                     | Containment                                    | Eradication                                 | Recovery                                | Lessons Learned                        |
|:-------------------------------------------------------------:|:--------------------------------------------------:|:----------------------------------------------:|:-------------------------------------------:|:---------------------------------------:|:--------------------------------------:|
| [**Practice**]                                                | [List victims of security alert*]                  | [Patch vulnerability*]                         | [**Report incident to external companies**] | [Reinstall host from golden image*]     | [**Develop incident report**]          |
| [**Take trainings**]                                          | [List host vulnerabilities*]                       | [**Block external IP address**]                | [Remove rogue network device*]              | [Restore data from backup*]             | [**Conduct lessons learned exercise**] |
| [**Raise personnel awareness**]                               | [**Put compromised accounts on monitoring**]       | [**Block internal IP address**]                | [**Delete email message**]                  | [**Unblock blocked IP**]                |                                        |
| [**Make personnel report suspicious activity**]               | [List hosts communicated with internal domain*]    | [**Block external domain**]                    | [Remove file*]                              | [**Unblock blocked domain**]            |                                        |
| [Set up relevant data collection*]                            | [List hosts communicated with internal IP*]        | [**Block internal domain**]                    | [Remove registry key*]                      | [**Unblock blocked URL**]               |                                        |
| [Set up a centralized long-term log storage*]                 | [List hosts communicated with internal URL*]       | [**Block external URL**]                       | [Remove service*]                           | [Unblock blocked port*]                 |                                        |
| [Develop communication map*]                                  | [Analyse domain name*]                             | [**Block internal URL**]                       | [**Revoke authentication credentials**]     | [Unblock blocked user*]                 |                                        |
| [Make sure there are backups*]                                | [Analyse IP*]                                      | [**Block port external communication**]        | [Remove user account*]                      | [**Unblock domain on email**]           |                                        |
| [Get network architecture map*]                               | [Analyse URI*]                                     | [**Block port internal communication**]        |                                             | [**Unblock sender on email**]           |                                        |
| [Get access control matrix*]                                  | [List hosts communicated by port*]                 | [**Block user external communication**]        |                                             | [**Restore quarantined email message**] |                                        |
| [Develop assets knowledge base*]                              | [List hosts connected to VPN*]                     | [**Block user internal communication**]        |                                             | [Restore quarantined file*]             |                                        |
| [Check analysis toolset*]                                     | [List hosts connected to intranet*]                | [Block data transferring by content pattern*]  |                                             | [Unblock blocked process*]              |                                        |
| [Access vulnerability management system logs*]                | [List data transferred*]                           | [**Block domain on email**]                    |                                             | [Enable disabled service*]              |                                        |
| [**Connect with trusted communities**]                        | [Collect transferred data*]                        | [**Block sender on email**]                    |                                             | [Unlock locked user account*]           |                                        |
| [**Access external network flow logs**]                       | [Identify transferred data*]                       | [**Quarantine email message**]                 |                                             |                                         |                                        |
| [Access internal network flow logs*]                          | [**List hosts communicated with external domain**] | [Quarantine file by format*]                   |                                             |                                         |                                        |
| [Access internal HTTP logs*]                                  | [**List hosts communicated with external IP**]     | [Quarantine file by hash*]                     |                                             |                                         |                                        |
| [**Access external HTTP logs**]                               | [**List hosts communicated with external URL**]    | [Quarantine file by path*]                     |                                             |                                         |                                        |
| [Access internal DNS logs*]                                   | [Find data transferred by content pattern*]        | [Quarantine file by content pattern*]          |                                             |                                         |                                        |
| [**Access external DNS logs**]                                | [Analyse user-agent*]                              | [Block process by executable path*]            |                                             |                                         |                                        |
| [Access VPN logs*]                                            | [**List users opened email message**]              | [Block process by executable metadata*]        |                                             |                                         |                                        |
| [Access DHCP logs*]                                           | [**Collect email message**]                        | [Block process by executable hash*]            |                                             |                                         |                                        |
| [Access internal packet capture data*]                        | [**List email message receivers**]                 | [Block process by executable format*]          |                                             |                                         |                                        |
| [Access external packet capture data*]                        | [**Make sure email message is phishing**]          | [Block process by executable content pattern*] |                                             |                                         |                                        |
| [**Get ability to block external IP address**]                | [**Extract observables from email message**]       | [Disable system service*]                      |                                             |                                         |                                        |
| [Get ability to block internal IP address*]                   | [Analyse email address*]                           | [Lock user account*]                           |                                             |                                         |                                        |
| [**Get ability to block external domain**]                    | [List files created*]                              |                                                |                                             |                                         |                                        |
| [Get ability to block internal domain*]                       | [List files modified*]                             |                                                |                                             |                                         |                                        |
| [**Get ability to block external URL**]                       | [List files deleted*]                              |                                                |                                             |                                         |                                        |
| [Get ability to block internal URL*]                          | [List files downloaded*]                           |                                                |                                             |                                         |                                        |
| [Get ability to block port external communication*]           | [List files with tampered timestamps*]             |                                                |                                             |                                         |                                        |
| [Get ability to block port internal communication*]           | [Find file by path*]                               |                                                |                                             |                                         |                                        |
| [Get ability to block user external communication*]           | [Find file by metadata*]                           |                                                |                                             |                                         |                                        |
| [Get ability to block user internal communication*]           | [Find file by hash*]                               |                                                |                                             |                                         |                                        |
| [Get ability to find data transferred by content pattern*]    | [Find file by format*]                             |                                                |                                             |                                         |                                        |
| [Get ability to block data transferring by content pattern*]  | [Find file by content pattern*]                    |                                                |                                             |                                         |                                        |
| [Get ability to list data transferred*]                       | [Collect file*]                                    |                                                |                                             |                                         |                                        |
| [Get ability to collect transferred data*]                    | [Analyse file hash*]                               |                                                |                                             |                                         |                                        |
| [Get ability to identify transferred data*]                   | [Analyse Windows PE*]                              |                                                |                                             |                                         |                                        |
| [Find data transferred by content pattern*]                   | [Analyse macos macho*]                             |                                                |                                             |                                         |                                        |
| [Get ability to analyse user-agent*]                          | [Analyse Unix ELF*]                                |                                                |                                             |                                         |                                        |
| [**Get ability to list users opened email message**]          | [Analyse MS office file*]                          |                                                |                                             |                                         |                                        |
| [**Get ability to list email message receivers**]             | [Analyse PDF file*]                                |                                                |                                             |                                         |                                        |
| [**Get ability to block email domain**]                       | [Analyse script*]                                  |                                                |                                             |                                         |                                        |
| [**Get ability to block email sender**]                       | [Analyse jar*]                                     |                                                |                                             |                                         |                                        |
| [**Get ability to delete email message**]                     | [Analyse filename*]                                |                                                |                                             |                                         |                                        |
| [**Get ability to quarantine email message**]                 | [List processes executed*]                         |                                                |                                             |                                         |                                        |
| [Get ability to collect email message*]                       | [Find process by executable path*]                 |                                                |                                             |                                         |                                        |
| [Get ability to analyse email address*]                       | [Find process by executable metadata*]             |                                                |                                             |                                         |                                        |
| [Get ability to list files created*]                          | [Find process by executable hash*]                 |                                                |                                             |                                         |                                        |
| [Get ability to list files modified*]                         | [Find process by executable format*]               |                                                |                                             |                                         |                                        |
| [Get ability to list files deleted*]                          | [Find process by executable content pattern*]      |                                                |                                             |                                         |                                        |
| [Get ability to list files downloaded*]                       | [List registry keys modified*]                     |                                                |                                             |                                         |                                        |
| [Get ability to list files with tampered timestamps*]         | [List registry keys deleted*]                      |                                                |                                             |                                         |                                        |
| [Get ability to find file by path*]                           | [List registry keys accessed*]                     |                                                |                                             |                                         |                                        |
| [Get ability to find file by metadata*]                       | [List registry keys created*]                      |                                                |                                             |                                         |                                        |
| [Get ability to find file by hash*]                           | [List services created*]                           |                                                |                                             |                                         |                                        |
| [Get ability to find file by format*]                         | [List services modified*]                          |                                                |                                             |                                         |                                        |
| [Get ability to find file by content pattern*]                | [List services deleted*]                           |                                                |                                             |                                         |                                        |
| [Get ability to collect file*]                                | [Analyse registry key*]                            |                                                |                                             |                                         |                                        |
| [Get ability to quarantine file by path*]                     | [List users authenticated*]                        |                                                |                                             |                                         |                                        |
| [Get ability to quarantine file by hash*]                     |                                                    |                                                |                                             |                                         |                                        |
| [Get ability to quarantine file by format*]                   |                                                    |                                                |                                             |                                         |                                        |
| [Get ability to quarantine file by content pattern*]          |                                                    |                                                |                                             |                                         |                                        |
| [Get ability to remove file*]                                 |                                                    |                                                |                                             |                                         |                                        |
| [Get ability to analyse file hash*]                           |                                                    |                                                |                                             |                                         |                                        |
| [Get ability to analyse windows pe*]                          |                                                    |                                                |                                             |                                         |                                        |
| [Get ability to analyse macos macho*]                         |                                                    |                                                |                                             |                                         |                                        |
| [Get ability to analyse unix elf*]                            |                                                    |                                                |                                             |                                         |                                        |
| [Get ability to analyse ms office file*]                      |                                                    |                                                |                                             |                                         |                                        |
| [Get ability to analyse pdf file*]                            |                                                    |                                                |                                             |                                         |                                        |
| [Get ability to analyse script*]                              |                                                    |                                                |                                             |                                         |                                        |
| [Get ability to analyse jar*]                                 |                                                    |                                                |                                             |                                         |                                        |
| [Get ability to analyse filename*]                            |                                                    |                                                |                                             |                                         |                                        |
| [Get ability to list processes executed*]                     |                                                    |                                                |                                             |                                         |                                        |
| [Get ability to find process by executable path*]             |                                                    |                                                |                                             |                                         |                                        |
| [Get ability to find process by executable metadata*]         |                                                    |                                                |                                             |                                         |                                        |
| [Get ability to find process by executable hash*]             |                                                    |                                                |                                             |                                         |                                        |
| [Get ability to find process by executable format*]           |                                                    |                                                |                                             |                                         |                                        |
| [Get ability to find process by executable content pattern*]  |                                                    |                                                |                                             |                                         |                                        |
| [Get ability to block process by executable path*]            |                                                    |                                                |                                             |                                         |                                        |
| [Get ability to block process by executable metadata*]        |                                                    |                                                |                                             |                                         |                                        |
| [Get ability to block process by executable hash*]            |                                                    |                                                |                                             |                                         |                                        |
| [Get ability to block process by executable format*]          |                                                    |                                                |                                             |                                         |                                        |
| [Get ability to block process by executable content pattern*] |                                                    |                                                |                                             |                                         |                                        |
| [Manage remote computer management system policies*]          |                                                    |                                                |                                             |                                         |                                        |
| [Get ability to list registry keys modified*]                 |                                                    |                                                |                                             |                                         |                                        |
| [Get ability to list registry keys deleted*]                  |                                                    |                                                |                                             |                                         |                                        |
| [Get ability to list registry keys accessed*]                 |                                                    |                                                |                                             |                                         |                                        |
| [Get ability to list registry keys created*]                  |                                                    |                                                |                                             |                                         |                                        |
| [Get ability to list services created*]                       |                                                    |                                                |                                             |                                         |                                        |
| [Get ability to list services modified*]                      |                                                    |                                                |                                             |                                         |                                        |
| [Get ability to list services deleted*]                       |                                                    |                                                |                                             |                                         |                                        |
| [Get ability to remove registry key*]                         |                                                    |                                                |                                             |                                         |                                        |
| [Get ability to remove service*]                              |                                                    |                                                |                                             |                                         |                                        |
| [Get ability to analyse registry key*]                        |                                                    |                                                |                                             |                                         |                                        |
| [Manage identity management system*]                          |                                                    |                                                |                                             |                                         |                                        |
| [Get ability to lock user account*]                           |                                                    |                                                |                                             |                                         |                                        |
| [Get ability to list users authenticated*]                    |                                                    |                                                |                                             |                                         |                                        |
| [Get ability to revoke authentication credentials*]           |                                                    |                                                |                                             |                                         |                                        |
| [Get ability to remove user account*]                         |                                                    |                                                |                                             |                                         |                                        |
|

<br>

[**Practice**]: Response_Actions/RA_1001_practice.md
[**Take trainings**]: Response_Actions/RA_1002_take_trainings.md
[**Raise personnel awareness**]: Response_Actions/RA_1003_raise_personnel_awareness.md
[**Make personnel report suspicious activity**]: Response_Actions/RA_1004_make_personnel_report_suspicious_activity.md
[Set up relevant data collection*]: https://github.com/atc-project/atc-react/issues/132
[Set up a centralized long-term log storage*]: https://github.com/atc-project/atc-react/issues/133
[Develop communication map*]: https://github.com/atc-project/atc-react/issues/134
[Make sure there are backups*]: https://github.com/atc-project/atc-react/issues/135
[Get network architecture map*]: https://github.com/atc-project/atc-react/issues/136
[Get access control matrix*]: https://github.com/atc-project/atc-react/issues/137
[Develop assets knowledge base*]: https://github.com/atc-project/atc-react/issues/138
[Check analysis toolset*]: https://github.com/atc-project/atc-react/issues/139
[Access vulnerability management system logs*]: https://github.com/atc-project/atc-react/issues/140
[**Connect with trusted communities**]: Response_Actions/RA_1014_connect_with_trusted_communities.md

[**Access external network flow logs**]: Response_Actions/RA_1101_access_external_network_flow_logs.md
[Access internal network flow logs*]: https://github.com/atc-project/atc-react/issues/141
[Access internal HTTP logs*]: https://github.com/atc-project/atc-react/issues/142
[**Access external HTTP logs**]: Response_Actions/RA_1104_access_external_http_logs.md
[Access internal DNS logs*]: https://github.com/atc-project/atc-react/issues/143
[**Access external DNS logs**]: Response_Actions/RA_1106_access_external_dns_logs.md
[Access VPN logs*]: https://github.com/atc-project/atc-react/issues/144
[Access DHCP logs*]: https://github.com/atc-project/atc-react/issues/145
[Access internal packet capture data*]: https://github.com/atc-project/atc-react/issues/146
[Access external packet capture data*]: https://github.com/atc-project/atc-react/issues/147
[**Get ability to block external IP address**]: Response_Actions/RA_1111_get_ability_to_block_external_ip_address.md
[Get ability to block internal IP address*]: https://github.com/atc-project/atc-react/issues/148
[**Get ability to block external domain**]: Response_Actions/RA_1113_get_ability_to_block_external_domain.md
[Get ability to block internal domain*]: https://github.com/atc-project/atc-react/issues/149
[**Get ability to block external URL**]: Response_Actions/RA_1115_get_ability_to_block_external_url.md
[Get ability to block internal URL*]: https://github.com/atc-project/atc-react/issues/150
[Get ability to block port external communication*]: https://github.com/atc-project/atc-react/issues/151
[Get ability to block port internal communication*]: https://github.com/atc-project/atc-react/issues/152
[Get ability to block user external communication*]: https://github.com/atc-project/atc-react/issues/153
[Get ability to block user internal communication*]: https://github.com/atc-project/atc-react/issues/154
[Get ability to find data transferred by content pattern*]: https://github.com/atc-project/atc-react/issues/155
[Get ability to analyse user-agent*]: https://github.com/atc-project/atc-react/issues/312
[Get ability to block data transferring by content pattern*]: https://github.com/atc-project/atc-react/issues/156
[Get ability to list data transferred*]: https://github.com/atc-project/atc-react/issues/157
[Get ability to collect transferred data*]: https://github.com/atc-project/atc-react/issues/158
[Get ability to identify transferred data*]: https://github.com/atc-project/atc-react/issues/159
[Find data transferred by content pattern*]: https://github.com/atc-project/atc-react/issues/160
[Analyse user-agent*]: https://github.com/atc-project/atc-react/issues/306
[**Get ability to list users opened email message**]: Response_Actions/RA_1201_get_ability_to_list_users_opened_email_message.md
[**Get ability to list email message receivers**]: Response_Actions/RA_1202_get_ability_to_list_email_message_receivers.md
[**Get ability to block email domain**]: Response_Actions/RA_1203_get_ability_to_block_email_domain.md
[**Get ability to block email sender**]: Response_Actions/RA_1204_get_ability_to_block_email_sender.md
[**Get ability to delete email message**]: Response_Actions/RA_1205_get_ability_to_delete_email_message.md
[**Get ability to quarantine email message**]: Response_Actions/RA_1206_get_ability_to_quarantine_email_message.md
[Get ability to collect email message*]: https://github.com/atc-project/atc-react/issues/161
[Get ability to analyse email address*]: https://github.com/atc-project/atc-react/issues/313
[Get ability to list files created*]: https://github.com/atc-project/atc-react/issues/162
[Get ability to list files modified*]: https://github.com/atc-project/atc-react/issues/163
[Get ability to list files deleted*]: https://github.com/atc-project/atc-react/issues/164
[Get ability to list files downloaded*]: https://github.com/atc-project/atc-react/issues/165
[Get ability to list files with tampered timestamps*]: https://github.com/atc-project/atc-react/issues/166
[Get ability to find file by path*]: https://github.com/atc-project/atc-react/issues/167
[Get ability to find file by metadata*]: https://github.com/atc-project/atc-react/issues/168
[Get ability to find file by hash*]: https://github.com/atc-project/atc-react/issues/169
[Get ability to find file by format*]: https://github.com/atc-project/atc-react/issues/170
[Get ability to find file by content pattern*]: https://github.com/atc-project/atc-react/issues/171
[Get ability to collect file*]: https://github.com/atc-project/atc-react/issues/172
[Get ability to quarantine file by path*]: https://github.com/atc-project/atc-react/issues/173
[Get ability to quarantine file by hash*]: https://github.com/atc-project/atc-react/issues/174
[Get ability to quarantine file by format*]: https://github.com/atc-project/atc-react/issues/175
[Get ability to quarantine file by content pattern*]: https://github.com/atc-project/atc-react/issues/176
[Get ability to remove file*]: https://github.com/atc-project/atc-react/issues/177
[Get ability to analyse file hash*]: https://github.com/atc-project/atc-react/issues/267
[Get ability to analyse windows pe*]: https://github.com/atc-project/atc-react/issues/268
[Get ability to analyse macos macho*]: https://github.com/atc-project/atc-react/issues/269
[Get ability to analyse unix elf*]: https://github.com/atc-project/atc-react/issues/270
[Get ability to analyse ms office file*]: https://github.com/atc-project/atc-react/issues/271
[Get ability to analyse pdf file*]: https://github.com/atc-project/atc-react/issues/272
[Get ability to analyse script*]: https://github.com/atc-project/atc-react/issues/273
[Get ability to analyse jar*]: https://github.com/atc-project/atc-react/issues/314
[Get ability to analyse filename*]: https://github.com/atc-project/atc-react/issues/315
[Get ability to list processes executed*]: https://github.com/atc-project/atc-react/issues/178
[Get ability to find process by executable path*]: https://github.com/atc-project/atc-react/issues/179
[Get ability to find process by executable metadata*]: https://github.com/atc-project/atc-react/issues/180
[Get ability to find process by executable hash*]: https://github.com/atc-project/atc-react/issues/181
[Get ability to find process by executable format*]: https://github.com/atc-project/atc-react/issues/182
[Get ability to find process by executable content pattern*]: https://github.com/atc-project/atc-react/issues/183
[Get ability to block process by executable path*]: https://github.com/atc-project/atc-react/issues/184
[Get ability to block process by executable metadata*]: https://github.com/atc-project/atc-react/issues/185
[Get ability to block process by executable hash*]: https://github.com/atc-project/atc-react/issues/186
[Get ability to block process by executable format*]: https://github.com/atc-project/atc-react/issues/187
[Get ability to block process by executable content pattern*]: https://github.com/atc-project/atc-react/issues/188
[Manage remote computer management system policies*]: https://github.com/atc-project/atc-react/issues/189
[Get ability to list registry keys modified*]: https://github.com/atc-project/atc-react/issues/190
[Get ability to list registry keys deleted*]: https://github.com/atc-project/atc-react/issues/191
[Get ability to list registry keys accessed*]: https://github.com/atc-project/atc-react/issues/192
[Get ability to list registry keys created*]: https://github.com/atc-project/atc-react/issues/193
[Get ability to list services created*]: https://github.com/atc-project/atc-react/issues/194
[Get ability to list services modified*]: https://github.com/atc-project/atc-react/issues/195
[Get ability to list services deleted*]: https://github.com/atc-project/atc-react/issues/196
[Get ability to remove registry key*]: https://github.com/atc-project/atc-react/issues/197
[Get ability to remove service*]: https://github.com/atc-project/atc-react/issues/198
[Get ability to analyse registry key*]: https://github.com/atc-project/atc-react/issues/316
[Manage identity management system*]: https://github.com/atc-project/atc-react/issues/199
[Get ability to lock user account*]: https://github.com/atc-project/atc-react/issues/200
[Get ability to list users authenticated*]: https://github.com/atc-project/atc-react/issues/201
[Get ability to revoke authentication credentials*]: https://github.com/atc-project/atc-react/issues/202
[Get ability to remove user account*]: https://github.com/atc-project/atc-react/issues/203

[List victims of security alert*]: https://github.com/atc-project/atc-react/issues/49
[List host vulnerabilities*]: https://github.com/atc-project/atc-react/issues/204
[**Put compromised accounts on monitoring**]: Response_Actions/RA_2003_put_compromised_accounts_on_monitoring.md
[List hosts communicated with internal domain*]: https://github.com/atc-project/atc-react/issues/45
[List hosts communicated with internal IP*]: https://github.com/atc-project/atc-react/issues/46
[List hosts communicated with internal URL*]: https://github.com/atc-project/atc-react/issues/47
[Analyse domain name*]: https://github.com/atc-project/atc-react/issues/31
[Analyse IP*]: https://github.com/atc-project/atc-react/issues/40
[Analyse URI*]: https://github.com/atc-project/atc-react/issues/32
[List hosts communicated by port*]: https://github.com/atc-project/atc-react/issues/205
[List hosts connected to VPN*]: https://github.com/atc-project/atc-react/issues/206
[List hosts connected to intranet*]: https://github.com/atc-project/atc-react/issues/207
[List data transferred*]: https://github.com/atc-project/atc-react/issues/208
[Collect transferred data*]: https://github.com/atc-project/atc-react/issues/209
[Identify transferred data*]: https://github.com/atc-project/atc-react/issues/210
[**List hosts communicated with external domain**]: Response_Actions/RA_2113_list_hosts_communicated_with_external_domain.md
[**List hosts communicated with external IP**]: Response_Actions/RA_2114_list_hosts_communicated_with_external_ip.md
[**List hosts communicated with external URL**]: Response_Actions/RA_2115_list_hosts_communicated_with_external_url.md
[Find data transferred by content pattern*]: https://github.com/atc-project/atc-react/issues/211
[**List users opened email message**]: Response_Actions/RA_2201_list_users_opened_email_message.md
[**Collect email message**]: Response_Actions/RA_2202_collect_email_message.md
[**List email message receivers**]: Response_Actions/RA_2203_list_email_message_receivers.md
[**Make sure email message is phishing**]: Response_Actions/RA_2204_make_sure_email_message_is_phishing.md
[**Extract observables from email message**]: Response_Actions/RA_2205_extract_observables_from_email_message.md
[Analyse email address*]: https://github.com/atc-project/atc-react/issues/307
[List files created*]: https://github.com/atc-project/atc-react/issues/48
[List files modified*]: https://github.com/atc-project/atc-react/issues/212
[List files deleted*]: https://github.com/atc-project/atc-react/issues/213
[List files downloaded*]: https://github.com/atc-project/atc-react/issues/214
[List files with tampered timestamps*]: https://github.com/atc-project/atc-react/issues/215
[Find file by path*]: https://github.com/atc-project/atc-react/issues/216
[Find file by metadata*]: https://github.com/atc-project/atc-react/issues/217
[Find file by hash*]: https://github.com/atc-project/atc-react/issues/218
[Find file by format*]: https://github.com/atc-project/atc-react/issues/219
[Find file by content pattern*]: https://github.com/atc-project/atc-react/issues/220
[Collect file*]: https://github.com/atc-project/atc-react/issues/221
[Analyse file hash*]: https://github.com/atc-project/atc-react/issues/39
[Analyse Windows PE*]: https://github.com/atc-project/atc-react/issues/33
[Analyse macos macho*]: https://github.com/atc-project/atc-react/issues/41
[Analyse Unix ELF*]: https://github.com/atc-project/atc-react/issues/44
[Analyse MS office file*]: https://github.com/atc-project/atc-react/issues/42
[Analyse PDF file*]: https://github.com/atc-project/atc-react/issues/43

[Analyse script*]: https://github.com/atc-project/atc-react/issues/274
[Analyse jar*]: https://github.com/atc-project/atc-react/issues/308
[Analyse filename*]: https://github.com/atc-project/atc-react/issues/309
[List processes executed*]: https://github.com/atc-project/atc-react/issues/34
[Find process by executable path*]: https://github.com/atc-project/atc-react/issues/222
[Find process by executable metadata*]: https://github.com/atc-project/atc-react/issues/223
[Find process by executable hash*]: https://github.com/atc-project/atc-react/issues/224
[Find process by executable format*]: https://github.com/atc-project/atc-react/issues/225
[Find process by executable content pattern*]: https://github.com/atc-project/atc-react/issues/226
[List registry keys modified*]: https://github.com/atc-project/atc-react/issues/37
[List registry keys deleted*]: https://github.com/atc-project/atc-react/issues/227
[List registry keys accessed*]: https://github.com/atc-project/atc-react/issues/228
[List registry keys created*]: https://github.com/atc-project/atc-react/issues/229
[List services created*]: https://github.com/atc-project/atc-react/issues/230
[List services modified*]: https://github.com/atc-project/atc-react/issues/231
[List services deleted*]: https://github.com/atc-project/atc-react/issues/232
[Analyse registry key*]: https://github.com/atc-project/atc-react/issues/310
[List users authenticated*]: https://github.com/atc-project/atc-react/issues/233

[Patch vulnerability*]: https://github.com/atc-project/atc-react/issues/234
[**Block external IP address**]: Response_Actions/RA_3101_block_external_ip_address.md
[**Block internal IP address**]: Response_Actions/RA_3102_block_internal_ip_address.md
[**Block external domain**]: Response_Actions/RA_3103_block_external_domain.md
[**Block internal domain**]: Response_Actions/RA_3104_block_internal_domain.md
[**Block external URL**]: Response_Actions/RA_3105_block_external_url.md
[**Block internal URL**]: Response_Actions/RA_3106_block_internal_url.md
[**Block port external communication**]: Response_Actions/RA_3107_block_port_external_communication.md
[**Block port internal communication**]: Response_Actions/RA_3108_block_port_internal_communication.md
[**Block user external communication**]: Response_Actions/RA_3109_block_user_external_communication.md
[**Block user internal communication**]: Response_Actions/RA_3110_block_user_internal_communication.md
[Block data transferring by content pattern*]: https://github.com/atc-project/atc-react/issues/235
[**Block domain on email**]: Response_Actions/RA_3201_block_domain_on_email.md
[**Block sender on email**]: Response_Actions/RA_3202_block_sender_on_email.md
[**Quarantine email message**]: Response_Actions/RA_3203_quarantine_email_message.md
[Quarantine file by format*]: https://github.com/atc-project/atc-react/issues/236
[Quarantine file by hash*]: https://github.com/atc-project/atc-react/issues/237
[Quarantine file by path*]: https://github.com/atc-project/atc-react/issues/238
[Quarantine file by content pattern*]: https://github.com/atc-project/atc-react/issues/239
[Block process by executable path*]: https://github.com/atc-project/atc-react/issues/240
[Block process by executable metadata*]: https://github.com/atc-project/atc-react/issues/241
[Block process by executable hash*]: https://github.com/atc-project/atc-react/issues/242
[Block process by executable format*]: https://github.com/atc-project/atc-react/issues/243
[Block process by executable content pattern*]: https://github.com/atc-project/atc-react/issues/244
[Disable system service*]: https://github.com/atc-project/atc-react/issues/245
[Lock user account*]: https://github.com/atc-project/atc-react/issues/246

[**Report incident to external companies**]: Response_Actions/RA_4001_report_incident_to_external_companies.md
[Remove rogue network device*]: https://github.com/atc-project/atc-react/issues/247
[**Delete email message**]: Response_Actions/RA_4201_delete_email_message.md
[Remove file*]: https://github.com/atc-project/atc-react/issues/248
[Remove registry key*]: https://github.com/atc-project/atc-react/issues/249
[Remove service*]: https://github.com/atc-project/atc-react/issues/250
[**Revoke authentication credentials**]: Response_Actions/RA_4601_revoke_authentication_credentials.md
[Remove user account*]: https://github.com/atc-project/atc-react/issues/251

[Reinstall host from golden image*]: https://github.com/atc-project/atc-react/issues/38
[Restore data from backup*]: https://github.com/atc-project/atc-react/issues/252
[**Unblock blocked IP**]: Response_Actions/RA_5101_unblock_blocked_ip.md
[**Unblock blocked domain**]: Response_Actions/RA_5102_unblock_blocked_domain.md
[**Unblock blocked URL**]: Response_Actions/RA_5103_unblock_blocked_url.md
[Unblock blocked port*]: https://github.com/atc-project/atc-react/issues/253
[Unblock blocked user*]: https://github.com/atc-project/atc-react/issues/254
[**Unblock domain on email**]: Response_Actions/RA_5201_unblock_domain_on_email.md
[**Unblock sender on email**]: Response_Actions/RA_5202_unblock_sender_on_email.md
[**Restore quarantined email message**]: Response_Actions/RA_5203_restore_quarantined_email_message.md
[Restore quarantined file*]: https://github.com/atc-project/atc-react/issues/255
[Unblock blocked process*]: https://github.com/atc-project/atc-react/issues/256
[Enable disabled service*]: https://github.com/atc-project/atc-react/issues/257
[Unlock locked user account*]: https://github.com/atc-project/atc-react/issues/258

[**Develop incident report**]: Response_Actions/RA_6001_develop_incident_report.md
[**Conduct lessons learned exercise**]: Response_Actions/RA_6002_conduct_lessons_learned_exercise.md

Действия Реагирования (Response Actions), отмеченные символом "*", являются пустыми файлами, содержащими только название и краткое описание.  
Они созданы для того, чтобы описать направление, в котором RE&CT будет развиваться.  
Ссылки ведут к GitHub issues по их разработке, в которой вы можете принять участие.  

## Действенная Аналитика

Проект ATC RE&CT наследует парадигму "Действенная Аналитика" от проекта [ATC](https://github.com/atc-project/atomic-threat-coverage).  
Это означает, что аналитика:  

- **человекочитаемая** (`.md`) для распространения/использования в ходе операционной деятельности  
- **машиночитаемая** (`.yml`) для автоматизированной обработки/интеграций  
- **исполняемая** платформой для реагирования на инциденты (Incident Response Platform, IRP). На данный момент поддерживается генерация шаблонов кейсов для IRP [TheHive](https://github.com/atc-project/atc-react/tree/master/docs/thehive_templates)  

Проще говоря, аналитика хранится в формате `.yml` файлов, автоматически конвертируется в документы в формате `.md` (посредством [jinja](https://palletsprojects.com/p/jinja/)) и `.json` файлы шаблонов кейсов TheHive.  
Для получения информации по кастомизации и использованию, обращайтесь к разделу [usage](https://github.com/atc-project/atc-react#usage) в README проекта.  

### Response Action

Response Action (Действие Реагирования) — это описание специфичной атомарной процедуры/задачи, которая должна быть выполнена в ходе реагирования на инцидент. Это первостепенный объект, используемый для составления Сценариев Реагирования (Response Playbooks).  
Каждое Действие Реагирования связано с конкретной [Стадией Реагирования](responsestages.md).  

Первая цифра идентификатора Действия Реагирования отражает Стадию, к которой это Действие относится:

- **1**: Подготовка (Preparation)
- **2**: Идентификация (Identification)
- **3**: Сдерживание (Containment)
- **4**: Ликвидация (Eradication)
- **5**: Восстановление (Recovery)
- **6**: Выводы (Lessons Learned)

Вторая цифра идентификатора Действия Реагирования отражает Категорию, к которой это Действие относится:

- **0**: Общее (General)
- **1**: Сеть (Network)
- **2**: Электронная почта (Email)
- **3**: Файл (File)
- **4**: Процесс (Process)
- **5**: Конфигурация (Configuration)
- **6**: Идентификационные данные (Identity)

Таким образом, посредством идентификатора Действия Реагирования, можно определить Стадию и Категорию, к которым это Действие принадлежит.
Например [RA**22**02: Collect an email message](Response_Actions/RA_2202_collect_email_message.md) относится к Стадии **2** (Идентификация) и Категории **2** (Электронная почта).

Категоризация предназначена для расширения возможностей для оценки зрелости и планирования развития процесса реагирования на инциденты.  

### Response Playbook

Response Playbook (Сценарий Реагирования) — это план, который представляет собой законченный список задач/процедур (Действий Реагирования) которые должны быть выполнены в ходе реагирования на конкретную угрозу с опциональным маппингом к фреймворкам [MITRE ATT&CK](https://attack.mitre.org/) или [Misinfosec AMITT](https://github.com/misinfosecproject/amitt_framework).

Сценарий Реагирования может включать в себя описание хода работ, особых условий/требований, детали по последовательности исполнения Действий Реагирования, или любую другую релевантную информацию.

### TheHive Case Templates

Шаблоны кейсов платформы реагирования на инциденты TheHive генерируются на основе Сценариев Реагирования.  
Каждая отдельная задача в шаблоне кейса — это отдельное Действие Реагирования (с его полным описанием).  

Вот пример импортированного шаблона кейса TheHive:

<details>
  <summary>Импортированный шаблон кейса TheHive, созданный на основе Сценария Реагирования (кликните, чтобы раскрыть)</summary>
  <img src="../images/thehive_case_template_v1.png" />
</details>

<details>
  <summary>Одна из задач в кейсе TheHive, созданная на основе Действия Реагирования (кликните, чтобы раскрыть)</summary>
  <img src="../images/thehive_case_task_v1.png" />
</details>
<br>
Шаблоны кейсов TheHive хранятся в директории `docs/thehive_templates` и могут быть импортированы в TheHive через его веб-интерфейс.

## Контакты

- Следите за обновлениями в [Twitter](https://twitter.com/atc_project)
- Присоединяйтесь к обсуждению в [Slack](https://join.slack.com/t/atomicthreatcoverage/shared_invite/zt-6ropl01z-wIdiq3M0AEZPj_HiKfbiBg) или [Telegram](https://t.me/atomic_threat_coverage) 

## Контрибьюторы

- Тимур Зиннятуллин, [@zinint](https://twitter.com/zinint)  
- Даниил Светлов, [@Mr_4nders0n](https://twitter.com/Mr_4nders0n)  
- Андреас Ханкелер, [@Karneades](https://github.com/Karneades)
- Патрик Эбрэхам, [@pjabes](https://github.com/pjabes)
- Лукас Берези, [@lberezy](https://github.com/lberezy)
- Эфе Эрдур, [@efeerdur](https://github.com/efeerdur)
- Алехандро Ортуно, [@aomanzanera](https://twitter.com/aomanzanera)  
- [@d3anp](https://github.com/d3anp)  
- Кристоф Ботт, [@xofolowski](https://github.com/xofolowski)  

Вы хотели бы внести свой вклад в проект и тоже стать участником? Инструкция [CONTRIBUTING](https://github.com/atc-project/atc-react/blob/master/CONTRIBUTING.md) поможет начать.  

## План развития

План развития проекта и соответствующие обсуждения можно найти в [issues](https://github.com/atc-project/atc-react/issues) посредством лейблов:

- [Обсуждения](https://github.com/atc-project/atc-react/issues?q=is%3Aissue+is%3Aopen+label%3Adiscussion)
- [Вопросы](https://github.com/atc-project/atc-react/issues?q=is%3Aissue+is%3Aopen+label%3Aquestion)
- [Улучшения](https://github.com/atc-project/atc-react/issues?q=is%3Aissue+is%3Aopen+label%3Aenhancement)
- [Разработка Действий Реагирования](https://github.com/atc-project/atc-react/issues?q=is%3Aissue+is%3Aopen+label%3ARA-dev)

## Лицензия

Лицензия доступна к просмотру по [ссылке](https://github.com/atc-project/atc-react/blob/master/LICENSE).
