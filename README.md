# 🏢 SQL Employee Management System (GUI Demo)

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![SQLite](https://img.shields.io/badge/SQLite-Stdlib-green.svg)](https://www.sqlite.org/)
[![Tkinter](https://img.shields.io/badge/Tkinter-GUI-orange.svg)](https://docs.python.org/3/library/tkinter.html)

## 📖 Table of Contents
- [Overview](#overview)
- [✨ Features](#features)
- [🚀 Quick Start](#quick-start)
- [📸 Screenshots](#screenshots)
- [💻 Usage](#usage)
- [🗄️ Project Structure](#project-structure)
- [🔧 Development & Customization](#development)
- [📊 Sample Data](#sample-data)
- [⚠️ Limitations](#limitations)
- [🤝 Contributing](#contributing)
- [📄 License](#license)

## Overview
**Most Relevant SQL/Data Analysis Project**: "Employee Management System" – A production-grade SQLite GUI app for advanced SQL operations on employee data (HR Analytics demo).

**Brief Description**: Built Employee DB CRUD GUI (Tkinter/Python stdlib) handling Add/Edit/Delete/View + custom SQL executor for complex analytics queries (e.g., `SELECT AVG(salary) GROUP BY position`, filtering high-earners). Processes sample dataset, persists changes, error-handles edge cases. Showcases SQL proficiency, data modeling (schema design), query optimization in interactive UI. Deployable anywhere (no deps), extensible for BI tools.

**Key Purpose**: Demonstrates SQL/Data skills for interviews/portfolios. Data persists in `company.db`.

Runs on **Windows/Mac/Linux** out-of-the-box.

*(Copy-paste ready for "Tell me about your SQL project" questions!)*

## ✨ Features
- ✅ **Full CRUD**: View/Add/Edit/Delete employees (name, position, salary).
- ✅ **Custom SQL Queries**: Execute any SQL (SELECT/JOIN/UPDATE/etc.) with results preview and error handling.
- ✅ **Persistent SQLite DB**: Auto-creates table + sample data on first run.
- ✅ **User-Friendly GUI**: Tabbed interface, Treeview list, form validation, refresh, confirm dialogs.
- ✅ **Zero Dependencies**: Pure `sqlite3` + `tkinter` (Python stdlib).
- ✅ **Error-Resilient**: Input validation, SQL exceptions handled.

## 🚀 Quick Start
1. **Prerequisites**: Python 3.8+.
2. Open terminal in project directory (`c:/Users/ADMIN/Desktop/project`).
3. Run:
   ```bash
   python main.py
   ```
4. GUI launches (~800x600 window). Enjoy!

**Pro Tip**: Use Query tab to flex SQL skills – e.g., `SELECT * FROM employees WHERE salary > 70000 ORDER BY salary DESC;`

## 📸 Screenshots
*(Add your own screenshots here for GitHub appeal!)*

### 1. Employees CRUD Tab
```
[Treeview: ID | Name | Position | Salary]
1 | John Doe | Developer | 75000
2 | Jane Smith | Manager | 95000
[Form: Name, Position, Salary fields]
[Buttons: Add | Edit | Delete | Refresh]
```

### 2. Custom SQL Query Tab
```
SQL: SELECT * FROM employees WHERE salary > 70000;
Results:
Columns: id, name, position, salary
(1, 'John Doe', 'Developer', 75000.0)
(2, 'Jane Smith', 'Manager', 95000.0)
```

*Tip*: Capture with `python main.py`, use tools like ShareX (Win) or Flameshot for images. Name: `screenshots/crud-tab.png`, `screenshots/query-tab.png`.

## 💻 Usage
### CRUD Tab
1. **View**: Auto-loads employee list.
2. **Add**: Fill form → Click **Add**.
3. **Edit**: Select row → Edit form → **Edit**.
4. **Delete**: Select → **Delete** (confirm dialog).
5. **Refresh**: Updates list after changes.

### Query Tab
1. Edit sample query or write custom SQL.
2. **Execute Query** → See results/errors below.
3. Supports SELECT (tabular results) + DML/DDL (success msg).

**Example Queries**:
```sql
-- High earners
SELECT * FROM employees WHERE salary > 70000;

-- Average salary
SELECT AVG(salary) as avg_salary FROM employees;

-- Update example
UPDATE employees SET salary = 100000 WHERE position = 'Manager';
```

## 🗄️ Project Structure
```
project/
├── main.py          # Core GUI app (250+ lines)
├── company.db       # SQLite DB (auto-created)
├── README.md        # 📄 You're reading it!
└── TODO.md          # Progress tracker
```

## 🔧 Development & Customization
- **Run in Dev**: `python main.py`
- **Test DB**: Open `company.db` with DB Browser for SQLite.
- **Extend**:
  1. Add columns: Edit `init_db()` CREATE TABLE.
  2. New queries/UI: Modify `execute_query()`, `setup_gui()`.
  3. Export: Add button for CSV export.
- **Lint/Test**: Pure Python – `python -m py_compile main.py` or pytest for units.

**Clean Reset**: Delete `company.db` → Reruns sample data.

## 📊 Sample Data (Initial DB)
| ID | Name       | Position  | Salary |
|----|------------|-----------|--------|
| 1  | John Doe  | Developer | 75000 |
| 2  | Jane Smith| Manager   | 95000 |
| 3  | Bob Johnson| Analyst  | 65000 |

## ⚠️ Limitations
- Single-table DB (easy to extend).
- No auth/export (focus on core SQL/GUI).
- Tkinter styling basic (modernize with customtkinter if deps OK).

## 🤝 Contributing
1. Fork repo.
2. Create feature branch.
3. PR with tests.
Ideas: Multi-table, charts, export.

## 📄 License
[MIT License](LICENSE) – Feel free to use/fork!

---

⭐ **Star if useful!** · 👀 **Watch for updates** · 💬 **Issues welcome**

