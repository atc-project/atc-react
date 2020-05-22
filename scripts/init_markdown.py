#!/usr/bin/env python3

try:
    from scripts.reactutils import REACTutils
except:
    from reactutils import REACTutils

from pathlib import Path


def react_create_markdown_dirs():
    REACTConfig = REACTutils.load_config('config.yml')
    base_dir = Path(REACTConfig.get(
        'md_name_of_root_directory',
        '../docs'
    ))

    target_dir_list = ['Response_Actions', 'Response_Playbooks' , 'Response_Stages']

    for item in target_dir_list:
        (base_dir / item).mkdir(parents=True, exist_ok=True)


if __name__ == '__main__':
    react_create_markdown_dirs()
