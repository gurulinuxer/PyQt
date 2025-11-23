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

Run the application

VS Code automation

This example is supported by the repository `.vscode/tasks.json` which defines tasks for:

- creating a virtual environment in `Helloworld/`,
- installing dependencies from `Helloworld/requirements.txt`,
- compiling `form.ui` into `ui_form.py`, and
- running `helloworld.py`.

From VS Code run `Tasks: Run Task` and choose the `Run all steps` task to execute the full sequence.

Manual steps (PowerShell)

If you prefer to run the same steps that the VS Code tasks perform manually, run these commands from the repository root (PowerShell):

```powershell
# 1) create virtual environment inside the example folder
python -m venv Helloworld\venv

# 2) activate the venv
.\Helloworld\venv\Scripts\Activate.ps1

# 3) install dependencies
pip install -r Helloworld\requirements.txt

# 4) compile the Qt Designer UI to a Python module (if needed)
cd Helloworld
pyside6-uic form.ui -o ui_form.py
cd ..

# 5) run the application
python Helloworld\helloworld.py
```

Notes:
- Replace `pyside6-uic` with `pyside2-uic` if you are using PySide2.
- `ui_form.py` is a generated file and can be regenerated locally. Decide whether to keep it committed or add it to `.gitignore`.
- Keep example-specific dependencies in the `Helloworld/requirements.txt` file.
- These commands match the sequence executed by `.vscode/tasks.json` and are useful when not using VS Code or when scripting CI steps.


