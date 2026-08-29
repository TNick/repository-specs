.PHONY: help validate test

help:
	@echo "validate  Validate specification metadata and documents"
	@echo "test      Run catalog validation"

validate:
	python _scripts/validate_catalog.py

test: validate
