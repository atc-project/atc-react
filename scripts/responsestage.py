#!/usr/bin/env python3

from jinja2 import Environment, FileSystemLoader

try:
    from scripts.reactutils import REACTutils
    from scripts.react_mapping import rs_mapping
    env = Environment(loader=FileSystemLoader('scripts/templates'))
except:
    from response.atc_react.scripts.reactutils import REACTutils
    from response.atc_react.scripts.react_mapping import rs_mapping
    env = Environment(loader=FileSystemLoader(
        'response/atc_react/scripts/templates'))

import os


REACTConfig = REACTutils.load_config("config.yml")


class ResponseStage:
    """Class for the Playbook Stage entity"""

    def __init__(self, yaml_file):
        """Init method"""

        # Init vars
        self.yaml_file = yaml_file
        # The name of the directory containing future markdown Response_Stages
        self.parent_title = "Response_Stages"

        # Init methods
        self.parse_into_fields(self.yaml_file)

    def parse_into_fields(self, yaml_file):
        """Description"""

        self.ra_parsed_file = REACTutils.read_yaml_file(yaml_file)

    def render_template(self, template_type):
        """Description
        template_type:
            - "markdown"
        """

        if template_type not in ["markdown"]:
            raise Exception(
                "Bad template_type. Available values:" +
                " [\"markdown\"]")

        template = env.get_template(
            'markdown_responsestage_template.md.j2'
        )

        self.ra_parsed_file.update(
            {'description': self.ra_parsed_file
                .get('description').strip()}
        )

        ras, ra_paths = REACTutils.load_yamls_with_paths(
            REACTConfig.get('response_actions_dir'))
        ra_filenames = [ra_path.split('/')[-1].replace('.yml', '')
                        for ra_path in ra_paths]

        rs_id = self.ra_parsed_file.get('id')

        stage_list = []

        for i in range(len(ras)):
            if rs_mapping[rs_id] == REACTutils.normalize_rs_name(ras[i].get('stage')):
                ra_id = ras[i].get('id')
                ra_filename = ra_filenames[i]
                ra_title = REACTutils.normalize_react_title(ras[i].get('title'))
                ra_description = ras[i].get('description').strip()
                stage_list.append(
                    (ra_id, ra_filename, ra_title, ra_description))

        self.ra_parsed_file.update({'stage_list': sorted(stage_list)})

        self.content = template.render(self.ra_parsed_file)

    def save_markdown_file(self,
                           atc_dir=REACTConfig.get('md_name_of_root_directory')):
        """Write content (md template filled with data) to a file"""

        base = os.path.basename(self.yaml_file)
        title = os.path.splitext(base)[0]

        file_path = atc_dir + self.parent_title + "/" + \
            title + ".md"

        return REACTutils.write_file(file_path, self.content)
