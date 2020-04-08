#!/usr/bin/env python3

from scripts.atcutils import ATCutils
from jinja2 import Environment, FileSystemLoader
import os


ATCconfig = ATCutils.load_config("scripts/config.yml")


class ResponseAction:
    """Class for the Playbook Actions entity"""

    def __init__(self, yaml_file):
        """Init method"""

        # Init vars
        self.yaml_file = yaml_file
        # The name of the directory containing future markdown Response_Actions
        self.parent_title = "Response_Actions"

        # Init methods
        self.parse_into_fields(self.yaml_file)

    def parse_into_fields(self, yaml_file):
        """Description"""

        self.ra_parsed_file = ATCutils.read_yaml_file(yaml_file)

    def render_template(self, template_type):
        """Description
        template_type:
            - "markdown"
        """

        if template_type not in ["markdown"]:
            raise Exception(
                "Bad template_type. Available values:" +
                " [\"markdown\"]")

        # Point to the templates directory
        env = Environment(loader=FileSystemLoader('scripts/templates'))

        template = env.get_template(
            'markdown_responseaction_template.md.j2'
        )

        self.ra_parsed_file.update(
            {'description': self.ra_parsed_file
                .get('description').strip()}
        )

        self.ra_parsed_file.update(
            {'title': ATCutils.normalize_react_title(self.ra_parsed_file
                .get('title'))}
        )

        self.content = template.render(self.ra_parsed_file)

    def save_markdown_file(self,
                           atc_dir=ATCconfig.get('md_name_of_root_directory')):
        """Write content (md template filled with data) to a file"""

        base = os.path.basename(self.yaml_file)
        title = os.path.splitext(base)[0]

        file_path = atc_dir + self.parent_title + "/" + \
            title + ".md"

        return ATCutils.write_file(file_path, self.content)
