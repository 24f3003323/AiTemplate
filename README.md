# Python Developer Template

A small starting point for Python projects. It includes a `src`-based app
package, environment-based settings, pinned dependencies, Ruff linting, and a
Makefile for common development tasks.

## Requirements

- Python 3.12 or newer (Ruff is configured for Python 3.12)
- GNU Make
- Git

On Windows, install GNU Make and ensure `make` is available on `PATH`. The
Makefile uses `.venv\Scripts\python.exe`, the standard virtual-environment
Python path on Windows.

## Get started

Clone the template and enter the project directory:

```powershell
git clone https://github.com/24f3003323/AiTemplate my-project
cd my-project
```

Create your local environment file from the example:

```powershell
Copy-Item .env.example .env
```

Edit `.env` and set values for the settings your app reads:

```dotenv
LLM_API_KEY=your-key
LLM_MODEL=your-model
DEBUG=false
```

Do not commit `.env` or put real credentials in source control. The current
example app prints its configured API key when it runs, so use a placeholder
key until that behavior is changed; never run it with a real secret in an
environment where console output may be shared or recorded.

Install the project and its dependencies:

```powershell
make setup
```

The `setup` target creates `.venv`, upgrades pip, installs the project in
editable mode, and installs the packages listed in `requirements.txt`. The
editable install currently requests a `dev` extra (`.[dev]`), which is not
declared in `pyproject.toml`; pip may print a warning about the missing extra.
The Makefile continues to install `requirements.txt`.


## Makefile commands

Run these commands from the project root:

| Command | What it does |
| --- | --- |
| `make setup` | Creates `.venv`, upgrades pip, installs the project in editable mode, and installs `requirements.txt`. |
| `make lint` | Runs `ruff check .` using the Ruff executable in `.venv`. |
| `make test` | Runs the app with `python -m app.main`. This is currently an app smoke run, not a unit-test suite. |
| `make check` | Runs `make lint` followed by `make test`. |
| `make clean` | Removes the `.venv` virtual environment. Run `make setup` again to recreate it. |

For example, after setup and activation:

```powershell
make lint
make test
```

The app loads `.env` settings through `src/app/config.py`. Its current entry
point is `src/app/main.py`; use these as starting points when adapting the
template for your project. Add project dependencies to `requirements.txt` and
update the app and configuration to match your needs.
