from homeassistant import config_entries
from homeassistant.const import CONF_HOST, CONF_PORT, CONF_CODE
from .const import (
    DOMAIN,
    CONF_CROW_KEEPALIVE,
    CONF_AREAS,
    CONF_AREANAME,
    CONF_ZONES,
    CONF_ZONENAME,
    DEFAULT_PORT,
    DEFAULT_KEEPALIVE,
)

class CrowConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_UNKNOWN

    async def async_step_user(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(
                title=user_input[CONF_HOST],
                data={
                    CONF_HOST: user_input[CONF_HOST],
                    CONF_PORT: user_input.get(CONF_PORT, DEFAULT_PORT),
                    CONF_CODE: user_input[CONF_CODE],
                    CONF_CROW_KEEPALIVE: user_input.get(CONF_CROW_KEEPALIVE, DEFAULT_KEEPALIVE),
                    CONF_AREAS: user_input[CONF_AREAS],
                    CONF_AREANAME: user_input[CONF_AREANAME],
                    CONF_ZONES: user_input[CONF_ZONES],
                    CONF_ZONENAME: user_input[CONF_ZONENAME],
                },
            )

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required(CONF_HOST): str,
                    vol.Optional(CONF_PORT, default=DEFAULT_PORT): int,
                    vol.Required(CONF_CODE): str,
                    vol.Optional(CONF_CROW_KEEPALIVE, default=DEFAULT_KEEPALIVE): bool,
                    vol.Required(CONF_AREAS): list,
                    vol.Required(CONF_AREANAME): str,
                    vol.Required(CONF_ZONES): list,
                    vol.Required(CONF_ZONENAME): str,
                }
            ),
        )
