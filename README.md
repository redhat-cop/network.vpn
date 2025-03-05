# Network VPN Validated Content

[![CI](https://github.com/redhat-cop/network.vpn/actions/workflows/tests.yml/badge.svg?branch=main&event=schedule)](https://github.com/redhat-cop/network.vpn/actions/workflows/tests.yml)
[![OpenSSF Best Practices](https://bestpractices.coreinfrastructure.org/projects/7639/badge)](https://bestpractices.coreinfrastructure.org/projects/7639)

## About
The Ansible Network VPN Validated Content provides essential roles to build, maintain and validate VPN tunnels across cloud providers and network appliances.

This collection includes the following roles:
- **`deploy`**: Ensure consistent configuration deployment across network devices.
- **`validate`**: Verifies the correctness and status of deployed VPN configurations.

## Included content

Click on the name of a role to view its documentation:

<!--start collection content-->
### Roles
Name | Description
--- | ---
[network.vpn.deploy](roles/deploy/README.md) | Deploy consistent network configurations.
[network.vpm.validate](roles/validate/README.md) | Validate the deployed VPN configurations.

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
## Usecases

### Example 1: Deploy and validate AWS and Azure tunnels

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

### Example 2: Deploy and validate CSR tunnels

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

## Requirements

The following collections should be installed:

- azure.azcollection
- cisco.ios
- community.aws

## Contributing

We welcome community contributions to this collection. If you find problems, please open an issue or create a PR against this repository.

Don't know how to start? Refer to the [Ansible community guide](https://docs.ansible.com/ansible/devel/community/index.html)!

Want to submit code changes? Take a look at the [Quick-start development guide](https://docs.ansible.com/ansible/devel/community/create_pr_quick_start.html).

We also use the following guidelines:

* [Collection review checklist](https://docs.ansible.com/ansible/devel/community/collection_contributors/collection_reviewing.html)
* [Ansible development guide](https://docs.ansible.com/ansible/devel/dev_guide/index.html)
* [Ansible collection development guide](https://docs.ansible.com/ansible/devel/dev_guide/developing_collections.html#contributing-to-collections)

### Code of Conduct
This collection follows the Ansible project's
[Code of Conduct](https://docs.ansible.com/ansible/devel/community/code_of_conduct.html).
Please read and familiarize yourself with this document.

## Release notes

Release notes are available [here](https://github.com/redhat-cop/network.vpn/blob/main/CHANGELOG.rst).

## Related information

- [Developing network resource modules](https://github.com/ansible-network/networking-docs/blob/main/rm_dev_guide.md)
- [Ansible Networking docs](https://github.com/ansible-network/networking-docs)
- [Ansible Collection Overview](https://github.com/ansible-collections/overview)
- [Ansible Roles overview](https://docs.ansible.com/ansible/2.9/user_guide/playbooks_reuse_roles.html)
- [Ansible User guide](https://docs.ansible.com/ansible/latest/user_guide/index.html)
- [Ansible Developer guide](https://docs.ansible.com/ansible/latest/dev_guide/index.html)
- [Ansible Community Code of Conduct](https://docs.ansible.com/ansible/latest/community/code_of_conduct.html)

## Licensing

GNU General Public License v3.0 or later.

See [LICENSE](https://www.gnu.org/licenses/gpl-3.0.txt) to see the full text.
