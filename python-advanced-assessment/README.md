# Python Advanced Assessment (PY-ADV-01 → PY-ADV-05)

This repository is a ready-to-use VS Code workspace scaffold for a 5-day
Advanced Python assessment. Each day has its own folder with a starter
`src/`, `tests/`, and a `README.md` containing the task checklist,
objective, deliverables, and evaluation criteria for that day.

## Folder Overview

| Folder | Focus |
|---|---|
| `PY-ADV-01-Core-ProblemSolving` | Execution model, mutability, decorators, closures, generators, comprehensions, 8–10 problems |
| `PY-ADV-02-OOP-DesignPatterns-Exceptions` | OOP, dunder methods, custom exceptions, context managers, design patterns |
| `PY-ADV-03-DataProcessing-Files-JSON-API` | CSV/JSON, validation, datetime, logging, REST API client, unit tests |
| `PY-ADV-04-Performance-Threading-Async` | timeit, memory, multithreading, multiprocessing, asyncio, benchmarking |
| `PY-ADV-05-FinalAssessment` | Full mini production-style application (config, models, business logic, API, validation, exceptions, logging, tests, docs) |

## Getting Started in VS Code

1. Open this folder in VS Code: `File > Open Folder...`
2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # macOS/Linux
   source .venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Install the recommended VS Code extensions when prompted
   (Python, Pylance, Python Test Explorer).
5. Work through each `PY-ADV-0X-...` folder in order. Each folder's
   `README.md` has the full task list, objective, deliverables and
   evaluation weightage for that day.
6. Run tests from the integrated terminal:
   ```bash
   pytest PY-ADV-01-Core-ProblemSolving/tests
   ```
   or use the Testing panel in VS Code (already configured in
   `.vscode/settings.json`).

## Repository Structure

```
python-advanced-assessment/
├── .vscode/
│   ├── settings.json
│   ├── launch.json
│   └── extensions.json
├── requirements.txt
├── README.md
├── PY-ADV-01-Core-ProblemSolving/
│   ├── README.md
│   ├── src/
│   └── tests/
├── PY-ADV-02-OOP-DesignPatterns-Exceptions/
│   ├── README.md
│   ├── src/
│   └── tests/
├── PY-ADV-03-DataProcessing-Files-JSON-API/
│   ├── README.md
│   ├── src/
│   └── tests/
├── PY-ADV-04-Performance-Threading-Async/
│   ├── README.md
│   ├── src/
│   └── tests/
└── PY-ADV-05-FinalAssessment/
    ├── README.md
    ├── app/
    │   ├── config/
    │   ├── models/
    │   ├── business_logic/
    │   ├── utils/
    │   ├── api/
    │   ├── validation/
    │   ├── exceptions/
    │   └── logging_setup/
    └── tests/
```

## Notes

- Each `src/` starter file contains `# TODO` markers mapped to the task
  list in that day's README — fill them in as you complete each task.
- Each day's deliverables and evaluation criteria are documented in
  that day's `README.md`, copied from the original assessment brief.
- Use meaningful Git commits as you progress (required for PY-ADV-05).
