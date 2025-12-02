# Ban Carbon Data Science Monorepo

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

A monorepo for Ban Carbon data science projects, following Cookiecutter Data Science v2 best practices.

## Structure

- **`libraries/`**: Shared code libraries used across projects
  - `ban_carbon_common`: Common utilities for paths, I/O, and visualization

- **`projects/`**: Individual data science projects
  - `power-plant-emissions`: Analysis of RGGI power plant emissions

- **`data/`**: Shared datasets used across multiple projects

## Quick Start

### Setup

```bash
# Create virtual environment
make create_environment
source .venv/bin/activate  # Unix/macOS

# Install dependencies
make requirements
```

### Working with Projects

```bash
# Navigate to a project
cd projects/power-plant-emissions
make help

# Or use shortcuts from root
make ppe-data      # Process power-plant-emissions data
make ppe-viz-map   # Generate visualization
```

## Available Commands

```bash
make help             # Show all commands
make requirements     # Install dependencies
make lint             # Check code style
make format           # Format code
make test-all         # Run all tests
make clean            # Remove artifacts
```

## Adding a New Project

1. Create project directory: `mkdir -p projects/my-new-project/src/my_new_project`
2. Copy structure from `projects/power-plant-emissions`
3. Run `uv sync` to register the project

## License

MIT License - see LICENSE file
