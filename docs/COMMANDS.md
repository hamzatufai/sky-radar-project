# Project commands

Run these commands from the project root folder.

| Task | Windows PowerShell | macOS/Linux |
| --- | --- | --- |
| Create virtual environment and install packages | `.\scripts\setup.ps1` | `./scripts/setup.sh` |
| Activate environment | `.\.venv\Scripts\Activate.ps1` | `source .venv/bin/activate` |
| Create local settings file | `Copy-Item .env.example .env` | `cp .env.example .env` |
| Run pipeline | `python -m opensky_radar.pipeline` | `python -m opensky_radar.pipeline` |
| Run tests | `python -m pytest` | `python -m pytest` |
| Leave virtual environment | `deactivate` | `deactivate` |
| Update packages | `python -m pip install -r requirements.txt --upgrade` | `python -m pip install -r requirements.txt --upgrade` |

## Output files

| File | Meaning |
| --- | --- |
| `data/processed/aircraft_states.csv` | Clean aircraft data from the latest run |
| `logs/pipeline.log` | Record of successful runs and errors |
