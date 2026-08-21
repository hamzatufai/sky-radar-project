from opensky_radar.transform import clean_aircraft_states


def test_clean_aircraft_states_keeps_useful_fields() -> None:
    state = [
        "abc123", " TEST123 ", "Pakistan", 1_700_000_000, 1_700_000_001,
        67.001, 24.860, 1000.0, False, 220.5, 180.0,
    ]

    records = clean_aircraft_states([state])

    assert records[0]["icao24"] == "abc123"
    assert records[0]["callsign"] == "TEST123"
    assert records[0]["latitude"] == 24.860
    assert records[0]["last_contact_utc"] == "2023-11-14T22:13:21+00:00"


def test_clean_aircraft_states_skips_short_rows() -> None:
    assert clean_aircraft_states([["too", "short"]]) == []
