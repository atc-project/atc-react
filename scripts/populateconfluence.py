#!/usr/bin/env python3

import glob
import sys
import traceback
import os
from jinja2 import Environment, FileSystemLoader

# Import ATC classes
try:
    from scripts.reactutils import REACTutils
    from scripts.responseaction import ResponseAction
    from scripts.responseplaybook import ResponsePlaybook
    from scripts.responsestage import ResponseStage
    from scripts.init_confluence import main as init_main
    env = Environment(loader=FileSystemLoader('scripts/templates'))
except:
    from response.atc_react.scripts.reactutils import REACTutils
    from response.atc_react.scripts.responseaction import ResponseAction
    from response.atc_react.scripts.responseplaybook import ResponsePlaybook
    from response.atc_react.scripts.responsestage import ResponseStage
    from response.atc_react.scripts.init_confluence import main as init_main
    env = Environment(loader=FileSystemLoader(
        'response/atc_react/scripts/templates'))


REACTConfig = REACTutils.load_config("config.yml")


class ReactPopulateConfluence:
    """Desc"""

    def __init__(self, auth, ra=False, rp=False, rs=False,
                 auto=False, ra_path=False,
                 rp_path=False, rs_path=False, init=False):
        
        """Desc"""

        self.auth = auth
        self.space = REACTConfig.get('confluence_space_name')
        self.apipath = REACTConfig.get('confluence_rest_api_url')
        self.root_name = REACTConfig.get('confluence_name_of_root_directory')

        # Check if init switch is used
        if init:
            if init_main(self.auth):
                print("[+] Created initial confluence pages successfully")
            else:
                print("[-] Failed to create initial confluence pages")
                raise Exception("Failed to init pages")

        # Main logic
        if auto:
            self.response_stage(rs_path)
            self.response_action(ra_path)
            self.response_playbook(rp_path)
            self.response_stage(rs_path)

        if ra:
            self.response_action(ra_path)

        if rp:
            self.response_playbook(rp_path)

        if rs:
            self.response_stage(rs_path)

    def response_action(self, ra_path):
        """Nothing here yet"""

        print("[*] Populating Response Actions...")
        if ra_path:
            ra_list = glob.glob(ra_path + '*.yml')
        else:
            ra_dir = REACTConfig.get('response_actions_dir')
            ra_list = glob.glob(ra_dir + '/*.yml')

        for ra_file in ra_list:
            try:
                ra = ResponseAction(ra_file, apipath=self.apipath,
                                    auth=self.auth, space=self.space)
                ra.render_template("confluence")

                confluence_data = {
                    "title": ra.ra_parsed_file['title'],
                    "spacekey": self.space,
                    "parentid": str(REACTutils.confluence_get_page_id(
                        self.apipath, self.auth, self.space,
                        "Response Actions")), "confluencecontent": ra.content,
                }

                res = REACTutils.push_to_confluence(
                    confluence_data, self.apipath, self.auth)
                if res == 'Page updated':
                    print("==> updated page: RA '" +
                          ra.ra_parsed_file['title'] + "'")
                # print("Done: ", ra.ra_parsed_file['title'])
            except Exception as err:
                print(ra_file + " failed")
                print("Err message: %s" % err)
                print('-' * 60)
                traceback.print_exc(file=sys.stdout)
                print('-' * 60)

        print("[+] Response Actions populated!")

    def response_playbook(self, rp_path):
        """Nothing here yet"""

        print("[*] Populating Response Playbooks...")
        if rp_path:
            rp_list = glob.glob(rp_path + '*.yml')
        else:
            rp_dir = REACTConfig.get('response_playbooks_dir')
            rp_list = glob.glob(rp_dir + '/*.yml')

        for rp_file in rp_list:
            try:
                rp = ResponsePlaybook(rp_file, apipath=self.apipath,
                                      auth=self.auth, space=self.space)
                rp.render_template("confluence")

                base = os.path.basename(rp_file)

                confluence_data = {
                    "title": rp.rp_parsed_file['title'],
                    "spacekey": self.space,
                    "parentid": str(REACTutils.confluence_get_page_id(
                        self.apipath, self.auth, self.space,
                        "Response Playbooks")),
                    "confluencecontent": rp.content,
                }

                res = REACTutils.push_to_confluence(confluence_data, self.apipath,
                                                  self.auth)
                if res == 'Page updated':
                    print("==> updated page: RP '" + base + "'")
                # print("Done: ", rp.rp_parsed_file['title'])
            except Exception as err:
                print(rp_file + " failed")
                print("Err message: %s" % err)
                print('-' * 60)
                traceback.print_exc(file=sys.stdout)
                print('-' * 60)
        print("[+] Response Playbooks populated!")

    def response_stage(self, rs_path):
        """Nothing here yet"""

        print("[*] Populating Response Stages...")
        if rs_path:
            rs_list = glob.glob(rs_path + '*.yml')
        else:
            rs_dir = REACTConfig.get('response_stages_dir')
            rs_list = glob.glob(rs_dir + '/*.yml')

        for rs_file in rs_list:
            try:
                rs = ResponseStage(rs_file, apipath=self.apipath,
                                   auth=self.auth, space=self.space)
                rs.render_template("confluence")

                base = os.path.basename(rs_file)

                confluence_data = {
                    "title": rs.rs_parsed_file['title'],
                    "spacekey": self.space,
                    "parentid": str(REACTutils.confluence_get_page_id(
                        self.apipath, self.auth, self.space,
                        "Response Stages")),
                    "confluencecontent": rs.content,
                }

                res = REACTutils.push_to_confluence(confluence_data, self.apipath,
                                                  self.auth)
                if res == 'Page updated':
                    print("==> updated page: RS '" + base + "'")
            except Exception as err:
                print(rs_file + " failed")
                print("Err message: %s" % err)
                print('-' * 60)
                traceback.print_exc(file=sys.stdout)
                print('-' * 60)

        #
        # Populate Response Stages root page 
        #

        template = env.get_template(
            'confluence_responsestage_main_template.html.j2'
        )

        rss, rs_paths = REACTutils.load_yamls_with_paths(REACTConfig.get('response_stages_dir'))

        rss_dict = {}
        rss_list = []

        for i in range(len(rss)):
            rs_id = rss[i].get('id')
            rs_title = rss[i].get('title')
            rs_confluence_page_name = rs_id + ": " + rs_title
            rs_confluence_page_id = str(REACTutils.confluence_get_page_id(
                            self.apipath, self.auth, self.space, rs_confluence_page_name)
                        )
            rs_description = rss[i].get('description')

            rss_list.append((rs_id, rs_title, rs_description, rs_confluence_page_id))

        rss_dict.update({'rss_list': sorted(rss_list)})
        rss_dict.update({'confluence_viewpage_url': REACTConfig.get('confluence_viewpage_url')})

        content = template.render(rss_dict)

        try:
            data = {
                "title": "Response Stages",
                "spacekey": self.space,
                "parentid": str(REACTutils.confluence_get_page_id(
                                self.apipath, self.auth, self.space,
                                self.root_name)),
                "confluencecontent": content,
            }

            res = REACTutils.push_to_confluence(data, self.apipath, self.auth)
            if res == 'Page updated':
                print("==> updated page: Response Stages root page")
        except Exception as err:
            print("Response Stages root page" + " failed")
            print("Err message: %s" % err)
            print('-' * 60)
            traceback.print_exc(file=sys.stdout)
            print('-' * 60)

        print("[+] Response Stages populated!")


