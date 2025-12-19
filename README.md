# PyQt / PySide6 Educational Demo

This repository contains two parallel example projects:

- A **Qt Widgets** UI built with `.ui` files and PyQt/PySide6.
- A **Qt Quick (QML)** UI using the same backend logic, to compare approaches.

Both are intentionally small and focused so beginners can see how widgets and QML map to each other.

## Requirements
- Windows 11 
- VS code 
- Python 3.8+ (use a virtual environment)

## Projects

### 1. UI project (Qt Widgets)

**Folder:** `uiproject/`

Classic widgets-based app using `.ui` and Python.

Key features:

- Login page (with banner, title, and GitHub link).
- Tabbed widget demo showing Buttons, Display, and Input widgets.
- TextBrowser areas that log widget interactions (button clicks, value changes, etc.).
- Shared backend logic in pure Python (`backend_functions.py`).

Project layout:
```
uiproject/
├─ helloworld.py # Main widgets application
├─ form.ui # Qt Designer UI file
├─ ui_form.py # Generated Python UI (from form.ui)
├─ requirements.txt # Dependencies for the widgets project
├─ venv/ # Virtual environment for uiproject (created by tasks)
└─ modules/
└─ backend_functions.py # Shared backend logic (dialogs, logging helpers, login check)
```  

### 2. QML project (Qt Quick / PySide6)

**Folder:** `qmlproject/`

Qt Quick version of the same ideas, built around QML, `StackView`, and `TabBar`, reusing the **same** backend functions from `uiproject`.

#### Layout
```
qmlproject/
├─ main.py # Starts QGuiApplication, loads QML, exposes backend
├─ requirements.txt # Dependencies for the QML project
├─ venv/ # Virtual environment for qmlproject (created by tasks)
├─ modules/
│ ├─ backend_functions.py # Shared backend logic copied/reused from uiproject
│ └─ qml_backend.py # QObject wrapper exposing backend to QML (slots/signals, thread worker)
└─ qml/
├─ main.qml # ApplicationWindow, menu bar, StackView navigation
└─ components/
├─ LoginPage.qml # Login screen (admin / 1234) with banner + GitHub link
├─ SecondPage.qml # Main tabbed page + Next button back to login
├─ ButtonsTab.qml # Button widgets (buttons, checkboxes, radios) + log area
├─ InputTab.qml # Input widgets (combos, sliders, dial, spinbox) + log area
├─ DisplayTab.qml # Display widgets (progress, spinbox, dial) + log area
├─ ThreeDTab.qml # Pseudo‑3D rotating square demo + log area
└─ ThreadsTab.qml # QThread worker example with start/stop + log area
```
#### Navigation flow

- `main.qml` shows an `ApplicationWindow` with:
  - **Menu** → “Widgets Explorer”.
  - **Help** → “About” dialog (project name, version, and demo login info).
  - A central `StackView`:
    - `initialItem: "components/LoginPage.qml"`.
- `LoginPage.qml`:
  - Banner-style header with title, author handle, and GitHub URL.
  - Username/password fields and **Login** button.
  - Demo credentials hint: `Username: admin`, `Password: 1234`.
  - Calls `backend.login(user, password)` and listens for `loginFailed` to show an error label.
- On `backend.loginSuccess` (wired in `main.qml`), the `StackView` pushes `SecondPage.qml`.
- `SecondPage.qml`:
  - Top-right **Next** button that calls `backend.back_to_login()` and returns to `LoginPage.qml`.
  - `TabBar + StackLayout` with the following tabs:
    - **Buttons**
    - **Input**
    - **Display**
    - **3D**
    - **Threads**

#### Tabs overview

All tabs follow the same pattern:

- Top: widgets to experiment with.
- Bottom: scrollable `TextArea` used like a TextBrowser.
- Each interaction calls Python logging helpers (`backend_functions.py`) or dedicated slots and appends a formatted text line.

**ButtonsTab.qml**

- Demonstrates:
  - `Button`, `ToolButton`.
  - Multiple `CheckBox` and `RadioButton` options.
- Logs:
  - Button clicks via `backend.logButtonClick(name)`.
  - Checkbox and radio state changes via `backend.logCheckboxToggle` and `backend.logRadioToggle`.

**InputTab.qml**

- Demonstrates:
  - Two `ComboBox`es (plain options + “font” list).
  - `Dial`, vertical and horizontal `Slider`s.
  - `SpinBox` and a “progress” `Slider`.
- Logs:
  - Combo changes: `logComboSelection`.
  - Dial, sliders: `logDialValue`, `logSliderValue`.
  - SpinBox: `logSpinBoxValue`.
- “Log input snapshot” button appends all current values in one shot.

**DisplayTab.qml**

- Demonstrates:
  - `SpinBox` + `Slider` tied together.
  - `ProgressBar` and label showing current value.
  - A display `Dial`.
- Logs value changes through the same backend helpers.
- Includes a “snapshot” button for logging the current display state.

**ThreeDTab.qml** (pseudo‑3D)

- Simulates a 3D cube using a rotating `Rectangle` + `Rotation` transform (no QtQuick3D needed).
- User can drag horizontally to rotate the square from 0–360 degrees.
- Shows the current angle centered on the square.
- Logs each angle change into the text browser in the format:  
  `[..time..] Pseudo-3D cube angle: XXX.X°`.

**ThreadsTab.qml**

- Demonstrates running background work from QML safely via Python:

  - **Start worker** → calls `backend.start_thread_example()`.
  - **Stop worker** → calls `backend.stop_thread_example()`.

- `QmlBackend` sets up:

  - A `ThreadWorker` subclass of `QObject` with:
    - `progress(str)` and `finished()` signals.
    - `run()` method executed in a `QThread` (simple loop with `time.sleep`).
  - A dedicated `QThread` for the worker.
  - A `threadLog(str)` signal exposed to QML.

- `ThreadsTab.qml` connects to `onThreadLog(message)` and appends each message to its TextArea, so you can see ticks coming from a worker thread without blocking the UI.

---

## Virtual environments and tasks

Each project has its **own** virtual environment and `requirements.txt` to avoid dependency conflicts.

- `uiproject/venv` – widgets UI dependencies.
- `qmlproject/venv` – QML UI dependencies.

Typical `requirements.txt` entries:

PySide6>=6.5,<7.0

VS Code’s `.vscode/tasks.json` defines tasks to:

- Create venv + install `requirements.txt` for each project.
- Run the widgets app (`helloworld.py`) or QML app (`main.py`) using the correct venv.

Example tasks (simplified):

- **Create UI virtual environment**
- **Install UI dependencies from requirements.txt**
- **Run HelloWorld.py**
- **Create QML virtual environment**
- **Install QML dependencies from requirements.txt**
- **Run QML main.py**

---

## Goals

This repository is meant as an educational playground to:

- Compare **Qt Widgets** and **Qt Quick (QML)** using the same Python backend.
- Show best practices for:
  - Separating UI and backend logic.
  - Logging widget interactions.
  - Navigating with `StackView` and `TabBar`.
  - Running background work with `QThread` and signaling results back to QML.
- Provide small, focused examples that beginners can extend for their own experiments.


## Contributing

- Create issues or pull requests for fixes and improvements.
- Keep generated files out of commits by regenerating `ui_form.py` locally.

## License

See the `LICENSE` file in the repository root for license terms.

