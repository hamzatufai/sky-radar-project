# Setup and AWS EC2 deployment guide

## 1. What you need

- Python 3.9 or newer
- Internet connection
- An OpenSky account only if you want authenticated API access
- For cloud deployment: an AWS account, an EC2 key pair, and the GitHub repository URL

## 2. Run locally on Windows

Open PowerShell in the project folder:

```powershell
.\scripts\setup.ps1
.\.venv\Scripts\Activate.ps1
Copy-Item .env.example .env
python -m opensky_radar.pipeline
python -m pytest
```

If PowerShell blocks the script, run this once in the current PowerShell window and retry:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

## 3. Run locally on macOS or Linux

```bash
chmod +x scripts/setup.sh
./scripts/setup.sh
source .venv/bin/activate
cp .env.example .env
python -m opensky_radar.pipeline
python -m pytest
```

## 4. Launch an Amazon Linux EC2 instance

In the AWS Console:

1. Open **EC2** and choose **Launch instance**.
2. Choose an **Amazon Linux 2023** AMI.
3. Choose a small instance suitable for a scheduled Python task, such as `t3.micro` where it is available.
4. Create or select a key pair and download the `.pem` file safely.
5. In the security group, allow inbound **SSH (TCP 22)** from **My IP** only. Do not open HTTP/HTTPS ports; this project is not a web server.
6. Launch the instance and copy its public IPv4 DNS name or public IPv4 address.

Stopping an EC2 instance stops instance-usage billing, but EBS storage can still have a charge. Terminating the instance deletes it permanently.

## 5. Connect to EC2 from Windows

In PowerShell, move to the folder containing your key, then connect. Replace the placeholders with your own values:

```powershell
ssh -i .\my-ec2-key.pem ec2-user@EC2_PUBLIC_DNS_OR_IP
```

If `ssh` is not available, install the Windows OpenSSH Client from Optional Features, then retry.

## 6. Install the project on EC2

Run these commands on the EC2 instance. Replace the repository URL if your repository address changes.

```bash
sudo dnf update -y
sudo dnf install -y git python3 python3-pip
git clone https://github.com/hamzatufai/sky-radar-project.git
cd sky-radar-project
python3 -m venv .venv
chmod +x scripts/setup.sh
./scripts/setup.sh
cp .env.example .env
python3 -m opensky_radar.pipeline
python3 -m pytest
```

The last two commands confirm that the pipeline runs and tests pass before scheduling it.

### Repair an existing Amazon Linux EC2 installation

If your instance shows `TypeError: unsupported operand type(s) for |`, it is using Python 3.9 with an older copy of this project. Update the project after you have pushed the Python 3.9 compatibility fix to GitHub:

```bash
cd ~/sky-radar-project
git pull --ff-only
./scripts/setup.sh
.venv/bin/python -m opensky_radar.pipeline
```

The project is compatible with Python 3.9 and newer after this update.

For an existing **Amazon Linux 2** instance, use `yum` instead of `dnf` when installing system packages:

```bash
sudo yum update -y
sudo yum install -y git python3 python3-pip
```

## 7. Add OpenSky credentials on EC2 (optional)

Only do this if you have OpenSky credentials. Do not commit this file to Git.

```bash
nano .env
```

Add your values:

```text
OPENSKY_USERNAME=your_username
OPENSKY_PASSWORD=your_password
REQUEST_TIMEOUT=30
```

Save with `Ctrl+O`, press `Enter`, then exit with `Ctrl+X`.

## 8. Schedule the pipeline every hour

Create the service file:

```bash
sudo nano /etc/systemd/system/opensky-radar.service
```

Paste this content. Change `/home/ec2-user/sky-radar-project` only if you cloned the project somewhere else.

```ini
[Unit]
Description=OpenSky Radar data pipeline
After=network-online.target
Wants=network-online.target

[Service]
Type=oneshot
User=ec2-user
WorkingDirectory=/home/ec2-user/sky-radar-project
ExecStart=/home/ec2-user/sky-radar-project/.venv/bin/python -m opensky_radar.pipeline
```

Create the timer file:

```bash
sudo nano /etc/systemd/system/opensky-radar.timer
```

Paste this content:

```ini
[Unit]
Description=Run OpenSky Radar pipeline every hour

[Timer]
OnCalendar=hourly
Persistent=true

[Install]
WantedBy=timers.target
```

Enable it and run it once now:

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now opensky-radar.timer
sudo systemctl start opensky-radar.service
sudo systemctl status opensky-radar.service --no-pager
systemctl list-timers opensky-radar.timer
```

## 9. Confirm EC2 output

```bash
cd ~/sky-radar-project
ls -lh data/processed/aircraft_states.csv
tail -n 20 logs/pipeline.log
sudo journalctl -u opensky-radar.service -n 50 --no-pager
```

Continue with [COMMANDS.md](COMMANDS.md) for day-to-day local and EC2 commands.
