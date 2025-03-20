# Validate

This role serves as the validation point for the `network.vpn` collection. Based on the provider and validation parameters specified, the correct validation tasks are executed.

## Overview

The `validate` role verifies the correctness and status of deployed VPN configurations. It checks whether the VPN tunnels are active, properly configured, and meet the expected session states. This role helps ensure that VPN configurations remain operational and compliant across cloud providers and network appliances.

## Features
- Validate VPN tunnel status across multiple providers.
- Ensure VPN configurations match expected states.
- Support for integration with Git repositories for storing validation results.

## Variables

| Variable Name        | Default Value | Required | Type |Description                                                   | Example |
|:---------------------|:-------------:|:--------:|:----:|:-------------------------------------------------------------|:-------:|
| `provider` | `""`          | yes      | str  | Cloud or network provider to validate VPN configurations.                    | `"aws","azure", "csr"` |
| `tunnel`         | `""`          | yes      | str | Tunnel identifier to validate.  | `"Tunnel0", "1"` |
| `session_status` | `""`          | yes      | str | Expected session status of the VPN tunnel. | `"connected", "UP"` |


## Usage
Below is an example playbook demonstrating how to use the `validate` role to verify VPN configurations across different providers.

```yaml
---
- name: Validate network VPN configurations
  hosts: all
  gather_facts: true
  tasks:
    - name: Include validate role
      ansible.builtin.include_role:
        name: network.vpn.validate
      vars:
        provider: aws
        tunnel: 1
        session_status: UP
```
### Example Output
When the playbook is executed successfully, the output will display the validation results. If discrepancies are found, they will be logged.

## License
GNU General Public License v3.0 or later.
See [LICENSE](https://www.gnu.org/licenses/gpl-3.0.txt) to see the full text.

## Author Information
- Ansible Network Content Team
