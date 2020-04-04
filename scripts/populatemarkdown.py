#!/usr/bin/env python3

# Import ATC classes
from scripts.responseaction import ResponseAction
from scripts.responseplaybook import ResponsePlaybook

# Import ATC Utils
from scripts.atcutils import ATCutils
from scripts.init_markdown import create_markdown_dirs

# Others
import glob
import traceback
import sys

ATCconfig = ATCutils.load_config("scripts/config.yml")


class PopulateMarkdown:
    """Class for populating markdown repo"""

    def __init__(self, ra=False, rp=False, auto=False,
                 ra_path=False, rp_path=False,
                 atc_dir=False, init=False):
        """Init"""

        # Check if atc_dir provided
        if atc_dir:
            self.atc_dir = atc_dir
        else:
            self.atc_dir = ATCconfig.get('md_name_of_root_directory') + '/'

        # Check if init switch is used
        if init:
            if self.init_export():
                print("[+] Created initial markdown directories successfully")
            else:
                print("[X] Failed to create initial markdown directories")
                raise Exception("Failed to markdown directories")

        # Main logic
        if auto:
            self.response_action(ra_path)
            self.response_playbook(rp_path)

        if ra:
            self.response_action(ra_path)

        if rp:
            self.response_playbook(rp_path)

    def init_export(self):
        try:
            create_markdown_dirs()
            return True
        except:
            return False

    def response_action(self, ra_path):
        """Populate Response Actions"""

        print("Populating Response Actions..")
        if ra_path:
            ra_list = glob.glob(ra_path + '*.yml')
        else:
            ra_dir = ATCconfig.get('response_actions_dir')
            ra_list = glob.glob(ra_dir + '/*.yml')

        for ra_file in ra_list:
            try:
                ra = ResponseAction(ra_file)
                ra.render_template("markdown")
                ra.save_markdown_file(atc_dir=self.atc_dir)
            except Exception as e:
                print(ra_file + " failed\n\n%s\n\n" % e)
                print("Err message: %s" % e)
                print('-' * 60)
                traceback.print_exc(file=sys.stdout)
                print('-' * 60)
        print("Response Actions populated!")

    def response_playbook(self, rp_path):
        """Populate Response Playbooks"""

        print("Populating Response Playbooks..")
        if rp_path:
            rp_list = glob.glob(rp_path + '*.yml')
        else:
            rp_dir = ATCconfig.get('response_playbooks_dir')
            rp_list = glob.glob(rp_dir + '/*.yml')

        for rp_file in rp_list:
            try:
                rp = ResponsePlaybook(rp_file)
                rp.render_template("markdown")
                rp.save_markdown_file(atc_dir=self.atc_dir)
            except Exception as e:
                print(rp_file + " failed\n\n%s\n\n" % e)
                print("Err message: %s" % e)
                print('-' * 60)
                traceback.print_exc(file=sys.stdout)
                print('-' * 60)
        print("Response Playbooks populated!")
