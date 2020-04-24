#!/usr/bin/env python3

from scripts.atcutils import ATCutils
from pathlib import Path


def create_markdown_dirs():
    config = ATCutils.load_config('scripts/config.yml')
    base_dir = Path(config.get(
        'md_name_of_root_directory',
        '../docs'
    ))

    target_dir_list = ['Response_Actions', 'Response_Playbooks']

    for item in target_dir_list:
        (base_dir / item).mkdir(parents=True, exist_ok=True)


if __name__ == '__main__':
    create_markdown_dirs()
