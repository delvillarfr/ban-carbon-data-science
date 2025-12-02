from pathlib import Path

from ban_carbon_common.config import (
    MONOREPO_ROOT,
    SHARED_DATA_DIR,
    SHARED_EXTERNAL_DATA_DIR,
    SHARED_INTERIM_DATA_DIR,
    SHARED_PROCESSED_DATA_DIR,
    SHARED_RAW_DATA_DIR,
)
from dotenv import load_dotenv
from loguru import logger

# Load project-specific environment variables
load_dotenv()

# Project paths - PROJ_ROOT is the project directory, not package directory
PROJ_ROOT = Path(__file__).resolve().parents[2]
logger.info(f"Project root: {PROJ_ROOT}")

DATA_DIR = PROJ_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
INTERIM_DATA_DIR = DATA_DIR / "interim"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
EXTERNAL_DATA_DIR = DATA_DIR / "external"

MODELS_DIR = PROJ_ROOT / "models"
REPORTS_DIR = PROJ_ROOT / "reports"
FIGURES_DIR = REPORTS_DIR / "figures"

__all__ = [
    # Project-specific paths
    "PROJ_ROOT",
    "DATA_DIR",
    "RAW_DATA_DIR",
    "INTERIM_DATA_DIR",
    "PROCESSED_DATA_DIR",
    "EXTERNAL_DATA_DIR",
    "MODELS_DIR",
    "REPORTS_DIR",
    "FIGURES_DIR",
    # Shared paths from library
    "MONOREPO_ROOT",
    "SHARED_DATA_DIR",
    "SHARED_RAW_DATA_DIR",
    "SHARED_INTERIM_DATA_DIR",
    "SHARED_PROCESSED_DATA_DIR",
    "SHARED_EXTERNAL_DATA_DIR",
]
