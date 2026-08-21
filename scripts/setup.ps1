$ErrorActionPreference = "Stop"
if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    throw "Python was not found. Install Python 3.10 or newer, then run this script again."
}
python -m venv .venv
& .\.venv\Scripts\python.exe -m pip install --upgrade pip
& .\.venv\Scripts\python.exe -m pip install -r requirements.txt
Write-Host "Setup complete. Next run: .\.venv\Scripts\Activate.ps1"
