#!/usr/bin/env python3

try:
    from scripts.reactutils import REACTutils
except:
    from response.atc_react.scripts.reactutils import REACTutils

from requests.auth import HTTPBasicAuth
import getpass


def main(c_auth=None):

    try:
        REACTConfig = REACTutils.load_config("config.yml")
        confluence_space_name = REACTConfig.get('confluence_space_name')
        confluence_space_home_page_name = REACTConfig.get(
            'confluence_space_home_page_name')
        confluence_rest_api_url = REACTConfig.get('confluence_rest_api_url')
        confluence_name_of_root_directory = REACTConfig.get(
            'confluence_name_of_root_directory')

    except Exception as e:
        raise e
        pass

    if not c_auth:
        mail = input("Login: ")
        password = getpass.getpass(prompt='Password: ', stream=None)
        auth = HTTPBasicAuth(mail, password)
    else:
        auth = c_auth

    url = confluence_rest_api_url
    content = ""

    print("[*] Creating RE&CT root page...")

    data = {
        "title": confluence_name_of_root_directory,
        "spacekey": confluence_space_name,
        "parentid": str(REACTutils.confluence_get_page_id(
            url, auth, confluence_space_name,
            confluence_space_home_page_name)),
        "confluencecontent": content,
    }

    if not REACTutils.push_to_confluence(data, url, auth):
        raise Exception("[-] Could not create or update the page. " +
                        "Is the parent name correct?")

    pages = ["Response Actions","Response Playbooks","Response Stages"]

    for page in pages:
        print("[*] Creating %s..." % page)
        data = {
            "title": page,
            "spacekey": confluence_space_name,
            "parentid": str(REACTutils.confluence_get_page_id(
                url, auth, confluence_space_name,
                confluence_name_of_root_directory)),
            "confluencecontent": content,
        }

        if not REACTutils.push_to_confluence(data, url, auth):
            raise Exception("[*] Could not create or update the page. " +
                            "Is the parent name correct?")
    print("[+] Initial Confluence page structure created!")
    return True


if __name__ == "__main__":
    main()
