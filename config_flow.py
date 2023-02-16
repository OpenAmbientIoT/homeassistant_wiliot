"""Config flow for Wiliot Pixel"""
from twiliot import wiliot_client
import voluptuous as vol

from .const import DOMAIN

from homeassistant import config_entries
from homeassistant.const import CONF_URL, CONF_API_KEY, CONF_USERNAME, CONF_COUNT

#from .const import DOMAIN

DATA_SCHEMA = vol.Schema({
    vol.Required(CONF_URL): str,
    vol.Required(CONF_API_KEY): str,
    vol.Required(CONF_USERNAME): str,
    vol.Optional(CONF_COUNT): int
})


class AirtouchConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a Wiliot config flow."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle a flow initialized by the user."""
        if user_input is None:
            return self.async_show_form(step_id="user", data_schema=DATA_SCHEMA)

        errors = {}

        url = user_input[CONF_URL]
        api_key = user_input[CONF_API_KEY]
        username = user_input[CONF_USERNAME]
        max_pixels = user_input[CONF_COUNT]
        # I'm hoping that not forcing entries_match for max_pixels makes it optional...
        self._async_abort_entries_match({
            CONF_URL: url,
            CONF_API_KEY: api_key,
            CONF_USERNAME: username
        })

        wc = wiliot_client(url=url, api_key=api_key, username=username)
        wiliot_pixels = wc.get_pixels()

        if not wiliot_pixels:
            errors["base"] = "no_pixels"

        if errors:
            return self.async_show_form(
                step_id="user", data_schema=DATA_SCHEMA, errors=errors
            )

        return self.async_create_entry(
            title=user_input[CONF_USERNAME],
            data={
                CONF_URL: user_input[CONF_USERNAME]
                CONF_USERNAME: user_input[CONF_USERNAME]
            },
        )
