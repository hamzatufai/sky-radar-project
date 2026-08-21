"""Download aircraft state data from OpenSky."""

import requests

from .config import Settings


def fetch_aircraft_states(settings: Settings) -> list[list[object]]:
    """Return state-vector rows supplied by the OpenSky API."""
    response = requests.get(
        settings.api_url,
        timeout=settings.timeout_seconds,
        auth=settings.auth,
    )
    response.raise_for_status()
    payload = response.json()
    return payload.get("states") or []
