"""Save pipeline output and run messages."""

import csv
import logging
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]
OUTPUT_FILE = PROJECT_ROOT / "data" / "processed" / "aircraft_states.csv"
LOG_FILE = PROJECT_ROOT / "logs" / "pipeline.log"


def configure_logging() -> None:
    """Write timestamped messages to the local log file."""
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        force=True,
    )


def save_csv(records: list[dict[str, object]]) -> Path:
    """Save records to CSV and return the output path."""
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "icao24", "callsign", "country", "last_contact_utc", "longitude",
        "latitude", "baro_altitude_m", "on_ground", "velocity_mps", "heading_degrees",
    ]
    with OUTPUT_FILE.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)
    return OUTPUT_FILE
