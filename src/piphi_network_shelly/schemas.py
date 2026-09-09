from __future__ import annotations

from pydantic import Field
from piphi_runtime_kit_python import RuntimeConfig


class DeviceConfig(RuntimeConfig):
    host: str
    alias: str | None = None
    username: str = "admin"
    password: str | None = None
    protocol: str = "http"
    actions_enabled: bool = False
    allowlisted_component_ids: list[str] = Field(default_factory=list)
