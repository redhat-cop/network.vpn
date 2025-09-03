#!/usr/bin/python
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = """
module: azure_rm_virtualnetworkgatewayconnection_info
version_added: "1.14.0"
short_description: Get virtual network connection info.
description: Get facts for a specific virtual network gateway connection.
author:
  - Nilashish Chakraborty (@NilashishC)
options:
  name:
    description: Only show results for a virtual network gateway connection.
    type: str
  resource_group:
    description: >
      Limit results by resource group. Required when filtering by name.
    type: str
  tags:
    description: >
      Limit results by providing a list of tags. Format tags as 'key'
      or 'key:value'.
    type: list
    elements: str
  ad_user:
    description: >
      Active Directory username. Use when authenticating with an Active
      Directory user rather than service principal.
    type: str
  adfs_authority_url:
    description: >
      Azure AD authority url. Use when authenticating with
      Username/password, and has your own ADFS authority.
    type: str
  api_profile:
    description: >
      Selects an API profile to use when communicating with Azure services.
      Default value of C(latest) is appropriate for public clouds; future
      values will allow use with Azure Stack.
    type: str
    default: latest
  auth_source:
    description: >
      Controls the source of the credentials to use for authentication.
    type: str
    choices: ['auto', 'cli', 'env', 'credential_file', 'msi']
    default: auto
  cert_validation_mode:
    description: >
      Controls the certificate validation behavior for Azure endpoints.
    type: str
    choices: ['validate', 'ignore']
  client_id:
    description: >
      Azure client ID. Use when authenticating with a Service Principal.
    type: str
  cloud_environment:
    description: >
      For cloud environments other than the US public cloud, the environment
      name (as defined by Azure Python SDK).
    type: str
    default: AzureCloud
  disable_instance_discovery:
    description: >
      Determines whether or not instance discovery is performed when
      attempting to authenticate. Setting this to true will completely
      disable both instance discovery and authority validation. This
      functionality is intended for use in scenarios where the metadata
      endpoint cannot be reached.
    type: bool
    default: false
  log_mode:
    description: Parent argument.
    type: str
  log_path:
    description: Parent argument.
    type: str
  password:
    description: >
      Active Directory user password. Use when authenticating with an Active
      Directory user rather than service principal.
    type: str
  profile:
    description: Security profile found in ~/.azure/credentials file.
    type: str
  secret:
    description: >
      Azure client secret. Use when authenticating with a Service Principal.
    type: str
  subscription_id:
    description: Your Azure subscription Id.
    type: str
  tenant:
    description: >
      Azure tenant ID. Use when authenticating with a Service Principal.
    type: str
  thumbprint:
    description: >
      The thumbprint of the private key specified in I(x509_certificate_path).
    type: str
  x509_certificate_path:
    description: >
      Path to the X509 certificate used to create the service principal
      in PEM format.
    type: path
"""

EXAMPLES = """
- name: Get facts for one virtual network connection
  network.vpn.azure_rm_virtualnetworkgatewayconnection_info:
    resource_group: myResourceGroup
    name: vpn-conn

- name: Get facts for all virtual network connections in a resource group
  network.vpn.azure_rm_virtualnetworkgatewayconnection_info:
    resource_group: myResourceGroup

- name: Get facts by tags
  network.vpn.azure_rm_virtualnetworkgatewayconnection_info:
    tags:
      - testing
"""
RETURN = """
  virtualnetworkgatewayconnections:
    description:
        - List of virtual network gateway connection dicts.
    returned: always
    type: list
    elements: dict
    contains:
      id:
        description: Resource ID of the virtual network gateway connection.
        type: str
      name:
        description: Name of virtual network gateway connection.
        type: str
      authorization_key:
        description: The authorization key.
        type: str
      connection_mode:
        description: >
          The connection mode for the virtual network gateway connection.
        type: str
      connection_type:
        description: The gateway connection type.
        type: str
      connection_protocol:
        description: Connection protocol used for this connection.
        type: str
        choices: ["IKEv2", "IKEv1"]
      connection_status:
        description:
          - The virtual network gateway connection status.
          - Returned when name of the connection is specified.
        type: str
      dpd_timeout_seconds:
        description: >
          The dead peer detection timeout of this connection in seconds.
        type: int
      enable_bgp:
        description: EnableBgp flag.
        type: bool
      express_route_gateway_bypass:
        description: Bypass ExpressRoute Gateway for data forwarding.
        type: bool
      local_network_gateway2:
        description: The name of the local network gateway resource.
        type: str
      location:
        description: >
          Valid Azure location. Defaults to location of the resource group.
        type: str
      provisioning_state:
        description: >
          The provisioning state for the virtual network gateway resource.
        type: str
      routing_weight:
        description: The routing weight.
        type: int
      shared_key:
        description: The IPSec shared key.
        type: str
      tags:
        description: Tags assigned to the resource. Dictionary of pairs.
        type: dict
      traffic_selector_policies:
        description: >
          The Traffic Selector Policies to be considered by this connection.
        type: list
      use_local_azure_ip_address:
        description: Use private local Azure IP for the connection.
        type: bool
      use_policy_based_traffic_selectors:
        description: Enable policy-based traffic selectors.
        type: bool
      virtual_network_gateway1:
        description: The virtual network gateway resource.
        type: dict
      virtual_network_gateway2:
        description: The virtual network gateway resource.
        type: dict
"""

