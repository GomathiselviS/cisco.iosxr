#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the resource
#   module builder playbook.
#
# Do not edit this file manually.
#
# Changes to this file will be over written
#   by the resource module builder.
#
# Changes should be made in the model used to
#   generate this file or in the resource module
#   builder template.
#
#############################################

"""
The module file for iosxr_lacp_interfaces
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "network",
}

DOCUMENTATION = """module: iosxr_lacp_interfaces
short_description: LACP interfaces resource module.
description:
- This module manages Link Aggregation Control Protocol (LACP) attributes of interfaces
  on IOS-XR devices.
version_added: 1.0.0
notes:
- Tested against IOS-XR 6.1.3.
- This module works with connection C(network_cli). See L(the IOS-XR Platform Options,../network/user_guide/platform_iosxr.html).
author: Nilashish Chakraborty (@nilashishc)
options:
  config:
    description: A dictionary of LACP interfaces options.
    type: list
    suboptions:
      name:
        description:
        - Name/Identifier of the interface or Ether-Bundle.
        type: str
      churn_logging:
        description:
        - Specifies the parameter for logging of LACP churn events.
        - Valid only for ether-bundles.
        - Mode 'actor' logs actor churn events only.
        - Mode 'partner' logs partner churn events only.
        - Mode 'both' logs actor and partner churn events only.
        type: str
        choices:
        - actor
        - partner
        - both
      collector_max_delay:
        description:
        - Specifies the collector max delay to be signaled to the LACP partner.
        - Valid only for ether-bundles.
        - Refer to vendor documentation for valid values.
        type: int
      period:
        description:
        - Specifies the rate at which packets are sent or received.
        - For ether-bundles, this specifies the period to be used by its member links.
        - Refer to vendor documentation for valid values.
        type: int
      switchover_suppress_flaps:
        description:
        - Specifies the time for which to suppress flaps during a LACP switchover.
        - Valid only for ether-bundles.
        - Refer to vendor documentation for valid values.
        type: int
      system:
        description:
        - This dict object contains configurable options related to LACP system parameters
          for ether-bundles.
        type: dict
        suboptions:
          priority:
            description:
            - Specifies the system priority to use in LACP negotiations for the bundle.
            - Refer to vendor documentation for valid values.
            type: int
          mac:
            description:
            - Specifies the system ID to use in LACP negotiations for the bundle,
              encoded as a MAC address.
            type: str
  running_config:
    description:
      - This option is used only with state I(parsed).
      - The value of this option should be the output received from the IOS-XR device by executing
        the command B(show running-config int).
      - The state I(parsed) reads the configuration from C(running_config) option and transforms
        it into Ansible structured data as per the resource module's argspec and the value is then
        returned in the I(parsed) key within the result.
    type: str
  state:
    description:
    - The state of the configuration after module completion.
    type: str
    choices:
    - merged
    - replaced
    - overridden
    - deleted
    default: merged
"""
EXAMPLES = """
# Using merged
#
#
# ------------
# Before state
# ------------
#
#
#
# RP/0/0/CPU0:an-iosxr#sh running-config interface
# Sun Jul 21 18:01:35.079 UTC
# interface Bundle-Ether10
# !
# interface Bundle-Ether11
# !
# interface Bundle-Ether12
# !
# interface Loopback888
#  description test for ansible
#  shutdown
# !
# interface MgmtEth0/0/CPU0/0
#  ipv4 address 192.0.2.11 255.255.255.0
# !
# interface GigabitEthernet0/0/0/1
#  description 'GigabitEthernet - 1'
# !
# interface GigabitEthernet0/0/0/2
#  description "GigabitEthernet - 2"
# !
# interface GigabitEthernet0/0/0/3
#  description "GigabitEthernet - 3"
# !
# interface GigabitEthernet0/0/0/4
#  description "GigabitEthernet - 4"
# !
#
#

 - name: Merge provided configuration with device configuration
   cisco.iosxr.iosxr_lacp_interfaces:
    config:
      - name: Bundle-Ether10
        churn_logging: actor
        collector_max_delay: 100
        switchover_suppress_flaps: 500

      - name: Bundle-Ether11
        system:
          mac: 00c2.4c00.bd15

      - name: GigabitEthernet0/0/0/1
        period: 200
    state: merged

