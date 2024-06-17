# Makefile for managing a Flask application

# Variables
APP_NAME = flask_app
FLASK_APP = app/app.py
FLASK_PORT=8000
VENV_DIR = eenv
PYTHON = $(VENV_DIR)/bin/python
PIP = $(VENV_DIR)/bin/pip

# Default target
.PHONY: all
all: run

# Create a virtual environment
.PHONY: venv
venv:
	python3 -m venv $(VENV_DIR)

# Install dependencies
.PHONY: install
install: venv
	$(PIP) install -r requirements.txt

# Run the Flask application
.PHONY: run
run: venv
	FLASK_APP=$(FLASK_APP) FLASK_RUN_PORT=$(FLASK_PORT) $(PYTHON) -m flask run

# Clean the environment
.PHONY: clean
clean:
	rm -rf $(VENV_DIR)

# Update dependencies
.PHONY: update
update:
	$(PIP) install --upgrade -r requirements.txt

# Display help
.PHONY: help
help:
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@echo "  all      - Run the Flask application (default)"
	@echo "  venv     - Create a virtual environment"
	@echo "  install  - Install dependencies"
	@echo "  run      - Run the Flask application"
	@echo "  clean    - Clean the environment"
	@echo "  update   - Update dependencies"
	@echo "  help     - Display this help message"
