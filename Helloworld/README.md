# HelloWorld Example

This folder contains the HelloWorld example application built with PySide6.

Overview

- Entry point: `helloworld.py` — a `QMainWindow` that loads the UI and connects UI actions to backend functions.
- UI source: `form.ui` — Qt Designer XML file located in this folder.
- Generated UI (optional): `ui_form.py` — produced by `pyside6-uic`.
- Backend helpers: `modules/backend_functions.py` — dialog and helper functions used by the UI.

Requirements

- Python 3.8+
- See `requirements.txt` in this folder (`PySide6`).

Generate the UI Python module

If `ui_form.py` is not present or you want to regenerate it, run inside this folder:

```powershell
# using PySide6
pyside6-uic form.ui -o ui_form.py

# or using PySide2
pyside2-uic form.ui -o ui_form.py
```

Run the application

VS Code automation

This example is supported by the repository `.vscode/tasks.json` which defines tasks for:

- creating a virtual environment in `Helloworld/`,
- installing dependencies from `Helloworld/requirements.txt`,
- compiling `form.ui` into `ui_form.py`, and
- running `helloworld.py`.

From VS Code run `Tasks: Run Task` and choose the `Run all steps` task to execute the full sequence.

Notes

- `ui_form.py` is a generated file and can be regenerated locally. Decide whether to keep it committed or add it to `.gitignore`.
- Keep example-specific dependencies in the `Helloworld/requirements.txt` file.
