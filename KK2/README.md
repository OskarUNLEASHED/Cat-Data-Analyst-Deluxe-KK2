# KK2 - Oraklet

FastAPI assignment scaffold for KK2.

## Planned App Structure

```text
app/
├── __init__.py
├── main.py
├── config.py
├── schemas.py
├── data.py
├── chain/
│   ├── __init__.py
│   ├── runnable.py
│   ├── steps.py
│   └── pipeline.py
└── tests/
    ├── __init__.py
    ├── test_endpoints.py
    └── test_chain.py
```

## Setup

```bash
uv sync
```

## Run

Implementation pending.

Expected command later:

```bash
uv run uvicorn app.main:app --reload
```

## Test

Implementation pending.

Expected command later:

```bash
uv run pytest app/tests/ -v
```
