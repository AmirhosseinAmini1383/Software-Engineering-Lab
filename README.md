# MiniOrder — Software Engineering Lab

A small educational order-management API for a 10-session software engineering lab. It starts as a **single application (modular monolith)**. It is **not** a microservice system.

## Requirements
- Python 3.11 or newer
- Git
- An internet connection for the initial installation

## Start on Windows (PowerShell)
```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m uvicorn app.main:app --reload
```
Open http://127.0.0.1:8000/docs and try `GET /products`.
Stop the server with Ctrl+C.

If `py` does not work, use `python` instead (using the corresponding virtual environment created).

## Start on Linux/macOS
```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m uvicorn app.main:app --reload
```

## Run tests
Windows:
```powershell
.\.venv\Scripts\python.exe -m pytest -q
```
Linux/macOS:
```bash
.venv/bin/python -m pytest -q
```

## Example API
- `GET /` — API status
- `GET /products` — list products
- `GET /products/{product_id}` — one product
- `POST /orders` — create order, e.g. `{"product_id": 1, "quantity": 2}`
- `GET /orders` — list orders

Data is kept **in memory**. Restarting the server clears newly created orders. This is deliberate for the first sessions; it is not a production-ready store or a real inventory-reservation implementation.

## Class workflow
1. One member forks the teacher's repository to their GitHub account.
2. That member invites teammates as collaborators to **the same fork**.
3. Each teammate clones the team's repository. No one needs their own separate fork.
4. Exercises are announced outside this repository; the teacher does not need to update this starter after teams fork it.
5. Git commands are introduced as needed during class. Avoid committing `.venv`, secrets, or generated files.

## Project structure
- `app/` API, sample catalog, and order logic
- `tests/` automated tests for later sessions
- `docs/` architecture worksheet to fill in during DDD sessions
- `.gitignore` excludes local/generated files

## Later sessions
The teams will design bounded contexts, inspect/change simple rules, run tests, introduce GitHub Actions, and containerize the application. Sample CI and Docker solutions are intentionally **not included** in the student starter.
