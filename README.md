# OpenSky Radar Pipeline

A simple Python project that downloads aircraft data from the OpenSky Network, cleans it, and saves it as a CSV file.

## What this project does

1. Downloads live aircraft state data from the OpenSky Network API.
2. Keeps useful fields: aircraft ID, flight name, location, altitude, speed, and time.
3. Saves clean data in `data/processed/aircraft_states.csv`.
4. Writes run messages to `logs/pipeline.log`.

## Project structure

```text
open-skyradar/
├── .gitignore                    # Files Git will not track
├── .env.example                  # Safe example settings
├── README.md                     # Project overview and quick start
├── requirements.txt              # Python packages to install
├── pyproject.toml                # Package and test settings
├── data/
│   ├── raw/                      # Original API data (kept local)
│   └── processed/                # Clean CSV output
├── docs/
│   ├── ARCHITECTURE.md           # How the pipeline works
│   ├── COMMANDS.md               # Every project command
│   └── SETUP.md                  # Installation guide
├── logs/                         # Run logs (kept local)
├── scripts/
│   ├── setup.ps1                 # Windows setup script
│   └── setup.sh                  # macOS/Linux setup script
├── src/
│   └── opensky_radar/
│       ├── __init__.py           # Package version
│       ├── client.py             # OpenSky API request
│       ├── config.py             # Environment settings
│       ├── pipeline.py           # Main workflow
│       ├── storage.py            # CSV and log writing
│       └── transform.py          # Data cleaning
└── tests/
    └── test_transform.py         # Data-cleaning tests
```

## Quick start (Windows)

```powershell
.\scripts\setup.ps1
.\.venv\Scripts\Activate.ps1
Copy-Item .env.example .env
python -m opensky_radar.pipeline
```

After the run, open `data/processed/aircraft_states.csv`.

For all commands and detailed steps, read [docs/COMMANDS.md](docs/COMMANDS.md) and [docs/SETUP.md](docs/SETUP.md).

## Important notes

- The public OpenSky endpoint can limit requests. Wait a little and run again if it returns an error.
- Do not put passwords or API secrets in the README. Use `.env` instead.
- This starter project works without an OpenSky account. Add account details to `.env` only if you later need authenticated access.