#
#
# -----------
# After state
# -----------
#
#
# RP/0/0/CPU0:an-iosxr#sh run int
# Sun Jul 21 18:24:52.413 UTC
# interface Bundle-Ether10
#  lacp churn logging actor
#  lacp switchover suppress-flaps 500
#  lacp collector-max-delay 100
# !
# interface Bundle-Ether11
#  lacp system mac 00c2.4c00.bd15
# !
# interface Bundle-Ether12
# !
# interface Loopback888
#  description test for ansible
#  shutdown
# !
# interface MgmtEth0/0/CPU0/0
#  ipv4 address 192.0.2.11 255.255.255.0
# !
# interface GigabitEthernet0/0/0/1
#  description 'GigabitEthernet - 1"
#  lacp period 200
# !
# interface GigabitEthernet0/0/0/2
#  description "GigabitEthernet - 2"
# !
# interface GigabitEthernet0/0/0/3
#  description "GigabitEthernet - 3"
# !
# interface GigabitEthernet0/0/0/4
#  description "GigabitEthernet - 4"
# !
#


# Using replaced
#
#
# ------------
# Before state
# ------------
#
#
# RP/0/0/CPU0:an-iosxr#sh run int
# Sun Jul 21 18:24:52.413 UTC
# interface Bundle-Ether10
#  lacp churn logging actor
#  lacp switchover suppress-flaps 500
#  lacp collector-max-delay 100
# !
# interface Bundle-Ether11
#  lacp system mac 00c2.4c00.bd15
# !
# interface Bundle-Ether12
# !
# interface Loopback888
#  description test for ansible
#  shutdown
# !
# interface MgmtEth0/0/CPU0/0
#  ipv4 address 192.0.2.11 255.255.255.0
# !
# interface GigabitEthernet0/0/0/1
#  description 'GigabitEthernet - 1"
#  lacp period 200
# !
# interface GigabitEthernet0/0/0/2
#  description "GigabitEthernet - 2"
# !
# interface GigabitEthernet0/0/0/3
#  description "GigabitEthernet - 3"
# !
# interface GigabitEthernet0/0/0/4
#  description "GigabitEthernet - 4"
# !
#

 - name: Replace LACP configuration of listed interfaces with provided configuration
   cisco.iosxr.iosxr_lacp_interfaces:
    config:
      - name: Bundle-Ether10
        churn_logging: partner

      - name: GigabitEthernet0/0/0/2
        period: 300
    state: replaced

#
#
# -----------
# After state
# -----------
#
#
# RP/0/0/CPU0:an-iosxr#sh run int
# Sun Jul 21 18:50:21.929 UTC
# interface Bundle-Ether10
#  lacp churn logging partner
# !
# interface Bundle-Ether11
#  lacp system mac 00c2.4c00.bd15
# !
# interface Bundle-Ether12
# !
# interface Loopback888
#  description test for ansible
#  shutdown
# !
# interface MgmtEth0/0/CPU0/0
#  ipv4 address 192.0.2.11 255.255.255.0
# !
# interface GigabitEthernet0/0/0/1
#  description 'GigabitEthernet - 1"
#  lacp period 200
# !
# interface GigabitEthernet0/0/0/2
#  description "GigabitEthernet - 2"
#  lacp period 300
# !
# interface GigabitEthernet0/0/0/3
#  description "GigabitEthernet - 3"
# !
# interface GigabitEthernet0/0/0/4
#  description "GigabitEthernet - 4"
# !
#
#


