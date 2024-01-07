from collections import OrderedDict
import logging
import voluptuous as vol
from datetime import timedelta

from homeassistant import config_entries
from homeassistant.const import (
    DOMAIN,
    CONF_HOST,
    DATA_CRW,
    CONF_CODE,
    CONF_CROW_KEEPALIVE,
    CONF_CROW_PORT,
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
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.core import callback

from .const import DOMAIN, CONF_HOST, CONF_CROW_PORT, CONF_CODE, CONF_CROW_KEEPALIVE, CONF_AREAS, CONF_AREANAME, CONF_ZONES, CONF_ZONENAME, CONF_ZONETYPE,

_LOGGER = logging.getLogger(__name__)


@callback
def configured_accounts(hass):
    """Return tuple of configured host."""
    entries = hass.config_entries.async_entries(DOMAIN)
    if entries:
        return (entry.data[CONF_HOST] for entry in entries)
    return ()


@config_entries.HANDLERS.register(DOMAIN)
class crowConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    def __init__(self):
        """Initialize."""
        self._host = vol.UNDEFINED
        self._port = vol.UNDEFINED
        self._code = vol.UNDEFINED
        self._area = vol.UNDEFINED 
        self._skeepalive_interval = 60
        self._outputs = vol.UNDEFINED 

  

    async def async_step_user(self, user_input=None):
        """Handle a user initiated config flow."""
        errors = {}

        if user_input is not None:
            self._host = user_input[CONF_HOST]
            self._port = user_input[CONF_CROW_PORT]
            self._code = user_input.get(CONF_CODE)
            self._area = user_input.get(CONF_AREAS)
            self._keepalive_interval = user_input[CONF_CROW_KEEPALIVE]
            self._outputs = user_input.get(CONF_OUTPUTS)

            try:
                # pylint: disable=no-value-for-parameter
                #session = async_get_clientsession(self.hass)
                #connection = AudiConnectAccount(
                #    session=session,
                #    username=vol.Email()(self._username),
                #    password=self._password,
                #    country=self._region,
                #    spin=self._spin,
                #)

                #if await connection.try_login(False) == False:
                #    raise Exception(
                #        "Unexpected error communicating with the Audi server"
                #    )

            #except vol.Invalid:
            #    errors[CONF_USERNAME] = "invalid_username"
            #except Exception:
            #    errors["base"] = "invalid_credentials"
            #else:
            #    if self._username in configured_accounts(self.hass):
            #        errors["base"] = "user_already_configured"
                else:
                    return self.async_create_entry(
                        title=f"{self._host}",
                        data={
                            CONF_HOST: self._host,
                            CONF_CROW_PORT: self._port,
                            CONF_CODE: self._code,
                            CONF_AREAS: self._area,
                            CONF_CROW_KEEPALIVE: self._keepalive_interval,
                            CONF_OUTPUTS: self._outputs,
                        },
                    )

        data_schema = OrderedDict()
        data_schema[vol.Required(CONF_HOST, default=self._host)] = str
        data_schema[vol.Required(CROW_PORT, default=self._port)] = str
        data_schema[vol.Required(CONF_CODE, default=self._code)] = str
        data_schema[vol.Required(CONF_AREAS, default=self._area)] = str
        data_schema[
            vol.Optional(CONF_CROW_KEEPALIVE, default=DEFAULT_KEEPALIVE)
        ] = int

        return self.async_show_form(
            step_id="host",
            data_schema=vol.Schema(data_schema),
            errors=errors,
        )

    async def async_step_import(self, user_input):
        """Import a config flow from configuration."""
        host = user_input[CONF_HOST]
        port = user_input[CONF_CROW_PORT]

        code = user_input[CONF_CODE]
        if user_input.get(CONF_SPIN):
            spin = user_input[CONF_SPIN]

        area = "1"
        if user_input.get(CONF_AREAS):
            area = user_input.get(CONF_AREAS)

        keepalive_interval = 60

        if user_input.get(CONF_CROW_KEEPALIVE):
            keepalive_interval = user_input[CONF_CROW_KEEPALIVE]

        if keepalive_interval < 30:
            keepalive_interval = 30

        try:
           # session = async_get_clientsession(self.hass)
           # connection = AudiConnectAccount(
           #     session=session,
           #     username=username,
           #     password=password,
           #     country=region,
           #     spin=spin,
           # )

           # if await connection.try_login(False) == False:
           #     raise Exception("Unexpected error communicating with the Audi server")

        #except Exception:
        #    _LOGGER.error("Invalid credentials for %s", username)
        #    return self.async_abort(reason="invalid_credentials")

        return self.async_create_entry(
            title=f"{host} (from configuration)",
            data={
                CONF_HOST: host,
                CONF_CROW_PORT: port,
                CONF_AREA: area,
                CONF_CODE: code,
                CONF_CROW_KEEPALIVE: keepalive_interval,
            },
        )
