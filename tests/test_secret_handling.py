from __future__ import annotations

import json

from piphi_network_shelly.schemas import DeviceConfig
from piphi_network_shelly.state import _split_config, make_entry


def test_password_is_kept_out_of_persisted_and_serialized_config() -> None:
    config = DeviceConfig(id="shelly-test", host="shelly.local", password="top-secret")

    public, secrets = _split_config(config)
    entry = make_entry(config)

    assert "password" not in public
    assert secrets == {"password": "top-secret"}
    assert "top-secret" not in json.dumps(entry)
