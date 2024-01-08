from homeassistant import config_entries
from homeassistant.core import callback
from homeassistant.const import (
    CONF_HOST,
    CONF_PORT,
    CONF_CODE,
)

from .const import (
    DOMAIN,
    CONF_CROW_KEEPALIVE,
    CONF_AREANAME,
    CONF_AREAS,
    CONF_ZONENAME,
    CONF_ZONES,
    CONF_ZONETYPE,
    CONF_OUTPUTS,
    CONF_OUTPUTNAME,
    DEFAULT_PORT,
    DEFAULT_KEEPALIVE,
)

class CrowConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        errors = {}

        if user_input is not None:
            # TODO: Test entered CONF_HOST, CONF_PORT and CONF_CODE if it is working

            return self.async_create_entry(
                title=user_input[CONF_HOST], data=user_input
            )

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required(CONF_HOST): str,
                    vol.Required(CONF_PORT, default=DEFAULT_PORT): int,
                    vol.Required(CONF_CODE): str,
                }
            ),
            errors=errors,
        )

    async def async_step_confirm(self, user_input=None):
        if user_input is not None:
            # TODO: Test entered CONF_AREAS and CONF_ZONES if it is working

            return self.async_create_entry(
                title=user_input[CONF_AREANAME], data=user_input
            )

        return self.async_show_form(
            step_id="confirm",
            data_schema=vol.Schema(
                {
                    vol.Required(CONF_AREANAME): str,
                    vol.Required(CONF_AREAS): str,
                    vol.Required(CONF_ZONENAME): str,
                    vol.Required(CONF_ZONES): str,
                }
            ),
            errors=errors,
        )
