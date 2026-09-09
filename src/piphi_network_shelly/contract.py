from __future__ import annotations

from typing import Any

ENDPOINTS = {
    "health": "/health",
    "diagnostics": "/diagnostics",
    "discover": "/discover",
    "entities": "/entities",
    "state": "/state",
    "config": "/config",
    "config_sync": "/config/sync",
    "deconfigure": "/deconfigure",
    "ui_config": "/ui-config",
    "events": "/events",
    "command": "/command",
}

REQUIRED_ENDPOINTS = ["health", "entities", "command", "config", "ui_config"]

CAPABILITIES: dict[str, dict[str, Any]] = {
    "connected": {"kind": "sensor", "unit": "bool"},
    "refresh": {"kind": "action"},
}

COMMANDS: dict[str, dict[str, Any]] = {
    "refresh": {
        "description": "Refresh the integration state.",
        "timeout_ms": 5000,
    },
}

CONFIG_SCHEMA: dict[str, Any] = {
    "schema": {
        "title": "PiPhi Network Shelly Setup",
        "type": "object",
        "required": ["host"],
        "properties": {
    "host": {
        "type": "string",
        "title": "Device Address"
    },
    "alias": {
        "type": "string",
        "title": "Device Name"
    },
    "username": {
        "type": "string",
        "title": "Username",
        "default": "admin"
    },
    "password": {
        "type": "string",
        "title": "Password",
        "format": "password",
        "writeOnly": True
    },
    "protocol": {
        "type": "string",
        "title": "RPC Transport",
        "enum": [
            "http",
            "mqtt"
        ],
        "default": "http"
    },
    "actions_enabled": {
        "type": "boolean",
        "title": "Enable Mutating Actions",
        "default": False
    },
    "allowlisted_component_ids": {
        "type": "array",
        "title": "Allowed Component IDs",
        "items": {
            "type": "string"
        },
        "default": []
    }
},
    },
    "uiSchema": {
        "host": {"placeholder": "192.168.1.50"},
        "alias": {"placeholder": "Shelly Device"},
    },
}

FALLBACK_ENTITY: dict[str, Any] = {
    "id": "shelly-device",
    "name": "Shelly Device",
    "device_id": "shelly-device",
    "entity_type": "shelly_device",
    "capabilities": ["connected", "refresh"],
    "available_commands": [
        {"id": "refresh", "label": "Refresh", "kind": "action"},
    ],
    "dashboard": {
        "allowed_widgets": [
    "tile",
    "light-card",
    "cover-card",
    "sensor-card",
    "energy-flow"
],
        "default_widget": "tile",
    },
}
