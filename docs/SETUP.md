# Setup guide

## What you need

- Python 3.10 or newer
- Internet connection
- PowerShell on Windows, or a terminal on macOS/Linux

## Windows setup

Open PowerShell in the project folder and run:

```powershell
.\scripts\setup.ps1
```

This creates `.venv` and installs all packages.

Activate the environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

Create your local settings file:

```powershell
Copy-Item .env.example .env
```

Run the pipeline:

```powershell
python -m opensky_radar.pipeline
```

## macOS/Linux setup

```bash
./scripts/setup.sh
source .venv/bin/activate
cp .env.example .env
python -m opensky_radar.pipeline
```

## If PowerShell blocks the setup script

Run this once for the current PowerShell window, then run the setup script again:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```
