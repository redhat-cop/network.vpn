# Network VPN Validated Content

[![CI](https://github.com/redhat-cop/network.vpn/operations/workflows/tests.yml/badge.svg?event=schedule)](https://github.com/ansible-network/network.telemetry/operations/workflows/tests.yml)
[![OpenSSF Best Practices](https://bestpractices.coreinfrastructure.org/projects/7639/badge)](https://bestpractices.coreinfrastructure.org/projects/7639)

This repository contains the `network.vpn` Ansible Collection.

## Description
An Ansible Collection to build, maintain and validate VPN tunnels across cloud providers and network appliances.
See `Supported Providers` section for more details.

## Tested with Ansible

Tested with ansible-core >=2.13 releases.


## Installation

#### Install from Automation Hub

To consume this Validated Content from Automation Hub, the following needs to be added to `ansible.cfg`:

```
[galaxy]
server_list = automation_hub

[galaxy_server.automation_hub]
url=https://cloud.redhat.com/api/automation-hub/
auth_url=https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token
token=<SuperSecretToken>
```
Get the required token from the [Automation Hub Web UI](https://console.redhat.com/ansible/automation-hub/token).

With this configured, simply run the following commands:

```
ansible-galaxy collection install network.vpn
```

#### Install from GitHub

```
ansible-galaxy collection install git+https://github.com/redhat-cop/network.vpn
```

You can also include it in a `requirements.yml` file and install it via `ansible-galaxy collection install -r requirements.yml` using the format:

```yaml
collections:
- name: https://github.com/redhat-cop/network.telemetry.git
  type: git
  version: main
```

## Using this collection

### Example 1

```yaml
---
- name: Deploy and validate AWS and Azure tunnels
  hosts: localhost
  gather_facts: true
  tasks:
    - name: "Run network.vpn collection with specified operations"
      ansible.builtin.include_role:
        name: network.vpn.run
      vars:
        operations:
          - name: deploy
            vars:
              provider: aws
              configuration_file: aws.yaml
          
          - name: deploy
            vars:
              provider: azure
              configuration_file: azure.yaml

          - name: validate
            vars:
              provider: aws
              tunnel: 1
              session_status: UP
          
          - name: validate
            vars:
              provider: azure
              resource_group: VPN-RG
              vpn_connection_name: Azure-to-AWS
              session_status: Connected
```

### Example 2

```yaml
---
- name: Deploy and Validate CSR tunnels
  hosts: csr_gateways
  gather_facts: true
  tasks:
    - name: "Run network.vpn collection with specified operations"
      ansible.builtin.include_role:
        name: network.vpn.run
      vars:
        provider: csr
        operations:
          - name: deploy
            vars:
              configuration_file: "{{ inventory_hostname }}.yaml"

          - name: validate
            vars:
              tunnel: Tunnel0
              session_status: Connected
```

## Supported providers


| **Provider**           | **Operations**                                                 | **Operation Options**  |
|------------------------|-------------------------------------------------------------|---------------------------
| aws                    | deploy                                                      | [Options](https://github.com/ansible-network/network.vpn/blob/main/docs/providers/aws/deploy.yaml)
|                        | validate                                                    | [Options](https://github.com/ansible-network/network.vpn/blob/main/docs/providers/aws/validate.yaml)
|                        |                                                             |
| azure                  | deploy                                                      | [Options](https://github.com/ansible-network/network.vpn/blob/main/docs/providers/azure/deploy.yaml)
|                        | validate                                                    | [Options](https://github.com/ansible-network/network.vpn/blob/main/docs/providers/azure/validate.yaml)
|                        |                                                             |
| csr                    | deploy                                                      | [Options](https://github.com/ansible-network/network.vpn/blob/main/docs/providers/csr/deploy.yaml)
|                        | validate                                                    | [Options](https://github.com/ansible-network/network.vpn/blob/main/docs/providers/csr/validate.yaml)


## Requirements
This following collections should be installed:
- azure.azcollection
- cisco.ios
- community.aws

### Code of Conduct
This collection follows the Ansible project's
[Code of Conduct](https://docs.ansible.com/ansible/devel/community/code_of_conduct.html).
Please read and familiarize yourself with this document.


## Release notes

Release notes are available [here](https://github.com/redhat-cop/network.vpn/blob/main/CHANGELOG.rst).

## Licensing

GNU General Public License v3.0 or later.

See [COPYING](https://www.gnu.org/licenses/gpl-3.0.txt) to see the full text.
