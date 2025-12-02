# Power Plant Emissions Analysis

Analysis of RGGI (Regional Greenhouse Gas Initiative) power plant emissions data.

## Overview

This project analyzes CO2 emissions from power plants in the RGGI region (Northeastern US states), including data processing, geospatial visualization, and exploratory analysis.

## Data Sources

- **RGGI Emissions Data**: Annual/quarterly facility-level emissions
- **Power Plant Geolocation**: Spatial data for US power plants
- **US State Boundaries**: Census Bureau state boundaries

## Getting Started

```bash
# Process raw data
make data

# Generate visualizations
make viz-map

# Explore in notebooks
jupyter lab notebooks/
```

## Available Commands

```bash
make help      # Show commands
make data      # Process raw data
make viz-map   # Generate emission map
make test      # Run tests
```

## Project Structure

```
power-plant-emissions/
├── data/           # Project-specific data
├── notebooks/      # Jupyter notebooks
├── src/            # Source code
├── models/         # Trained models
└── reports/        # Generated outputs
```
