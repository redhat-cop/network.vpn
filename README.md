# Ansible Network VPN Collection

This repository contains the `network.vpn` Ansible Collection.

## Description
An Ansible Collection to build, maintain and validate VPN tunnels across cloud providers and network appliances.
See `Supported Providers` section for more details.

## Tested with Ansible

Tested with ansible-core 2.13 releases.

## Installation

```
ansible-galaxy collection install network.vpn
```

You can also include it in a `requirements.yml` file and install it via `ansible-galaxy collection install -r requirements.yml` using the format:

```yaml
collections:
- name: network.vpn
```

See [Ansible Using collections](https://docs.ansible.com/ansible/latest/user_guide/collections_using.html) for more details.

## Using this collection

### Example 1

```yaml
---
- name: Deploy and validate AWS and Azure tunnels
  hosts: localhost
  gather_facts: true
  tasks:
    - name: "Run network.vpn collection with specified actions"
      ansible.builtin.include_role:
        name: network.vpn.run
      vars:
        actions:
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
    - name: "Run network.vpn collection with specified actions"
      ansible.builtin.include_role:
        name: network.vpn.run
      vars:
        provider: csr
        actions:
          - name: deploy
            vars:
              configuration_file: "{{ inventory_hostname }}.yaml"

          - name: validate
            vars:
              tunnel: Tunnel0
              session_status: Connected
```

## Supported providers


| **Provider**           | **Actions**                                                 | **Action Options**  |
|------------------------|-------------------------------------------------------------|----------------------
| aws                    | deploy                                                      | [Options](https://github.com/ansible-network/network.vpn/blob/main/docs/providers/aws/deploy.yaml)
|                        | validate                                                    | [Options](https://github.com/ansible-network/network.vpn/blob/main/docs/providers/aws/validate.yaml)
|                        |                                                             |
| azure                  | deploy                                                      | [Options](https://github.com/ansible-network/network.vpn/blob/main/docs/providers/azure/deploy.yaml)
|                        | validate                                                    | [Options](https://github.com/ansible-network/network.vpn/blob/main/docs/providers/azure/validate.yaml)
|                        |                                                             |
| csr                    | deploy                                                      | [Options](https://github.com/ansible-network/network.vpn/blob/main/docs/providers/csr/validate.yaml)
|                        | validate                                                    | [Options](https://github.com/ansible-network/network.vpn/blob/main/docs/providers/csr/validate.yaml)


## Requirements
This following collections should be installed:
- azure.azcollection
- cisco.ios
- community.aws

## Licensing

GNU General Public License v3.0 or later.

See [COPYING](https://www.gnu.org/licenses/gpl-3.0.txt) to see the full text.
