#!/usr/bin/env python3

import yaml
import re
import warnings
import requests
import html
import json

from os import listdir
from os.path import isfile, join
from yaml.scanner import ScannerError
from requests.auth import HTTPBasicAuth

# ########################################################################### #
# ############################### REACTutils ################################ #
# ########################################################################### #

# Default configuration file path
DEFAULT_PROJECT_CONFIG_PATH = 'scripts/config.default.yml'
DEFAULT_CONFIG_PATH = 'config.yml'

# Show warnings only once:
with warnings.catch_warnings():
    warnings.simplefilter("once")


class REACTConfig(object):
    """Class for handling the project configuration"""

    def __init__(self, path='config.yml'):
        """Constructor that will return an REACTconfig object holding
        the project configuration

        Keyword Arguments:
            path {str} -- 'Path of the local configuration file' (default: {'config.yml'})
        """

        self.config_local = path
        self.config_project = DEFAULT_PROJECT_CONFIG_PATH

    def get_config_project(self):
        """Get the configuration as defined by the project

        Returns:
            config {dict} -- Dictionary object containing configuration,
                             as set in the project configuration.
        """

        return self.__config_project

    def get_config_local(self):
        """Get the configuartion that is defined locally,
only contains local overrides and additions.

        Returns:
            config {dict} -- Dictionary object containing local configuration, 
                             containing only overrides and additions.
        """

        return self.__config_local

    @property
    def config(self):
        """Get the whole configuration including local settings and additions. 
This the configuation that is used by the application.

        Returns:
            config {dict} -- Dictionary object containing default settings, overriden by local settings if set.
        """

        config_final = dict(self.config_project)
        config_final.update(self.config_local)
        return config_final

    def set_config_project(self, path):
        """Set the project configuration via file path

        Arguments:
            path {str} -- File location of the config (yaml)
        """

        self.__config_project = dict(self.__read_yaml_file(path))

    def set_config_local(self, path):
        """Set the local configration via file path.
This will override project defaults in the final configuration.
If no local configuration is found on the argument path, a warning will be shown, and only default config is used.


        Arguments:
            path {str} -- Local config file location
        """

        try:
            self.__config_local = dict(self.__read_yaml_file(path))
        except FileNotFoundError:
            wrn = "Local config '{path}' not found, using project default"
            # Warning will show because it is in Exception block.
            warnings.warn(wrn.format(path=path))
            self.__config_local = {}

    def __read_yaml_file(self, path):
        """Open the yaml file and load it to the variable.
        Return created list"""
        with open(path) as f:
            yaml_fields = yaml.load_all(f.read(), Loader=yaml.FullLoader)

        buff_results = [x for x in yaml_fields]
        if len(buff_results) > 1:
            result = buff_results[0]
            result['additions'] = buff_results[1:]
        else:
            result = buff_results[0]

        return result

    def get(self, key):
        """ Maps to 'get' Function of configuration {dict} object """
        return self.config.get(key)

    config_local = property(get_config_local, set_config_local)
    config_project = property(get_config_project, set_config_project)


# Initialize global config
REACTconfig = REACTConfig()