try:
    from azure.core.exceptions import ResourceNotFoundError
except Exception:
    # This is handled in azure_rm_common
    pass

from ansible_collections.azure.azcollection.plugins.module_utils.azure_rm_common import (  # noqa: E501
    AzureRMModuleBase,
)


class AzureRMVirtualNetworkGatewayConnectionInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            name=dict(type="str"),
            resource_group=dict(type="str"),
            tags=dict(type="list", elements="str"),
        )

        self.results = dict(changed=False, virtualnetworkgatewayconnections=[])

        self.name = None
        self.resource_group = None
        self.tags = None

        super(AzureRMVirtualNetworkGatewayConnectionInfo, self).__init__(
            self.module_arg_spec,
            supports_check_mode=True,
            supports_tags=False,
            facts_module=True,
        )

    def exec_module(self, **kwargs):
        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        if self.name is not None:
            results = self.get_item()
        elif self.resource_group is not None:
            results = self.list_resource_group()

        self.results["virtualnetworkgatewayconnections"] = self.curated(
            results
        )

        return self.results

    def get_item(self):
        self.log("Get properties for {0}".format(self.name))
        item = None
        results = []

        try:
            item = (
                self.network_client.virtual_network_gateway_connections
                .get(self.resource_group, self.name)
            )
        except ResourceNotFoundError:
            pass

        if item and self.has_tags(item.tags, self.tags):
            results = [item]
        return results

    def list_resource_group(self):
        self.log("List items for resource group")
        try:
            response = (
                self.network_client.virtual_network_gateway_connections
                .list(self.resource_group)
            )
        except ResourceNotFoundError as exc:
            self.fail(
                "Failed to list for resource group {0} - {1}".format(
                    self.resource_group, str(exc)
                )
            )

        results = []
        for item in response:
            if self.has_tags(item.tags, self.tags):
                results.append(item)
        return results

    def curated(self, raws):
        self.log("Format all items")
        return [self.virtualnwgwconn_to_dict(x) for x in raws] if raws else []

    def virtualnwgwconn_to_dict(self, vngwconn):
        result = dict(
            authorization_key=vngwconn.authorization_key,
            connection_mode=vngwconn.connection_mode,
            connection_protocol=vngwconn.connection_protocol,
            connection_type=vngwconn.connection_type,
            dpd_timeout_seconds=vngwconn.dpd_timeout_seconds,
            etag=vngwconn.etag,
            enable_bgp=vngwconn.enable_bgp,
            express_route_gateway_bypass=vngwconn.express_route_gateway_bypass,
            id=vngwconn.id,
            ipsec_policies=vngwconn.ipsec_policies,
            location=vngwconn.location,
            name=vngwconn.name,
            provisioning_state=vngwconn.provisioning_state,
            routing_weight=vngwconn.routing_weight,
            shared_key=vngwconn.shared_key,
            tags=vngwconn.tags,
            traffic_selector_policies=vngwconn.traffic_selector_policies,
            use_local_azure_ip_address=vngwconn.use_local_azure_ip_address,
            use_policy_based_traffic_selectors=(
                vngwconn.use_policy_based_traffic_selectors
            ),
            virtual_network_gateway1=dict(
                id=vngwconn.virtual_network_gateway1.id
            ),
        )
        if vngwconn.connection_status:
            result["connection_status"] = vngwconn.connection_status
        if vngwconn.local_network_gateway2:
            result["local_network_gateway2"] = dict(
                id=vngwconn.local_network_gateway2.id
            )
        if vngwconn.virtual_network_gateway2:
            result["virtual_network_gateway2"] = dict(
                id=vngwconn.virtual_network_gateway2.id
            )
        return result


def main():
    AzureRMVirtualNetworkGatewayConnectionInfo()


if __name__ == "__main__":
    main()
