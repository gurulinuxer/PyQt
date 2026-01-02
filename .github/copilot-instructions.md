# Copilot instructions for the PyQt / PySide6 demo repo

Purpose: give AI coding agents the minimal, actionable knowledge to be productive here.

High-level architecture
- Two parallel example apps show the same backend patterns: `uiproject/` (Qt Widgets) and `qmlproject/` (Qt Quick / QML).
- Shared idea: small, stateless backend helpers live in `*/modules/backend_functions.py` and provide timestamped log messages and simple dialogs. UI layers call those helpers rather than containing business logic.
- QML integration: `qmlproject/main.py` instantiates `QmlBackend` and registers it with the QML context via `engine.rootContext().setContextProperty("backend", backend)`. See `qmlproject/modules/qml_backend.py` for the QObject wrapper exposing slots/signals used by QML.

Key files to read first
- `uiproject/helloworld.py` — widgets entrypoint.
- `uiproject/modules/backend_functions.py` and `qmlproject/modules/backend_functions.py` — central helper methods and logging format.
- `qmlproject/main.py` and `qmlproject/modules/qml_backend.py` — QML <-> Python glue and thread worker pattern.
- `qmlproject/qml/components/*` — QML pages and tabs demonstrating how UI calls backend slots (e.g., `backend.logButtonClick(name)`).

Important patterns and conventions (repo-specific)
- Two separate venvs: each project keeps its own `venv/` and `requirements.txt`; tasks in `.vscode/tasks.json` create and use those venvs. Do not assume a single global venv.
- Generated UI file: `ui_form.py` is produced from `form.ui` by `pyside6-uic`; the repo documents regenerating it locally. Prefer editing `form.ui` in Qt Designer and regenerating rather than editing `ui_form.py` by hand.
- Stateless backend helpers: `BackendFunctions` methods are intentionally small and synchronous. Tests or refactors should preserve this surface (methods return formatted strings; UI appends them to logs).
- QML callable methods: `QmlBackend` exposes `@Slot` methods that return strings used directly by QML TextArea append operations. When changing signatures, update both QML calls and the Python slot decorator.
- Threading pattern: see `ThreadWorker` in `qmlproject/modules/qml_backend.py` — worker is a `QObject` moved to a `QThread`; it emits `progress` signals connected to `threadLog` (a QmlBackend Signal) and is stopped by calling a `stop()` slot. Keep explicit cleanup: `thread.quit()` + `thread.wait()`.

Run / developer workflows (concrete commands)
- Use the provided VS Code tasks or run manually from each project folder.
- Example (Linux / POSIX commands):
  - Create a venv and install (qmlproject):

    python -m venv qmlproject/venv
    source qmlproject/venv/bin/activate
    pip install -r qmlproject/requirements.txt

  - Run QML app:

    source qmlproject/venv/bin/activate
    python qmlproject/main.py

  - Widgets app (uiproject):

    python -m venv uiproject/venv
    source uiproject/venv/bin/activate
    pip install -r uiproject/requirements.txt
    # compile UI if needed
    pyside6-uic uiproject/form.ui -o uiproject/ui_form.py
    python uiproject/helloworld.py

Notes: the repository README and `uiproject/README.md` document PowerShell examples and VS Code tasks; on Linux use the `source venv/bin/activate` activation path.

What to change when adding features
- To expose new QML functions: add a `@Slot` method to `QmlBackend`, return simple types (str, int, bool) or use Signals for async messages. Register the instance in `main.py` as `backend`.
- To add new UI controls in QML: add a method in `BackendFunctions` for consistent logging and call it via `backend.<method>` from QML.
- For background work: follow the existing `ThreadWorker` pattern (QObject worker, moved to QThread, emit progress signals). Avoid running long synchronous work in the main thread.

Repository-specific gotchas
- Demo credentials are hardcoded: Username `admin`, Password `1234` (see `validate_login`). Tests or changes that rely on authentication should update this function.
- `ui_form.py` is generated — decide if you want it tracked. Regenerate locally when `form.ui` changes.
- QML signal/slot names are referenced in QML; renaming signals in Python requires updating QML handlers (search for `onThreadLog`, `loginFailed`, `loginSuccess`).

If you're an AI assistant editing code
- Prioritize: (1) small, non-breaking changes to `BackendFunctions`, (2) add new `@Slot` methods in `QmlBackend` and corresponding QML calls, (3) avoid changing threading logic unless accompanied by tests or manual run verification.
- When modifying signature types used by QML, include both the Python `@Slot(...)` decorator signature and a sample QML call in your PR description.

Where to ask humans for clarification
- If a change affects venv/CI expectations or requires switching PySide6/PySide2, ask before changing `requirements.txt` or build tasks.

Files referenced
- uiproject/helloworld.py
- uiproject/modules/backend_functions.py
- uiproject/form.ui
- qmlproject/main.py
- qmlproject/modules/qml_backend.py
- qmlproject/modules/backend_functions.py
- qmlproject/qml/components/*

End of instructions — ask for feedback if any section is unclear or if you'd like more examples inserted.