# Using overridden
#
#
# ------------
# Before state
# ------------
#
#
# RP/0/0/CPU0:an-iosxr#sh run int
# Sun Jul 21 18:24:52.413 UTC
# interface Bundle-Ether10
#  lacp churn logging actor
#  lacp switchover suppress-flaps 500
#  lacp collector-max-delay 100
# !
# interface Bundle-Ether11
#  lacp system mac 00c2.4c00.bd15
# !
# interface Bundle-Ether12
# !
# interface Loopback888
#  description test for ansible
#  shutdown
# !
# interface MgmtEth0/0/CPU0/0
#  ipv4 address 192.0.2.11 255.255.255.0
# !
# interface GigabitEthernet0/0/0/1
#  description 'GigabitEthernet - 1"
#  lacp period 200
# !
# interface GigabitEthernet0/0/0/2
#  description "GigabitEthernet - 2"
#  lacp period 200
# !
# interface GigabitEthernet0/0/0/3
#  description "GigabitEthernet - 3"
# !
# interface GigabitEthernet0/0/0/4
#  description "GigabitEthernet - 4"
# !
#
#

 - name: Override all interface LACP configuration with provided configuration
   cisco.iosxr.iosxr_lacp_interfaces:
    config:
      - name: Bundle-Ether12
        churn_logging: both
        collector_max_delay: 100
        switchover_suppress_flaps: 500

      - name: GigabitEthernet0/0/0/1
        period: 300
    state: overridden

#
#
# -----------
# After state
# -----------
#
#
# RP/0/0/CPU0:an-iosxr(config-if)#do sh run int
# Sun Jul 21 19:32:36.115 UTC
# interface Bundle-Ether10
# !
# interface Bundle-Ether11
# !
# interface Bundle-Ether12
#  lacp churn logging both
#  lacp switchover suppress-flaps 500
#  lacp collector-max-delay 100
# !
# interface Loopback888
#  description test for ansible
#  shutdown
# !
# interface MgmtEth0/0/CPU0/0
#  ipv4 address 192.0.2.11 255.255.255.0
# !
# interface GigabitEthernet0/0/0/1
#  description 'GigabitEthernet - 1"
#  lacp period 300
# !
# interface GigabitEthernet0/0/0/2
#  description "GigabitEthernet - 2"
# !
# interface GigabitEthernet0/0/0/3
#  description "GigabitEthernet - 3"
# !
# interface GigabitEthernet0/0/0/4
#  description "GigabitEthernet - 4"
# !
#


