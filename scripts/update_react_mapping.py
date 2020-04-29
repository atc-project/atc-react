#!/usr/bin/env python3

import json
import requests

ra_mapping = {}
rs_mapping = {}

react_json_url = ("https://raw.githubusercontent.com/"
                   "/atc-project/atc-react/master/"
                   "docs/react.json")

react_json = requests.get(react_json_url).json()

for object in react_json["objects"]:
    if object['type'] == "x-react-action" and "RA" in \
            object['external_references'][0]['external_id']:
        ra_id = object['external_references'][0]['external_id']
        ra_name = object['name']
        ra_mapping.update({ra_id: ra_name})
    elif object['type'] == "x-react-stage":
        rs_id = object['external_references'][0]['external_id']
        rs_name = object['name']
        rs_mapping.update({rs_id: rs_name})

with open('react_mapping.py', 'w') as fp:
    fp.write("ra_mapping = " + json.dumps(ra_mapping, sort_keys=True, indent=4) + '\n')
    fp.write("rs_mapping = " + json.dumps(rs_mapping, sort_keys=True, indent=4))
