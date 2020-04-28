#!/usr/bin/env python3

from scripts.populatemarkdown import PopulateMarkdown
from scripts.thehive_templates import RPTheHive
from scripts.atcutils import ATCutils
from scripts.generate_mkdocs_config import GenerateMkdocs
from scripts.react2stix import GenerateSTIX

# Others
import argparse

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description="""Main function of atc-react.

    You can not only choose to export analytics but also to use different
    modules.
""")

    # Mutually exclusive group for chosing the output of the script
    group = parser.add_mutually_exclusive_group(required=True)

    group.add_argument('-M', '--markdown', action='store_true',
                       help='Export analytics to Markdown repository')
    group.add_argument('-T', '--thehive', action='store_true',
                       help='Generate TheHive Case templates')
    group.add_argument('-MK', '--mkdocs', action='store_true',
                       help='Generate mkdofc navigation file')
    group.add_argument('-STIX', '--stix', action='store_true',
                       help='Generate STIX objects')

    # Mutually exclusive group for chosing type of data
    group2 = parser.add_mutually_exclusive_group(required=False)

    group2.add_argument('-A', '--auto', action='store_true',
                        help='Build full repository')
    group2.add_argument('-RA', '--responseactions', action='store_true',
                        help='Build response action part')
    group2.add_argument('-RP', '--responseplaybook', action='store_true',
                        help='Build response playbook part')
    group2.add_argument('-RS', '--responsestage', action='store_true',
                        help='Build response stage part')

    # Init capabilities
    parser.add_argument('-i', '--init', action='store_true',
                        help="Build initial pages or directories " +
                             "depending on the export type")

    args = parser.parse_args()

    if args.markdown:
        PopulateMarkdown(auto=args.auto, ra=args.responseactions,
                         rp=args.responseplaybook, rs=args.responsestage, init=args.init)
    elif args.mkdocs:
        GenerateMkdocs()
    elif args.stix:
        GenerateSTIX()
    elif args.thehive:
        ATCconfig = ATCutils.read_yaml_file("scripts/config.yml")
        ATCconfig2 = ATCutils.read_yaml_file("scripts/config.default.yml")
        print("HINT: Make sure proper directories are " +
              "configured in the scripts/config.yml")
        if ATCconfig.get(
                'response_playbooks_dir',
                ATCconfig2.get('response_playbooks_dir')) and \
                ATCconfig.get(
                    'response_actions_dir',
                    ATCconfig2.get('response_actions_dir')) and \
                ATCconfig.get(
                    'thehive_templates_dir',
                    ATCconfig2.get('thehive_templates_dir')):
            RPTheHive(
                inputRP=ATCconfig.get(
                    'response_playbooks_dir',
                    ATCconfig2.get('response_playbooks_dir')),
                inputRA=ATCconfig.get(
                    'response_actions_dir',
                    ATCconfig2.get('response_actions_dir')),
                output=ATCconfig.get(
                    'thehive_templates_dir',
                    ATCconfig2.get('thehive_templates_dir'))
            )
            print("Done!")
        else:
            print("ERROR: Dirs were not provided in the config")
