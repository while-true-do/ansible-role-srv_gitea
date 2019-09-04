<!--
name: README.md
description: This file contains important information for the repository.
author: while-true-do.io
contact: hello@while-true-do.io
license: BSD-3-Clause
-->

<!-- github shields -->
[![Github (tag)](https://img.shields.io/github/tag/while-true-do/ansible-role-srv_gitea.svg)](https://github.com/while-true-do/ansible-role-srv_gitea/tags)
[![Github (license)](https://img.shields.io/github/license/while-true-do/ansible-role-srv_gitea.svg)](https://github.com/while-true-do/ansible-role-srv_gitea/blob/master/LICENSE)
[![Github (issues)](https://img.shields.io/github/issues/while-true-do/ansible-role-srv_gitea.svg)](https://github.com/while-true-do/ansible-role-srv_gitea/issues)
[![Github (pull requests)](https://img.shields.io/github/issues-pr/while-true-do/ansible-role-srv_gitea.svg)](https://github.com/while-true-do/ansible-role-srv_gitea/pulls)
<!-- travis shields -->
[![Travis (com)](https://img.shields.io/travis/com/while-true-do/ansible-role-srv_gitea.svg)](https://travis-ci.com/while-true-do/ansible-role-srv_gitea)
<!-- ansible shields -->
[![Ansible (min. version)](https://img.shields.io/badge/dynamic/yaml.svg?label=Min.%20Ansible%20Version&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhile-true-do%2Fansible-role-srv_gitea%2Fmaster%2Fmeta%2Fmain.yml&query=%24.galaxy_info.min_ansible_version&colorB=black)](https://galaxy.ansible.com/while_true_do/srv_gitea)
[![Ansible (platforms)](https://img.shields.io/badge/dynamic/yaml.svg?label=Supported%20OS&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhile-true-do%2Fansible-role-srv_gitea%2Fmaster%2Fmeta%2Fmain.yml&query=galaxy_info.platforms%5B*%5D.name&colorB=black)](https://galaxy.ansible.com/while_true_do/srv_gitea)
[![Ansible (tags)](https://img.shields.io/badge/dynamic/yaml.svg?label=Galaxy%20Tags&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhile-true-do%2Fansible-role-srv_gitea%2Fmaster%2Fmeta%2Fmain.yml&query=%24.galaxy_info.galaxy_tags%5B*%5D&colorB=black)](https://galaxy.ansible.com/while_true_do/srv_gitea)

# Ansible Role: srv_gitea

An Ansible Role to install and configure gitea.

## Motivation

[Gitea.io](https://gitea.io/) is a git server, written in
[golang](https://golang.org/). As a Developer, having such a tool ready is quite
mandatory.

## Description

This Role install and configures [Gitea.io](https://gitea.io/).

-   Download the binary
-   Create needed directory structure
-   Configure the systemd service
-   Configure gitea
-   Updating does not work automatically

## Requirements

Used Modules:

-   [Ansible Package Module](https://docs.ansible.com/ansible/latest/modules/package_module.html)
-   [Ansible Service Module](https://docs.ansible.com/ansible/latest/modules/service_module.html)
-   [Ansible Systemd Module](https://docs.ansible.com/ansible/latest/modules/systemd_module.html)
-   [Ansible User Module](https://docs.ansible.com/ansible/latest/modules/user_module.html)
-   [Ansible Group Module](https://docs.ansible.com/ansible/latest/modules/group_module.html)
-   [Ansible Template Module](https://docs.ansible.com/ansible/latest/modules/template_module.html)
-   [Ansible ini_file Module](https://docs.ansible.com/ansible/latest/modules/ini_file_module.html)
-   [Ansible File Module](https://docs.ansible.com/ansible/latest/modules/file_module.html)
-   [Ansible Firewalld Module](https://docs.ansible.com/ansible/latest/modules/firewalld_module.html)
-   [Ansible get_url Module](https://docs.ansible.com/ansible/latest/modules/get_url_module.html)
-   [Ansible package_facts Module](https://docs.ansible.com/ansible/latest/modules/package_facts_module.html)

## Installation

Install from [Ansible Galaxy](https://galaxy.ansible.com/while_true_do/srv_gitea)
```
ansible-galaxy install while_true_do.srv_gitea
```

Install from [Github](https://github.com/while-true-do/ansible-role-srv_gitea)
```
git clone https://github.com/while-true-do/ansible-role-srv_gitea.git while_true_do.srv_gitea
```

Dependencies:

You need to have git installed on the destination system and you can use
[while_true_do.app_git](galaxy.ansible.com/while_true_do/app_git) or the role
will take care of a basic git installation.

```
ansible-galaxy install -r requirements.yml
```

## Usage

### Role Variables

```
---
# defaults file for while_true_do.srv_gitea

## Package Management
wtd_srv_gitea_package_mode: "binary"
# Only needed for wtd_srv_gitea_package_mode = "binary"
wtd_srv_gitea_package_version: "1.9.2"
wtd_srv_gitea_package_url: "https://dl.gitea.io/gitea/{{ wtd_srv_gitea_package_version }}/gitea-{{ wtd_srv_gitea_package_version }}-linux-amd64"
# State can be present|absent
wtd_srv_gitea_package_state: "present"

## Configuration Management
wtd_srv_gitea_conf_user:
  name: "gitea"
  group: "gitea"
  home: "/home/gitea"

wtd_srv_gitea_conf_port: "3000"
wtd_srv_gitea_conf_var: "/var/lib/gitea"
wtd_srv_gitea_conf_etc: "/etc/gitea"

# Gitea has tons of options. You can get an overview here:
# https://docs.gitea.io/en-us/config-cheat-sheet/
# https://github.com/go-gitea/gitea/blob/master/custom/conf/app.ini.sample
wtd_srv_gitea_conf:
  - option: "APP_NAME"
    value: "Gitea - Git with a cup of tea"
    section: null
  - option: RUN_MODE
    value: "prod"
    section: null
  - option: "RUN_USER"
    value: "{{ wtd_srv_gitea_conf_user.name }}"
    section: null
  - option: "AUTHOR"
    value: "Gitea - Git with a cup of tea"
    section: "ui.meta"
  - option: "HTTP_PORT"
    value: "{{ wtd_srv_gitea_conf_port }}"
    section: "server"
  - option: "HTTP_ADDR"
    value: "0.0.0.0"
    section: "server"
  - option: "DOMAIN"
    value: "localhost"
    section: "server"
  - option: "ROOT"
    value: "{{ wtd_srv_gitea_conf_user.home }}/gitea-repositories"
    section: "repository"

## Service Management
wtd_srv_gitea_service: "gitea"
# State can be started|stopped
wtd_srv_gitea_service_state: "started"
wtd_srv_gitea_service_enabled: true

## Firewalld Management
wtd_srv_gitea_fw_mgmt: true
wtd_srv_gitea_fw_port: "{{ wtd_srv_gitea_conf_port }}/tcp"
# State can be enabled|disabled
wtd_srv_gitea_fw_state: "enabled"
# Zone can be according to defined zones on your machine.
wtd_srv_gitea_fw_zone: "public"
```

### Example Playbook

Running Ansible
[Roles](https://docs.ansible.com/ansible/latest/user_guide/playbooks_reuse_roles.html)
can be done in a
[playbook](https://docs.ansible.com/ansible/latest/user_guide/playbooks_intro.html).

#### Simple

```
---
- hosts: all
  roles:
    - role: while_true_do.srv_gitea
```

#### Advanced

Install another version and change the port.

```
- hosts: all
  roles:
    - role: while_true_do.srv_gitea
      wtd_srv_gitea_conf_port: "8080"
      wtd_srv_gitea_package_version: "1.X.Y"
```

## Known Issues

1.  RedHat Testing is currently not possible in public, due to limitations
    in subscriptions.
2.  Some services and features cannot be tested properly, due to limitations
    in docker.

## Testing

Most of the "generic" tests are located in the
[Test Library](https://github.com/while-true-do/test-library).

Ansible specific testing is done with
[Molecule](https://molecule.readthedocs.io/en/stable/).

Infrastructure testing is done with
[testinfra](https://testinfra.readthedocs.io/en/stable/).

Automated testing is done with [Travis CI](https://travis-ci.com/while-true-do).

## Contribute

Thank you so much for considering to contribute. We are very happy, when somebody
is joining the hard work. Please fell free to open
[Bugs, Feature Requests](https://github.com/while-true-do/ansible-role-srv_gitea/issues)
or [Pull Requests](https://github.com/while-true-do/ansible-role-srv_gitea/pulls) after
reading the [Contribution Guideline](https://github.com/while-true-do/doc-library/blob/master/docs/CONTRIBUTING.md).

See who has contributed already in the [kudos.txt](./kudos.txt).

## License

This work is licensed under a [BSD-3-Clause License](https://opensource.org/licenses/BSD-3-Clause).

## Contact

-   Site <https://while-true-do.io>
-   Twitter <https://twitter.com/wtd_news>
-   Code <https://github.com/while-true-do>
-   Mail [hello@while-true-do.io](mailto:hello@while-true-do.io)
-   IRC [freenode, #while-true-do](https://webchat.freenode.net/?channels=while-true-do)
-   Telegram <https://t.me/while_true_do>
