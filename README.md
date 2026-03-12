# Simple SQL Employee Management System with GUI

## Demo for Company/Portfolio
**What it does:** GUI to manage employees DB (View/Add/Edit/Delete) + run custom SQL queries. Uses SQLite + Tkinter (no installs).

## Quick Start
1. Open terminal in project dir.
2. Run:
```
python main.py
```
3. GUI opens:
   - List shows sample employees.
   - Add/Edit/Delete via form.
   - Query tab: Try `SELECT * FROM employees WHERE salary > 50000`.
4. Data saves to `company.db`.

## Features
- CRUD on Employees (id, name, position, salary).
- Custom SQL executor.
- Error handling.

**Pro Tip:** Customize queries to show SQL skills!

## Tech
- Python stdlib: sqlite3, tkinter.
- Works on Windows/Mac/Linux.
