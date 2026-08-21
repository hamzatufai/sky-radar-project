# Pipeline architecture

## Local pipeline

```text
OpenSky Network API
    |
    v
client.py       downloads aircraft state data
    |
    v
transform.py    keeps and cleans useful fields
    |
    v
storage.py      writes CSV output and a pipeline log
    |
    v
data/processed/aircraft_states.csv
```

`pipeline.py` connects each step. The small root-level `opensky_radar` folder makes this command work from the project folder:

```bash
python -m opensky_radar.pipeline
```

The full implementation remains organised in `src/opensky_radar`.

## AWS EC2 deployment architecture

```text
systemd timer (runs every hour)
    |
    v
opensky-radar.service
    |
    v
Python virtual environment (.venv)
    |
    v
OpenSky Radar pipeline
    |
    +--> data/processed/aircraft_states.csv
    +--> logs/pipeline.log
    +--> journalctl service logs
```

The timer starts the service once per hour. The service runs the pipeline once, saves the CSV, writes a log, and exits. No web application is exposed, so EC2 only needs SSH access for administration.

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
