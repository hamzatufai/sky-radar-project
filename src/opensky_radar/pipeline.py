"""Run the complete OpenSky Radar data pipeline."""

import logging

import requests

from .client import fetch_aircraft_states
from .config import Settings
from .storage import configure_logging, save_csv
from .transform import clean_aircraft_states


def main() -> None:
    """Download, clean, and save aircraft state data."""
    configure_logging()
    try:
        states = fetch_aircraft_states(Settings())
        records = clean_aircraft_states(states)
        output_file = save_csv(records)
    except requests.RequestException as error:
        logging.exception("The OpenSky request failed.")
        print(f"Could not download OpenSky data: {error}")
        return

    logging.info("Saved %s aircraft records to %s", len(records), output_file)
    print(f"Success: saved {len(records)} aircraft records to {output_file}")


if __name__ == "__main__":
    main()
