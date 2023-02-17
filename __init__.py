"""The Wiliot integration."""
from __future__ import annotations

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant

from .const import DOMAIN

# TODO List the platforms that you want to support.
# For your initial PR, limit it to 1 platform.
PLATFORMS: list[Platform] = [Platform.SENSOR]


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Wiliot from a config entry."""

    hass.data.setdefault(DOMAIN, {})
    # TODO 1. Create API instance
    #myAPI = await hass.async_add_executor_job(
    #    wiliot_client(
    #        api_key = entry.data["password"],
    #        username = entry.data["username"]
    #    )
    #)
    myAPI = await hass.async_add_executor_job(
        PlatformClient(
            api_key = entry.data["password"],
            owner_id = entry.data["username"]
        )
    )
    # TODO 2. Validate the API connection (and authentication)
    assert not myAPI.client.auth_obj.token_expired()
    # TODO 3. Store an API object for your platforms to access
    hass.data[DOMAIN][entry.entry_id] = myAPI

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    if unload_ok := await hass.config_entries.async_unload_platforms(entry, PLATFORMS):
        hass.data[DOMAIN].pop(entry.entry_id)

    return unload_ok
