"""Runtime configuration package for sandbox process.

Why:
    Owns validated immutable configuration snapshots for private runtime
    instances.
"""

from __future__ import annotations

from sandbox_process._internal.config.assembly import (
    build_default_config as build_default_config,
)
from sandbox_process._internal.config.models import (
    SampleLibConfig as _Config,
)
from sandbox_process._internal.config.state import (
    get_config as get_config,
    install_config as install_config,
)
from sandbox_process._internal.config.validation import (
    validate_config as validate_config,
)

SampleLibConfig = _Config
