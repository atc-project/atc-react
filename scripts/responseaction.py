#!/usr/bin/env python3

from jinja2 import Environment, FileSystemLoader
import os

try:
    from scripts.reactutils import REACTutils
    from scripts.react_mapping import rs_mapping
    env = Environment(loader=FileSystemLoader('scripts/templates'))
except:
    from response.atc_react.scripts.reactutils import REACTutils
    from response.atc_react.scripts.react_mapping import rs_mapping
    env = Environment(loader=FileSystemLoader(
        'response/atc_react/scripts/templates'))

REACTConfig = REACTutils.load_config("config.yml")


class ResponseAction:
    """Class for the Playbook Actions entity"""

    def __init__(self, yaml_file, apipath=None, auth=None, space=None):
        """Init method"""

        # Init vars
        self.yaml_file = yaml_file
        self.apipath = apipath
        self.auth = auth
        self.space = space
        # The name of the directory containing future markdown Response_Actions
        self.parent_title = "Response_Actions"

        # Init methods
        self.parse_into_fields(self.yaml_file)


    def parse_into_fields(self, yaml_file):
        """Description"""

        self.ra_parsed_file = REACTutils.read_yaml_file(yaml_file)


    def render_template(self, template_type):
        """Description
        template_type:
            - "markdown"
            - "confluence"
        """

        if template_type not in ["markdown", "confluence"]:
            raise Exception(
                "Bad template_type. Available values:" +
                " [\"markdown\", \"confluence\"]")

        #
        # PRE: Common for both Markdown and Confluence templates
        #

        self.ra_parsed_file.update(
            {'category': REACTutils.get_ra_category(self.ra_parsed_file
                .get('id'))}
        )

        self.ra_parsed_file.update(
            {'description': self.ra_parsed_file.get('description').strip()}
        )

        # Get proper template
        if template_type == "markdown":

            template = env.get_template(
                'markdown_responseaction_template.md.j2'
            )
    
            self.ra_parsed_file.update(
                {'title': REACTutils.normalize_react_title(self.ra_parsed_file
                    .get('title'))}
            )
    
            stage_list = []
            stage = self.ra_parsed_file.get('stage')
    
            for rs_id, rs_name in rs_mapping.items():
                if REACTutils.normalize_rs_name(stage) == rs_name:
                    stage_list.append((rs_id, rs_name))
    
            self.ra_parsed_file.update(
                {'stage': stage_list}
            )

        elif template_type == "confluence":

            template = env.get_template(
                'confluence_responseaction_template.html.j2')

            new_title = self.ra_parsed_file.get('id')\
                + ": "\
                + REACTutils.normalize_react_title(self.ra_parsed_file.get('title'))

            self.ra_parsed_file.update(
                {'title': new_title}
            )

            self.ra_parsed_file.update(
                {'confluence_viewpage_url': REACTConfig.get('confluence_viewpage_url')})

            ##
            ## Add link to a stage
            ##
            stage = self.ra_parsed_file.get('stage')
            rs_list = []
            for rs_id, rs_name in rs_mapping.items():
                if REACTutils.normalize_rs_name(stage) == rs_name:
                    if self.apipath and self.auth and self.space:
                        rs_confluence_page_name = rs_id + ": " + rs_name
                        rs_confluence_page_id = str(REACTutils.confluence_get_page_id(
                            self.apipath, self.auth, self.space, rs_confluence_page_name)
                        )
                        rs_list.append((rs_id, rs_name, rs_confluence_page_id))
                    else:
                        rs_confluence_page_id = ""
                        rs_list.append((rs_id, rs_name, rs_confluence_page_id))
                    break

            self.ra_parsed_file.update(
                    {'stage': rs_list}
            )

        #
        # POST: Common for both Markdown and Confluence templates
        #
        self.content = template.render(self.ra_parsed_file)

    def save_markdown_file(self,
                           atc_dir=REACTConfig.get('md_name_of_root_directory')):
        """Write content (md template filled with data) to a file"""

        base = os.path.basename(self.yaml_file)
        title = os.path.splitext(base)[0]

        file_path = atc_dir + self.parent_title + "/" + \
            title + ".md"

        return REACTutils.write_file(file_path, self.content)
