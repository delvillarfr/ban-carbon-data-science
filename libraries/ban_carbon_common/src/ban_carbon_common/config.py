from pathlib import Path

from loguru import logger

def get_monorepo_root(start_path: Path | None = None) -> Path:
    """
    Find monorepo root by looking for pyproject.toml with workspace config.

    Args:
        start_path: Starting directory for search (defaults to this file's location)

    Returns:
        Path to monorepo root directory

    Raises:
        RuntimeError: If monorepo root cannot be found
    """
    if start_path is None:
        start_path = Path(__file__).resolve().parent

    current = start_path.resolve()
    while current != current.parent:
        pyproject = current / "pyproject.toml"
        if pyproject.exists():
            content = pyproject.read_text()
            if "[tool.uv.workspace]" in content:
                return current
        current = current.parent

    raise RuntimeError("Could not find monorepo root with [tool.uv.workspace]")

# Shared paths at monorepo root
MONOREPO_ROOT = get_monorepo_root()
logger.info(f"Monorepo root: {MONOREPO_ROOT}")

SHARED_DATA_DIR = MONOREPO_ROOT / "data"
SHARED_RAW_DATA_DIR = SHARED_DATA_DIR / "raw"
SHARED_INTERIM_DATA_DIR = SHARED_DATA_DIR / "interim"
SHARED_PROCESSED_DATA_DIR = SHARED_DATA_DIR / "processed"
SHARED_EXTERNAL_DATA_DIR = SHARED_DATA_DIR / "external"

# Configure logger with tqdm integration
try:
    from tqdm import tqdm
    logger.remove(0)
    logger.add(lambda msg: tqdm.write(msg, end=""), colorize=True)
except ModuleNotFoundError:
    pass

__all__ = [
    "get_monorepo_root",
    "MONOREPO_ROOT",
    "SHARED_DATA_DIR",
    "SHARED_RAW_DATA_DIR",
    "SHARED_INTERIM_DATA_DIR",
    "SHARED_PROCESSED_DATA_DIR",
    "SHARED_EXTERNAL_DATA_DIR",
]
