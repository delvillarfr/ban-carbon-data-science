#################################################################################
# GLOBALS                                                                       #
#################################################################################

MONOREPO_NAME = ban-carbon-data-science
PYTHON_VERSION = 3.12
PYTHON_INTERPRETER = python

#################################################################################
# WORKSPACE COMMANDS                                                            #
#################################################################################

## Set up workspace environment
.PHONY: create_environment
create_environment:
	uv venv --python $(PYTHON_VERSION)
	@echo ">>> New uv virtual environment created. Activate with:"
	@echo ">>> Windows: .\\.venv\\Scripts\\activate"
	@echo ">>> Unix/macOS: source ./.venv/bin/activate"

## Install all workspace dependencies
.PHONY: requirements
requirements:
	uv sync --all-packages

## Lint all code in workspace
.PHONY: lint
lint:
	ruff format --check
	ruff check

## Format all code in workspace
.PHONY: format
format:
	ruff check --fix
	ruff format

## Clean all compiled Python files
.PHONY: clean
clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name ".ruff_cache" -exec rm -rf {} +

#################################################################################
# PROJECT SHORTCUTS                                                             #
#################################################################################

## Run power-plant-emissions project targets
.PHONY: ppe-%
ppe-%:
	$(MAKE) -C projects/power-plant-emissions $*

#################################################################################
# SELF DOCUMENTING COMMANDS                                                     #
#################################################################################

.DEFAULT_GOAL := help

define PRINT_HELP_PYSCRIPT
import re, sys; \
lines = '\n'.join([line for line in sys.stdin]); \
matches = re.findall(r'\n## (.*)\n[\s\S]+?\n([a-zA-Z_-]+):', lines); \
print('Available rules:\n'); \
print('\n'.join(['{:25}{}'.format(*reversed(match)) for match in matches]))
endef
export PRINT_HELP_PYSCRIPT

help:
	@$(PYTHON_INTERPRETER) -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)
