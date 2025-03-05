# Deploy

## Overview
The `deploy` role reads VPN configuration details from the provided/default or remote inventory and deploys them to network appliances. It ensures that VPN settings remain consistent and compliant across devices. Users can source configurations from local files or remote repositories and deploy only when changes are detected.

## Features
- Retrieve VPN configuration data from local or remote sources.
- Deploy VPN settings only when modifications are necessary.
- Support for integration with Git repositories for version control.

## Variables

| Variable Name        | Default Value | Required | Type |Description                                                   | Example |
|:---------------------|:-------------:|:--------:|:----:|:-------------------------------------------------------------|:-------:|
| `provider` | `""`          | yes      | str  | Cloud or network provider to validate VPN configurations.                    | `"aws","azure", "csr"` |
| `tunnel`         | `""`          | yes      | str | Tunnel identifier to validate.  | `"Tunnel0", "1"` |
| `session_status` | `""`          | yes      | str | Expected session status of the VPN tunnel. | `"connected", "UP"` |


## Usage
Below is an example playbook demonstrating how to use the `deploy` role, where we retrieve VPN configurations from the specified gh_scm_path and apply them to the network.

```yaml
---
- name: Deploy network VPN configurations
  hosts: all
  gather_facts: true
  tasks:
    - name: Include deploy role
      ansible.builtin.include_role:
        name: network.vpn.deploy
      vars:
        provider: aws
        tunnel: 1
        session_status: UP
```
### Example Output
When the playbook executes successfully, the output will show VPN configurations being applied. Verbose output can be enabled for debugging.

## License
GNU General Public License v3.0 or later.
See [LICENSE](https://www.gnu.org/licenses/gpl-3.0.txt) to see the full text.

## Author Information
- Ansible Network Content Team
