# Network VPN Validated Content

[![CI](https://github.com/redhat-cop/network.vpn/actions/workflows/tests.yml/badge.svg?branch=main&event=schedule)](https://github.com/redhat-cop/network.vpn/actions/workflows/tests.yml)
[![OpenSSF Best Practices](https://bestpractices.coreinfrastructure.org/projects/7639/badge)](https://bestpractices.coreinfrastructure.org/projects/7639)

This repository contains the `network.vpn` Ansible Collection.

## Description

An Ansible Collection to build, maintain and validate VPN tunnels across cloud providers and network appliances.
See `Supported Providers` section for more details.

## Tested with Ansible

Tested with ansible-core >=2.15 releases.

## Installation

To consume this Validated Content from Automation Hub, the following needs to be added to `ansible.cfg`:

```ini
[galaxy]
server_list = automation_hub

[galaxy_server.automation_hub]
url=https://cloud.redhat.com/api/automation-hub/
auth_url=https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token
token=<SuperSecretToken>
```

Get the required token from the [Automation Hub Web UI](https://console.redhat.com/ansible/automation-hub/token).

With this configured, simply run the following commands:

```bash
ansible-galaxy collection install network.vpn
```

## Using this collection

### Example 1

```yaml
---
- name: Deploy and validate AWS and Azure tunnels
  hosts: localhost
  gather_facts: true
  tasks:
    - name: "Deploy aws"
      ansible.builtin.include_role:
        name: network.vpn.deploy
      vars:
        provider: aws
        configuration_file: aws.yaml

    - name: "Deploy azure"
      ansible.builtin.include_role:
        name: network.vpn.deploy
      vars:
        provider: azure
        configuration_file: azure.yaml

    - name: "Validate aws tunnel"
      ansible.builtin.include_role:
        name: network.vpn.validate
      vars:
        provider: aws
        tunnel: 1
        session_status: UP

    - name: "Validate azure tunnel"
      ansible.builtin.include_role:
        name: network.vpn.validate
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
    - name: "Invoke deploy role"
      ansible.builtin.include_role:
        name: network.vpn.deploy
      vars:
        provider: csr
        configuration_file: "{{ inventory_hostname }}.yaml"

    - name: "Invoke validate role"
      ansible.builtin.include_role:
        name: network.vpn.validate
      vars:
        tunnel: Tunnel0
        session_status: Connected
```

## Supported providers

| **Provider** | **Operations** | **Operation Options**                                                                             |
| ------------ | -------------- | ------------------------------------------------------------------------------------------------- |
| aws          | deploy         | [Options](https://github.com/redhat-cop/network.vpn/blob/main/docs/providers/aws/deploy.yaml)     |
|              | validate       | [Options](https://github.com/redhat-cop/network.vpn/blob/main/docs/providers/aws/validate.yaml)   |
|              |                |
| azure        | deploy         | [Options](https://github.com/redhat-cop/network.vpn/blob/main/docs/providers/azure/deploy.yaml)   |
|              | validate       | [Options](https://github.com/redhat-cop/network.vpn/blob/main/docs/providers/azure/validate.yaml) |
|              |                |
| csr          | deploy         | [Options](https://github.com/redhat-cop/network.vpn/blob/main/docs/providers/csr/deploy.yaml)     |
|              | validate       | [Options](https://github.com/redhat-cop/network.vpn/blob/main/docs/providers/csr/validate.yaml)   |

## Requirements

The following collections should be installed:

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
