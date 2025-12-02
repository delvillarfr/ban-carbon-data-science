#################################################################################
# GLOBALS                                                                       #
#################################################################################

PROJECT_NAME = power-plant-emissions
PYTHON_INTERPRETER = python

#################################################################################
# COMMANDS                                                                      #
#################################################################################

## Process raw data into cleaned datasets
.PHONY: data
data:
	$(PYTHON_INTERPRETER) -m power_plant_emissions.dataset

## Generate power plant emission map visualization
.PHONY: viz-map
viz-map:
	$(PYTHON_INTERPRETER) -m power_plant_emissions.plots

## Run project tests
.PHONY: test
test:
	$(PYTHON_INTERPRETER) -m pytest tests

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
