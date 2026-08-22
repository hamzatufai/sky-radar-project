"""Project settings read from environment variables."""

from dataclasses import dataclass
import os
from typing import Optional, Tuple

from dotenv import load_dotenv


load_dotenv()


@dataclass(frozen=True)
class Settings:
    """Settings needed to call the OpenSky API."""

    api_url: str = "https://opensky-network.org/api/states/all"
    timeout_seconds: int = int(os.getenv("REQUEST_TIMEOUT", "30"))
    username: Optional[str] = os.getenv("OPENSKY_USERNAME") or None
    password: Optional[str] = os.getenv("OPENSKY_PASSWORD") or None

    @property
    def auth(self) -> Optional[Tuple[str, str]]:
        """Return login details only when both values are present."""
        if self.username and self.password:
            return self.username, self.password
        return None
