# Author: Felix Fontein <felix@fontein.de>
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or
# https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: 2020, Ansible Project

"""
YAML handling.
"""

from __future__ import annotations

from typing import Any

import yaml

_SafeLoader: Any
_SafeDumper: Any
try:
    # use C version if possible for speedup
    from yaml import CSafeDumper as _SafeDumper
    from yaml import CSafeLoader as _SafeLoader
except ImportError:
    from yaml import SafeDumper as _SafeDumper
    from yaml import SafeLoader as _SafeLoader


def load_yaml(path: str) -> Any:
    """
    Load and parse YAML file ``path``.
    """
    with open(path, 'rb') as stream:
        return yaml.load(stream, Loader=_SafeLoader)


def store_yaml(path: str, content: Any) -> None:
    """
    Store ``content`` as YAML file under ``path``.
    """
    with open(path, 'w', encoding='utf-8') as stream:
        dumper = _SafeDumper
        dumper.ignore_aliases = lambda *args: True
        yaml.dump(content, stream, default_flow_style=False, Dumper=dumper)
