VENV_ACTIVATE ?= . venv/bin/activate

all: start

.PHONY: start
start: venv install

.PHONY: venv
venv:
	$(info * Setting up Python Virtual Environment...)
	python3 -m venv venv
	$(VENV_ACTIVATE) && pip install -U pip
	$(VENV_ACTIVATE) && pip install wheel
	$(VENV_ACTIVATE) && pip install poetry==1.1.8

.PHONY: install
install:
	$(info * Installing Dependencies...)
	$(VENV_ACTIVATE) && poetry install

.PHONY: run
run:
	$(info * Run API...)
	$(VENV_ACTIVATE) && python example/main.py

.PHONY: test
test:
	$(info * Testing...)
	$(VENV_ACTIVATE) && pytest

.PHONY: fuzz
fuzz:
	$(info * Fuzzing...)
	$(VENV_ACTIVATE) && schemathesis run --checks all --app=example.main:api /openapi.json
