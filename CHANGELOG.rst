====================================
Network VPN Collection Release Notes
====================================

.. contents:: Topics

v5.0.0
======

Major Changes
-------------

- Added integration tests to align with the new role-based structure.
- Converted operations like `deploy` and `validate` into individual roles for better modularity and clarity.
- Each role (`deploy`, `validate`) now has its own README.md and integration tests.
- Improved documentation and usage examples for each role to reflect the restructuring.
- Restructured the network.vpn collection by converting supported operations into separate roles
- Updated the `network.vpn` collection documentation to reflect the new role-based structure.

v4.0.0
======

Release Summary
---------------

With this release, the minimum required version of `ansible-core` for this collection is `2.15.0`. The last version known to be compatible with `ansible-core` versions below `2.15` is v3.0.1.

Major Changes
-------------

- Bumping `requires_ansible` to `>=2.15.0`, since previous ansible-core versions are EoL now.

v3.0.1
======

Release Summary
---------------

Re-releasing 3.0.0 as 3.0.1, starting from 3.0.0, the minimum `ansible-core` version this collection requires is `2.14.0`. The last known version compatible with ansible-core<2.14 is `2.0.0`.

v3.0.0
======

Release Summary
---------------

Starting from this release, the minimum `ansible-core` version this collection requires is `2.14.0`. The last known version compatible with ansible-core<2.14 is `v2.0.0`.

Major Changes
-------------

- Bumping `requires_ansible` to `>=2.14.0`, since previous ansible-core versions are EoL now.

v2.0.0
======

Major Changes
-------------

- Please refer to README for updated examples.
- Staring with this release, the keyword `actions` has been changed to `operations`.

Documentation Changes
---------------------

- Fix installation guide in README.
- Update readme with collections installation commands.

v1.3.0
======

Release Summary
---------------

Re-releasing v1.2.0 with bumped galaxy.yml version.

v1.2.0
======

Release Summary
---------------

Fixed errors that were reported during ansible-galaxy collection publish process for v1.1.0.

v1.1.0
======

Release Summary
---------------

Re-releasing v1.0.0 with updated version tag and fixed URLs for issues and repository in galaxy.yml.

v1.0.0
======

Release Summary
---------------

Releasing v1.0.0 of the Ansible network.vpn collection that builds, maintains and validates VPN tunnels across cloud providers and network appliances.
