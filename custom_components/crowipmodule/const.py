
DOMAIN = "crowipmodule"

DATA_CRW = "crowipmodule"

CONF_CODE = "code"
CONF_CROW_KEEPALIVE = "keepalive_interval"
CONF_CROW_PORT = "port"
CONF_AREANAME = "name"
CONF_AREAS = "areas"
CONF_ZONENAME = "name"
CONF_ZONES = "zones"
CONF_ZONETYPE = "type"
CONF_OUTPUTS = "outputs"
CONF_OUTPUTNAME = "name"

DEFAULT_PORT = 5002
DEFAULT_KEEPALIVE = 60
"""CDEFAULT_KEEPALIVE = 60"""
DEFAULT_ZONETYPE = "opening"
DEFAULT_TIMEOUT = 10
"""DEFAULT_TIMEOUT = 10"""

SIGNAL_ZONE_UPDATE = "crowipmodule.zones_updated"
SIGNAL_AREA_UPDATE = "crowipmodule.areas_updated"
SIGNAL_SYSTEM_UPDATE = "crowipmodule.system_updated"
SIGNAL_OUTPUT_UPDATE = "crowipmodule.output_updated"
SIGNAL_KEYPAD_UPDATE = "crowipmodule.keypad_updated"