class REACTutils:
    """Class which consists of handful methods used throughout the project"""

    def __init__(self):
        """Init method"""
        pass

    @staticmethod
    def read_rule_file(path):
        """Open the file and load it to the variable. Return text"""

        with open(path) as f:
            rule_text = f.read()

        return rule_text

    @staticmethod
    def load_yamls_with_paths(path):
        yamls = [join(path, f) for f in listdir(path) if isfile(
            join(path, f)) if f.endswith('.yaml') or f.endswith('.yml')]
        result = []
        for yaml in yamls:
            try:
                result.append(REACTutils.read_yaml_file(yaml))
            except ScannerError:
                raise ScannerError('yaml is bad! %s' % yaml)
        return (result, yamls)

    @staticmethod
    def read_yaml_file(path):
        """Open the yaml file and load it to the variable.
        Return created list"""
        if path == 'config.yml':
            wrn = "Use 'load_config' or 'REACTConfig' instead for config"
            # Warning will not show,
            # unless captured by logging facility or python called with -Wd
            warnings.warn(message=wrn,
                          category=DeprecationWarning)
            return REACTConfig(path).config

        with open(path) as f:
            yaml_fields = yaml.load_all(f.read(), Loader=yaml.FullLoader)

        buff_results = [x for x in yaml_fields]
        if len(buff_results) > 1:
            result = buff_results[0]
            result['additions'] = buff_results[1:]
        else:
            result = buff_results[0]
        return result

    @staticmethod
    def load_config(path):
        """Load the configuration YAML files used ofr ATC into a dictionary 

        Arguments:
            path {filepath} -- File path of the local configuration file

        Returns:
            dict -- Configuration for ATC in dictionary format
        """

        return REACTConfig(path).config

    @staticmethod
    def load_yamls(path):
        """Load multiple yamls into list"""

        yamls = [
            join(path, f) for f in listdir(path)
            if isfile(join(path, f))
            if f.endswith('.yaml')
            or f.endswith('.yml')
        ]

        result = []

        for yaml in yamls:
            try:
                result.append(REACTutils.read_yaml_file(yaml))

            except ScannerError:
                raise ScannerError('yaml is bad! %s' % yaml)

        return result

    @staticmethod
    def write_file(path, content, options="w+"):
        """Simple method for writing content to some file"""

        with open(path, options) as file:
            file.write(content)

        return True

    @staticmethod
    def confluence_get_page_id(apipath, auth, space, title):
        """Get confluence page ID based on title and space"""

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        url = apipath + "content"
        space_page_url = url + '?spaceKey=' + space + '&title=' \
            + title + '&expand=space'

        response = requests.request(
            "GET",
            space_page_url,
            headers=headers,
            auth=auth
        )

        if response.status_code == 401:
            print("Unauthorized Response. Try to use a token instead of a password. " +
                  "Follow the guideline for more info: \n" +
                  "https://developer.atlassian.com/cloud/confluence/basic-auth-" +
                  "for-rest-apis/#supplying-basic-auth-headers")
            exit()
        else:
            response = response.json()

        # Check if response contains proper information and return it if so
        if response.get('results'):
            if isinstance(response['results'], list):
                if response['results'][0].get('id'):
                    return response['results'][0][u'id']

        # If page not found
        return None


    @staticmethod
    def push_to_confluence(data, apipath, auth):
        """Description"""

        apipath = apipath if apipath[-1] == '/' else apipath + '/'

        url = apipath + "content"

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        alldata = True
        for i in ["title", "spacekey", "parentid", "confluencecontent"]:
            if i not in data.keys():
                alldata = False
        if not alldata:
            raise Exception("Not all data were provided in order " +
                            "to push the content to confluence")

        dict_payload = {
            "title": "%s" % data["title"],  # req
            "type": "page",  # req
            "space": {  # req
                "key": "%s" % data["spacekey"]
            },
            "status": "current",
            "ancestors": [
                {
                    "id": "%s" % data["parentid"]  # parent id
                }
            ],
            "body": {  # req
                "storage": {
                    "value": "%s" % data["confluencecontent"],
                    "representation": "storage"
                }
            }
        }
        payload = json.dumps(dict_payload)

        response = requests.request(
            "POST",
            url,
            data=payload,
            headers=headers,
            auth=auth
        )

        resp = json.loads(response.text)
        if "data" in resp.keys():
            if "successful" in resp["data"].keys() \
                    and bool(resp["data"]["successful"]):
                return "Page created"
            else:
                cid = REACTutils.confluence_get_page_id(
                    apipath, auth, data["spacekey"],
                    data["title"]
                )

            response = requests.request(
                "GET",
                url + "/%s?expand=body.storage,version" % str(cid),
                data=payload,
                headers=headers,
                auth=auth
            )

            resp = json.loads(response.text)

            current_content = resp["body"]["storage"]["value"]

            #if current_content == data["confluencecontent"]:
            # compare pages: revert changes in confluence page, remove \n \r \t \s
            conv = {
                '<ac:structured-macro ac:name="markdown"[^>]*>': '<ac:structured-macro ac:name="markdown">',
                '<ac:structured-macro ac:name="expand"[^>]*>': '<ac:structured-macroac:name="expand">',
                '<ac:structured-macro ac:name="code"[^>]*>': '<ac:structured-macroac:name="code">',
                'â€™': '’', 
                'Ä€': 'Ā', 
                '\n': '',
                '\r': '',
                '\t': '',
                ' ': ''
            }
            curr = html.unescape(current_content)
            new = html.unescape(data["confluencecontent"])
            for str_from, str_to in conv.items():
                curr = re.sub(str_from, str_to, curr)
                new = re.sub(str_from, str_to, new)

            if curr == new:
                return "No update required"

            try:
                i = int(resp["version"]["number"]) + 1
                dict_payload["version"] = {"number": i}
                payload = json.dumps(dict_payload)

                response = requests.request(
                    "PUT",
                    url + "/%s" % str(cid),
                    data=payload,
                    headers=headers,
                    auth=auth
                )

                return "Page updated"
            except KeyError:
                response = requests.request(
                    "GET",
                    url + "/%s/" % str(cid),
                    data=payload,
                    headers=headers,
                    auth=auth
                )

                resp = json.loads(response.text)
                try:
                    resp["version"]["number"] += 1

                    dict_payload["version"] = resp["version"]
                    payload = json.dumps(dict_payload)

                    response = requests.request(
                        "PUT",
                        url + "/%s" % str(cid),
                        data=payload,
                        headers=headers,
                        auth=auth
                    )

                    return "Page updated"

                except BaseException:
                    return "Page update failed"
        elif "status" in resp.keys():
            if resp["status"] == "current":
                return "Page created"

        return None


    @staticmethod
    def normalize_react_title(title):
        """Normalize title if it is a RA/RP title in the following format:
        RP_0003_identification_make_sure_email_is_a_phishing
        """
        
        react_id_re = re.compile(r'R[AP]_\d{4}.*$')
        if react_id_re.match(title):
            title = title[8:].split('_', 0)[-1].replace('_', ' ').capitalize()
            new_title = ""
            for word in title.split():
                if word.lower() in [
                        "ip", "dns", "ms", "ngfw", "ips", "url", "pe", "pdf", 
                        "elf", "dhcp", "vpn", "smb", "ftp", "http" ]:
                    new_title += word.upper()
                    new_title += " "
                    continue
                elif word.lower() in [ "unix", "windows", "proxy", "firewall", "mach-o" ]:
                    new_title += word.capitalize()
                    new_title += " "
                    continue
                new_title += word
                new_title += " "
            return new_title.strip()
        return title

    @staticmethod
    def get_ra_category(ra_id):
        """Get a Response Action category, i.e. file, network, email, etc
        Using the the RA ID
        """
        categories = {
          "General": 0,
          "Network": 1,
          "Email": 2,
          "File": 3,
          "Process": 4,
          "Configuration": 5,
          "Identity": 6,
        }

        for name, number in categories.items():
            category_re = re.compile(r'RA\d{1}' + str(number) + '.*$')
            if category_re.match(ra_id):
                return name

        return "N/A"

    @staticmethod
    def normalize_rs_name(rs_name):
        """Revieve a Response Stage name, i.e. reparation, lessons_learned, etc
        Return normalized RS name
        """

        stages = {
          "preparation": "Preparation",
          "identification": "Identification",
          "containment": "Containment",
          "eradication": "Eradication",
          "recovery": "Recovery",
          "lessons_learned": "Lessons Learned"
        }

        for stage_name, normal_stage_name in stages.items():
            if rs_name == stage_name:
                return normal_stage_name

        return "N/A"
