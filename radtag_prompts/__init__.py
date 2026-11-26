"""RadTag prompt texts.

This package re-exports the newest prompt version shipped with it.  Prompt
modules are named ``v<major>_<minor>`` (for example ``v1_1``); when a new
version module is added, it becomes the default on the next install without
editing this file.  Older versions stay importable explicitly, for example
``from radtag_prompts.v1_0 import SYSTEM``.
"""

import re as _re
from importlib import import_module as _import_module
from pkgutil import iter_modules as _iter_modules


def _latest_prompt_module() -> str:
    """Return the name of the highest ``v<major>_<minor>`` module."""
    versions = []
    for info in _iter_modules(__path__):
        match = _re.fullmatch(r"v(\d+)_(\d+)", info.name)
        if match is not None:
            versions.append((tuple(int(part) for part in match.groups()), info.name))
    if not versions:
        raise ImportError("radtag_prompts: no prompt version modules found")
    return max(versions)[1]


_current = _latest_prompt_module()
_prompts = _import_module(f".{_current}", __name__)
globals()[_current] = _prompts

__version__ = getattr(_prompts, "__version__", _current[1:].replace("_", "."))

_exported = tuple(getattr(_prompts, "__all__", ()))
__all__ = ["__version__", _current, *_exported]
globals().update({_name: getattr(_prompts, _name) for _name in _exported})
