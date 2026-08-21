# Pipeline architecture

```text
OpenSky API
    |
    v
client.py  -> downloads the aircraft state response
    |
    v
transform.py -> keeps and cleans useful fields
    |
    v
storage.py -> writes a CSV file and a log entry
    |
    v
data/processed/aircraft_states.csv
```

`pipeline.py` connects all parts. Keeping each job in a separate file makes the project easier to read, test, and improve.

## Data fields in the CSV

- `icao24`: unique aircraft identifier
- `callsign`: flight name when available
- `country`: aircraft origin country
- `longitude`, `latitude`: position
- `baro_altitude_m`: altitude in metres
- `velocity_mps`: speed in metres per second
- `heading_degrees`: direction of travel
- `on_ground`: whether the aircraft is on the ground
- `last_contact_utc`: time of the most recent signal
