.DEFAULT_GOAL := help

.PHONY: help init init-dev test lint delint typecheck check pre-commit

# Select an isolated environment for the current platform.
ifeq ($(OS),Windows_NT)
PLATFORM_VENV := .venv-win
else
PLATFORM_VENV := .venv-lnx
endif

# Make UV create and use only the platform-specific environment.
init init-dev test lint delint typecheck check pre-commit: export UV_PROJECT_ENVIRONMENT := $(PLATFORM_VENV)

help:
	@echo "Available commands:"
	@echo "  make init       - Install runtime dependencies"
	@echo "  make init-dev   - Install development dependencies and hooks"
	@echo "  make test       - Run tests"
	@echo "  make lint       - Check linting, formatting, types, and structure"
	@echo "  make delint     - Fix lint and formatting issues"
	@echo "  make typecheck  - Run type checking"
	@echo "  make check      - Run lint and tests"
	@echo "  make pre-commit - Run pre-commit on all files"

init:
	uv sync --frozen --no-dev

init-dev:
	uv sync --frozen --extra dev
	uv run pre-commit install

test:
	uv run pytest

lint:
	uv run ruff check src tests
	uv run ruff format --check src tests
	uv run ty check src
	uv run python scripts/check_file_lengths.py
	uv run python scripts/check_python_blocks.py

delint:
	uv run ruff check --fix --unsafe-fixes src tests
	uv run ruff format src tests
	uv run python scripts/check_python_blocks.py --fix

typecheck:
	uv run ty check src

check: lint test

pre-commit:
	uv run pre-commit run --all-files
