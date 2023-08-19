# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

__metaclass__ = type


class ModuleDocFragment(object):
    OPTIONS_GUEST = r"""
options:
  name:
    description:
      - name of the guest VM being managed. Note that VM must be previously
        defined with xml.
      - This option is required unless I(command) is C(list_vms) or C(info).
    type: str
    aliases:
      - guest
      """

    OPTIONS_STATE = r"""
options:
  state:
    description:
      - Note that there may be some lag for state requests like C(shutdown)
        since these refer only to VM states. After starting a guest, it may not
        be immediately accessible.
        state and command are mutually exclusive except when command=list_vms. In
        this case all VMs in specified state will be listed.
    choices: [ destroyed, paused, running, shutdown ]
    type: str
    """

    OPTIONS_COMMAND = r"""
options:
  command:
    description:
      - In addition to state management, various non-idempotent commands are available.
    choices: [ create, define, destroy, freemem, get_xml, info, list_vms, nodeinfo, pause, shutdown, start, status, stop, undefine, unpause, virttype ]
    type: str
    """

    OPTIONS_AUTOSTART = r"""
options:
  autostart:
    description:
      - Start VM at host startup.
    type: bool
    """

    OPTIONS_URI = r"""
options:
  uri:
    description:
      - Libvirt connection uri.
    default: qemu:///system
    type: str
    """

    OPTIONS_XML = r"""
options:
  xml:
    description:
      - XML document used with the define command.
      - Must be raw XML content using C(lookup). XML cannot be reference to a file.
    type: str
    """
