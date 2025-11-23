# PySide Widgets Project Examples

A collection of small PySide/PyQt example applications. Each example should live in its own folder (for example `Helloworld/`, `Calculator/`, `FormExample/`, etc.) and follow the same structure: a `.ui` file (optional), an application entry point, optional generated UI Python module, and supporting modules.

## Requirements

- Python 3.8+ (use a virtual environment)
- The project `requirements.txt` lists `PySide6` (see `Helloworld/requirements.txt`).

## Setup (Windows / PowerShell)

This project includes VS Code task automation that performs the usual setup and run steps (create venv, install deps, compile the UI, run the app). See the **VS Code automation** section below for details. If you prefer not to use VS Code, the manual steps are still valid.

(See individual example folders for overview, UI generation, run instructions and VS Code tasks — for example `Helloworld/README.md`.)

## Project structure

```
./
	.gitignore            # repo-level ignores
	README.md
	LICENSE
	Helloworld/
		form.ui             # Qt Designer UI file
		helloworld.py       # app entry point
		ui_form.py          # generated (pyuic) — may be ignored
		requirements.txt    # runtime deps (PySide6)
		pyproject.toml      # small metadata used by pyside tooling
		modules/
			backend_functions.py
		.qtcreator/         # Qt Creator settings (usually ignored)
		venv/               # optional local virtualenv (ignored)
```



## Contributing

- Create issues or pull requests for fixes and improvements.
- Keep generated files out of commits by regenerating `ui_form.py` locally.

## License

See the `LICENSE` file in the repository root for license terms.

