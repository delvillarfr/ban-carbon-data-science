from pathlib import Path

from ban_carbon_common.config import (
    DATA_DIR,
    MONOREPO_ROOT,
    PROCESSED_DATA_DIR,
    RAW_DATA_DIR,
)
from dotenv import load_dotenv
from loguru import logger

# Load project-specific environment variables
load_dotenv()

# Project paths - PROJ_ROOT is the project directory, not package directory
PROJ_ROOT = Path(__file__).resolve().parents[2]
logger.info(f"Project root: {PROJ_ROOT}")

REPORTS_DIR = PROJ_ROOT / "reports"
FIGURES_DIR = REPORTS_DIR / "figures"

__all__ = [
    # Project-specific paths
    "PROJ_ROOT",
    "REPORTS_DIR",
    "FIGURES_DIR",
    # Monorepo paths
    "MONOREPO_ROOT",
    "DATA_DIR",
    "RAW_DATA_DIR",
    "PROCESSED_DATA_DIR",
]
