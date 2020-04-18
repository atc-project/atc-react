# You can help contribute to RE&CT

RE&CT is in a constant state of development. We are always on the lookout for new information to help refine and extend what is covered. If you have additional Incident Response techniques, know about variations on one already covered, or have other relevant information, then we would like to hear from you.

All contributions and feedback to RE&CT are appreciated. Please don't hesitate to tell us what do you think could be improved by [submitting GitHub issue](#how-to-submit-an-issue).

# How to add a new Response Action?

If you would like to contribute a Response Action only, you need to follow [How to add a new feature or create a pull request](#how-to-add-a-new-feature-or-create-a-pull-request) guideline, points 1, 2, 3, 5, 7, 8, bypassing 4 and 6, since you don't need the development environment.

Here is an example of good Response Action — [RA3207: Block IP on IPS](response_actions/RA_3207_block_ip_on_ips.yml):

```
title: RA_3207_block_ip_on_ips
id: RA3207
description: Block an IP address in an IPS
author: '@atc_project'
creation_date: 31.01.2019
stage: containment
linked_analytics:
  - MS_IPS
workflow: |
  Block ip on IPS using native filtering functionality.
  Warning: 
  - If not all corporate hosts access the internet through the IPS, you will **not** be able to contain the threat using this Response Action.
  - Be careful blocking IP address. Make sure it's not a cloud provider or a hoster. If you would like to block something that is hosted on a well-known cloud provider or on a big hoster IP address, you should block a specific URL using alternative Response Action.
```

1. It is vendor-agnostic (doesn't include any specific IPS configurations)
2. It is detailed enough to be actionable and useful
3. Provides some important notes for a user

For now, we would like to focus on high-level definition of what should be done on a specific IR stage. It doesn't necessary to describe a specific way to configure IP blocking policy on a specific IPS solution (or any other system) since it is its basic functionality. If an organization has an IPS, we suppose that they know how to use it. If not, RE&CT will not (and doesn't suppose to) help.  

Please use the same approach for your contribution.  

You can pick up one of the Response Actions marked by "*" sign in the [Matrix](README.md#the-rect-framework). The links lead to GitHub issues, that you can use to contribute your analytics. All of the Response Actions mentioned in the issues have a special placeholder file with pre-defined ID and description that you should use to contribute your analytics. Don't hesitate to put your name to the `author` field, since these issues and placeholders have been created for one reason — to describe the way RE&CT should grow.  

If you would like to contribute a completely new Response Action, please use a special [Response Action template](response_actions/respose_action.yml.template).  

# How to add a new Response Playbook?

If you would like to contribute a Response Playbook only, you need to follow [How to add a new feature or create a pull request](#how-to-add-a-new-feature-or-create-a-pull-request) guideline, points 1, 2, 3, 5, 7, 8, bypassing 4 and 6, since you don't need the development environment.

Please use a special [Response Playbook template](response_playbooks/respose_playbook.yml.template) and existing [RP0001: Phishing email](response_playbooks/RP_0001_phishing_email.yml) response playbook as a reference.

# How to submit an issue?

First, please refer to [contribution-guide.org](http://www.contribution-guide.org/) for the steps we expect from contributors before submitting an issue or bug report. Be as concrete as possible, include relevant logs, package versions etc.

The proper place for open-ended questions is [Slack](https://join.slack.com/t/atomicthreatcoverage/shared_invite/zt-6ropl01z-wIdiq3M0AEZPj_HiKfbiBg) or [Telegram](https://t.me/atomic_threat_coverage). 

# How to add a new feature or create a pull request?

1. Fork the [atc-react repository](https://github.com/atc-project/atc-react)
2. Clone your fork: `git clone https://github.com/<YOUR GITHUB USERNAME>/atc-react.git`
3. Create a new branch based on `develop`: `git checkout -b my-feature develop`
4. Setup your Python enviroment
   - Create a new [virtual environment](https://virtualenv.pypa.io/en/stable/): `pip install virtualenv; virtualenv atc_env` and activate it:
      - For linux: `source atc_env/bin/activate` 
      - For windows: `atc_env\Scripts\activate`
   - Install ATC and its test dependencies in [editable mode](https://pip.pypa.io/en/stable/reference/pip_install/#editable-installs) — `pip install -r requirements.txt`
5. Implement your changes
6. Check your code for PEP8 requirements
7. Add files, commit and push: `git add ... ; git commit -m "my commit message"; git push origin my-feature`
8. [Create a PR](https://help.github.com/articles/creating-a-pull-request/) on Github. Write a **clear description** for your PR, including all the context and relevant information, such as:
   - The issue that you fixed, e.g. `Fixes #123`
   - Motivation: why did you create this PR? What functionality did you set out to improve? What was the problem + an overview of how you fixed it? Whom does it affect and how should people use it?
   - Any other useful information: links to other related Github or mailing list issues and discussions, benchmark graphs, academic papers…
   - Note that your Pull Request should be into the **develop** branch, **not master**