# Using deleted
#
#
# ------------
# Before state
# ------------
#
#
# RP/0/0/CPU0:an-iosxr#sh run int
# Sun Jul 21 18:24:52.413 UTC
# interface Bundle-Ether10
#  lacp churn logging actor
#  lacp switchover suppress-flaps 500
#  lacp collector-max-delay 100
# !
# interface Bundle-Ether11
#  lacp non-revertive
# !
# interface Bundle-Ether12
# !
# interface Loopback888
#  description test for ansible
#  shutdown
# !
# interface MgmtEth0/0/CPU0/0
#  ipv4 address 192.0.2.11 255.255.255.0
# !
# interface GigabitEthernet0/0/0/1
#  description 'GigabitEthernet - 1"
#  lacp period 200
# !
# interface GigabitEthernet0/0/0/2
#  description "GigabitEthernet - 2"
#   lacp period 300
# !
# interface GigabitEthernet0/0/0/3
#  description "GigabitEthernet - 3"
# !
# interface GigabitEthernet0/0/0/4
#  description "GigabitEthernet - 4"
# !
#

 - name: Deleted LACP configurations of provided interfaces (Note - This won't delete the interface itself)
   cisco.iosxr.iosxr_lacp_interfaces:
    config:
      - name: Bundle-Ether10
      - name: Bundle-Ether11
      - name: GigabitEthernet0/0/0/1
      - name: GigabitEthernet0/0/0/2
    state: deleted

#
#
# -----------
# After state
# -----------
#
#
# Using parsed:

# parsed.cfg
# interface Bundle-Ether10
#  lacp churn logging actor
#  lacp switchover suppress-flaps 500
#  lacp collector-max-delay 100
# !
# interface Bundle-Ether11
#  lacp system mac 00c2.4c00.bd15
# !
# interface MgmtEth0/0/CPU0/0
#  ipv4 address 192.0.2.11 255.255.255.0
# !
# interface GigabitEthernet0/0/0/1
#  lacp period 200
# !
#

- name: Convert lacp interfaces config to argspec without connecting to the appliance
    cisco.iosxr.iosxr_lacp_interfaces:
      running_config: "{{ lookup('file', './parsed.cfg') }}"

# --------------
# Output:
# --------------

#    parsed:
#      - name: Bundle-Ether10
#        churn_logging: actor
#        collector_max_delay: 100
#        switchover_suppress_flaps: 500
#
#      - name: Bundle-Ether11
#        system:
#          mac: 00c2.4c00.bd15
#
#      - name: GigabitEthernet0/0/0/1
#        period: 200
#
#

# Using gathered:

# Native config:
# interface Bundle-Ether10
#  lacp churn logging actor
#  lacp switchover suppress-flaps 500
#  lacp collector-max-delay 100
# !
# interface Bundle-Ether11
#  lacp system mac 00c2.4c00.bd15
# !
# interface MgmtEth0/0/CPU0/0
#  ipv4 address 192.0.2.11 255.255.255.0
# !
# interface GigabitEthernet0/0/0/1
#  lacp period 200
# !
#

- name: Gather IOSXR lacp interfaces configuration
  cisco.iosxr.iosxr_lacp_interfaces:
    config:
    state: gathered

# ----------
# Output
# ---------
#    gathered:
#      - name: Bundle-Ether10
#        churn_logging: actor
#        collector_max_delay: 100
#        switchover_suppress_flaps: 500
#
#      - name: Bundle-Ether11
#        system:
#          mac: 00c2.4c00.bd15
#
#      - name: GigabitEthernet0/0/0/1
#        period: 200

# Using rendered:

 - name: Render platform specific commands from task input using rendered state
   cisco.iosxr.iosxr_lacp_interfaces:
    config:
      - name: Bundle-Ether10
        churn_logging: actor
        collector_max_delay: 100
        switchover_suppress_flaps: 500

      - name: Bundle-Ether11
        system:
          mac: 00c2.4c00.bd15

      - name: GigabitEthernet0/0/0/1
        period: 200
    state: rendered

# -------------
# Output
# -------------
# rendered: [
#     - "interface Bundle-Ether10"
#     - " lacp churn logging actor"
#     - " lacp switchover suppress-flaps 500"
#     - " lacp collector-max-delay 100"
#     - "interface Bundle-Ether11"
#     - " lacp system mac 00c2.4c00.bd15"
#     - "interface MgmtEth0/0/CPU0/0"
#     - " ipv4 address 192.0.2.11 255.255.255.0"
#     - "interface GigabitEthernet0/0/0/1"
#     - " lacp period 200"
#


"""
RETURN = """
before:
  description: The configuration as structured data prior to module invocation.
  returned: always
  type: list
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
after:
  description: The configuration as structured data after module completion.
  returned: when changed
  type: list
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
commands:
  description: The set of commands pushed to the remote device.
  returned: always
  type: list
  sample: ['interface Bundle-Ether10', 'lacp churn logging partner', 'lacp period 150']
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.argspec.lacp_interfaces.lacp_interfaces import (
    Lacp_interfacesArgs,
)
from ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.config.lacp_interfaces.lacp_interfaces import (
    Lacp_interfaces,
)


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    required_if = [
        ("state", "merged", ("config",)),
        ("state", "replaced", ("config",)),
        ("state", "overridden", ("config",)),
        ("state", "rendered", ("config",)),
        ("state", "parsed", ("running_config",)),
    ]

    mutually_exclusive = [("config", "running_config")]
    module = AnsibleModule(
        argument_spec=Lacp_interfacesArgs.argument_spec,
        required_if=required_if,
        supports_check_mode=True,
        mutually_exclusive=mutually_exclusive,
    )

    result = Lacp_interfaces(module).execute_module()
    module.exit_json(**result)


if __name__ == "__main__":
    main()
