# Project commands

Run local commands from the project root folder. Run EC2 commands after you connect to the Amazon Linux instance.

## Local commands

| Task | Windows PowerShell | macOS/Linux |
| --- | --- | --- |
| Create virtual environment and install packages | `.\scripts\setup.ps1` | `./scripts/setup.sh` |
| Activate environment | `.\.venv\Scripts\Activate.ps1` | `source .venv/bin/activate` |
| Create local settings file | `Copy-Item .env.example .env` | `cp .env.example .env` |
| Run pipeline | `python -m opensky_radar.pipeline` | `python3 -m opensky_radar.pipeline` |
| Run tests | `python -m pytest` | `python3 -m pytest` |
| Leave virtual environment | `deactivate` | `deactivate` |
| Update packages | `python -m pip install -r requirements.txt --upgrade` | `python3 -m pip install -r requirements.txt --upgrade` |
| View CSV output | `Get-Content data\processed\aircraft_states.csv -TotalCount 5` | `head -n 5 data/processed/aircraft_states.csv` |
| View pipeline log | `Get-Content logs\pipeline.log -Tail 30` | `tail -n 30 logs/pipeline.log` |

## EC2 deployment commands

Replace `EC2_PUBLIC_DNS_OR_IP`, `my-ec2-key.pem`, and the project folder if your names are different.

| Task | Command |
| --- | --- |
| Connect from Windows | `ssh -i .\my-ec2-key.pem ec2-user@EC2_PUBLIC_DNS_OR_IP` |
| Go to project | `cd ~/sky-radar-project` |
| Install dependencies | `./scripts/setup.sh` |
| Run once now | `.venv/bin/python -m opensky_radar.pipeline` |
| Run tests | `.venv/bin/python -m pytest` |
| Start hourly schedule | `sudo systemctl enable --now opensky-radar.timer` |
| Run scheduled service now | `sudo systemctl start opensky-radar.service` |
| Check service result | `sudo systemctl status opensky-radar.service --no-pager` |
| Check timer | `systemctl list-timers opensky-radar.timer` |
| Read service logs | `sudo journalctl -u opensky-radar.service -n 50 --no-pager` |
| Follow service logs live | `sudo journalctl -u opensky-radar.service -f` |
| Read CSV output | `head -n 5 data/processed/aircraft_states.csv` |
| Read local pipeline log | `tail -n 30 logs/pipeline.log` |
| Stop hourly schedule | `sudo systemctl disable --now opensky-radar.timer` |

## Update the project on EC2

Run these commands after pushing new code to GitHub:

```bash
cd ~/sky-radar-project
git pull --ff-only
./scripts/setup.sh
sudo systemctl daemon-reload
sudo systemctl start opensky-radar.service
sudo systemctl status opensky-radar.service --no-pager
```

## Output files

| File | Meaning |
| --- | --- |
| `data/processed/aircraft_states.csv` | Clean aircraft data from the latest run |
| `logs/pipeline.log` | A record of successful runs and errors |
