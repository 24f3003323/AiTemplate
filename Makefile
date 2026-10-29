PYTHON = python
VENV_PYTHON = .venv/Scripts/python.exe
RUFF = .venv/Scripts/ruff.exe


.PHONY: setup lint test check clean

setup:
	$(PYTHON) -m venv .venv
	$(VENV_PYTHON) -m pip install --upgrade pip
	$(VENV_PYTHON) -m pip install -e ".[dev]"
	$(VENV_PYTHON) -m pip install -r requirements.txt

lint:
	$(RUFF) check .

test:
	python -m app.main

check: lint test

clean:
	python -c "import shutil; shutil.rmtree('.venv', ignore_errors=True)"