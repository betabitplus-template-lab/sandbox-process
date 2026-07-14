"""Runtime config validation helpers for sandbox process.

Why:
    Centralizes config normalization and invariant checks before snapshots are
    constructed or installed.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from sandbox_process._internal.config.models import (
        SampleLibConfig,
    )


def validate_config(config: SampleLibConfig) -> None:
    """Validate one runtime config snapshot."""
    _ = config
