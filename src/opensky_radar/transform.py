"""Turn OpenSky state vectors into clear dictionary records."""

from datetime import UTC, datetime


def _utc_time(timestamp: object) -> str | None:
    if timestamp is None:
        return None
    return datetime.fromtimestamp(float(timestamp), UTC).isoformat()


def clean_aircraft_states(states: list[list[object]]) -> list[dict[str, object]]:
    """Keep fields that are useful for a simple radar dataset."""
    records: list[dict[str, object]] = []
    for state in states:
        if len(state) < 11:
            continue
        records.append(
            {
                "icao24": state[0],
                "callsign": state[1].strip() if isinstance(state[1], str) else None,
                "country": state[2],
                "last_contact_utc": _utc_time(state[4]),
                "longitude": state[5],
                "latitude": state[6],
                "baro_altitude_m": state[7],
                "on_ground": state[8],
                "velocity_mps": state[9],
                "heading_degrees": state[10],
            }
        )
    return records
