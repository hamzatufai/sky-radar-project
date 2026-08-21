"""Local entry point for the source package.

This file lets `python -m opensky_radar.pipeline` work directly from the
project folder while the implementation remains organised in `src/`.
"""

from pathlib import Path


_SOURCE_PACKAGE = Path(__file__).resolve().parent.parent / "src" / "opensky_radar"
__path__.append(str(_SOURCE_PACKAGE))
__version__ = "0.1.0"
