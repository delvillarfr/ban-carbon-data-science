"""
Shared data I/O utilities with validation.

This module provides reusable functions for loading and processing
geospatial and tabular data with pandera validation.
"""
from pathlib import Path

import geopandas
from loguru import logger


def load_world_boundaries(raw_dir: Path, processed_dir: Path, force: bool = False) -> geopandas.GeoDataFrame:
    """
    Load world country boundaries, processing if necessary.

    Args:
        raw_dir: Directory containing raw geoBoundariesCGAZ_ADM0 files
        processed_dir: Directory for processed output
        force: If True, reprocess even if processed file exists

    Returns:
        GeoDataFrame with world boundaries in EPSG:4326
    """
    fname = "geoBoundariesCGAZ_ADM0"
    processed_path = processed_dir / fname

    if processed_path.exists() and not force:
        logger.info(f"Loading processed {fname}")
        return geopandas.read_file(processed_path)

    logger.info(f"Processing {fname}")
    gdf = geopandas.read_file(raw_dir / fname)
    gdf = gdf.to_crs("EPSG:4326")
    gdf.to_file(processed_path)

    return gdf


__all__ = [
    "load_world_boundaries",
]
