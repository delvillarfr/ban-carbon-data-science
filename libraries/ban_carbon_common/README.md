# Ban Carbon Common Library

Shared utilities for Ban Carbon data science projects.

## Features

- **Path Management**: Utilities for finding monorepo root and managing data paths
- **Data I/O**: Validated data loading with pandera schemas
- **Visualization**: Reusable plotting functions for maps and charts
- **Logging**: Pre-configured loguru integration with tqdm

## Usage

### Path Management

```python
from ban_carbon_common.config import (
    MONOREPO_ROOT,
    SHARED_DATA_DIR,
    SHARED_RAW_DATA_DIR,
)

# Access shared data
data_file = SHARED_RAW_DATA_DIR / "my_dataset.csv"
```

### Data I/O

```python
from ban_carbon_common.io import load_world_boundaries

# Load world boundaries
world = load_world_boundaries(
    raw_dir=SHARED_RAW_DATA_DIR,
    processed_dir=SHARED_PROCESSED_DATA_DIR
)
```

### Visualization

```python
from ban_carbon_common.visualization import setup_map_figure

# Create a map figure
fig, ax = setup_map_figure(figsize=(12, 10))
```

## Development

```bash
cd libraries/ban_carbon_common
pytest tests/
```
