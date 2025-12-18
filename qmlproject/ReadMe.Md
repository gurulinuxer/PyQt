# QML Widget Explorer (PySide6 + Qt Quick)

This project is a QML-based version of the original **Qt Widgets UI Explorer**, built with **PySide6 (Qt for Python)** and **Qt Quick Controls 2**. It is designed as an educational example to compare:

- `.ui` (widgets) vs `.qml` (Qt Quick) UIs  
- How to **reuse the same Python backend** (`modules/backend_functions.py`) from both projects  
- How to structure a small QML app with **StackView**, **tabs**, a **Python backend adapter**, and a simple worker start/stop flow  

The app shows a login page, then a tabbed “widget explorer” with **Buttons**, **Display**, **Input**, and a pseudo‑3D rotation demo, each logging interactions into a text browser-style area.

---

## Project structure
qmlproject/
├─ main.py # Starts QGuiApplication, loads QML, exposes backend
├─ modules/
│ ├─ backend_functions.py # Shared backend logic reused from the UI project
│ └─ qml_backend.py # QObject wrapper exposing backend to QML (slots/signals, thread worker)
└─ qml/
├─ main.qml # ApplicationWindow, menu bar, StackView navigation
└─ components/
├─ LoginPage.qml # Login screen (admin / 1234) with banner + GitHub link
├─ SecondPage.qml # Main tabbed page + Next button back to login
├─ ButtonsTab.qml # Button widgets (buttons, checkboxes, radios) + log area
├─ InputTab.qml # Input widgets (combos, sliders, dial, spinbox) + log area
├─ DisplayTab.qml # Display widgets (progress, value display, dial) + log area
├─ ThreeDTab.qml # Pseudo‑3D rotation demo (rotating square) + log area
└─ ThreadsTab.qml # QThread worker example with start/stop controls + log area

The **Python backend** is reused as-is from the widgets project, with `qml_backend.QmlBackend` acting as a thin adapter to expose:

- Login flow: `login(username, password)` / signals `loginSuccess`, `loginFailed`, `goToLogin`  
- Logging helpers: `logButtonClick`, `logCheckboxToggle`, `logRadioToggle`, `logComboSelection`, `logSpinBoxValue`, `logSliderValue`, `logDialValue`  
- Worker control: `start_worker()`, `stop_worker()` and related signals used by the QML UI to start/stop a background worker cleanly  

---

## Setup

Use the same virtual environment and dependencies as the UI project.

From the top-level workspace (where `Helloworld/` and `qmlproject/` live):

cd .\Helloworld
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt


To run the QML project:

cd ..\qmlproject
..\Helloworld\venv\Scripts\activate
python main.py


If you use VS Code, there is a `tasks.json` entry **“Run QML main.py”** which:

1. Creates/updates the venv in `Helloworld/`  
2. Installs dependencies from `requirements.txt`  
3. Activates that venv and runs `qmlproject/main.py`

---

## How the QML app works

### main.py / main.qml

- `main.py` creates a `QGuiApplication`, sets up a `QQmlApplicationEngine`, and exposes an instance of `QmlBackend` to QML as a context property named `backend`.  
- `qml/main.qml` defines an `ApplicationWindow` with a single `StackView`:
  - Initial page: `"components/LoginPage.qml"`.  
  - A `Connections` block listens to `backend.loginSuccess` / `backend.goToLogin` and pushes or resets to `SecondPage.qml` / `LoginPage.qml`.

### Login flow

`LoginPage.qml`:

- Simple `Page` with `TextField` for username and password and a **Login** button.  
- On click, calls `backend.login(user.text, pwd.text)`.  
- On `loginSuccess`, `main.qml` pushes `"components/SecondPage.qml"` onto the `StackView`.  
- On `loginFailed`, the page shows an error label.

Credentials are the same as the UI project: **admin / 1234**, implemented in `BackendFunctions.validate_login`.

### Second page and tabs

`SecondPage.qml`:

- `TabBar` + `StackLayout` hosting multiple tabs:
  - **Buttons** → `ButtonsTab.qml`  
  - **Display** → `DisplayTab.qml`  
  - **Input** → `InputTab.qml`  
  - **3D** (pseudo‑3D) → `ThreeDTab.qml`  
- A **Next** button in the top-right calls `backend.back_to_login()`, which triggers `backend.goToLogin` and returns to the login page via `main.qml`.

---

## Tabs overview

All tabs follow the same teaching pattern:

- Top area: widgets or a demo to experiment with.  
- Bottom area: a scrollable `TextArea` acting like a **TextBrowser**.  
- Every interaction calls a backend logging helper so the user sees readable log lines (e.g., “Button 'X' clicked”, “CheckBox 'Option 1' checked”, “Worker started”). The log keeps the cursor at the end so the latest entry is always visible.

### ButtonsTab.qml

Shows typical “button-like” controls:

- `Button` (push button)  
- `ToolButton`  
- Multiple `CheckBox` options  
- Multiple `RadioButton` choices  

Each control’s signals call:

- `backend.logButtonClick(name)` for button presses.  
- `backend.logCheckboxToggle(name, checked)` / `backend.logRadioToggle(name, checked)` for state changes.

Log lines are appended to the bottom text area; the cursor is moved to the end so the latest activity stays visible.

### DisplayTab.qml

Demonstrates display-oriented widgets:

- `ProgressBar` driven by `Slider` and `SpinBox`.  
- `Label` that reflects the current numeric value.  
- A `Dial` as a gauge-style control.  

All changes log using:

- `logSpinBoxValue`, `logSliderValue`, `logDialValue`.

A **“Log current state snapshot”** button writes a compact summary of all current values into the log area.

### InputTab.qml

Combines input widgets:

- Two `ComboBox`es (options, “fonts” list).  
- `Dial`, vertical and horizontal `Slider`s.  
- `SpinBox` and a separate “progress” `Slider`.  

Each control logs its changes via `logComboSelection`, `logDialValue`, `logSliderValue`, `logSpinBoxValue`. A **“Log input snapshot”** button appends a full snapshot of all current values to the log area.

### ThreeDTab.qml (pseudo‑3D rotation demo)

Provides a minimal, “3D-like” example without requiring full Qt Quick 3D:

- A centered square “cube” that rotates based on mouse drag in the top area.  
- The current angle is clamped between 0° and 360° and displayed as text on the square.  
- Every change in angle is logged into the bottom `TextArea` with a readable message (for example, “Rotation: 123.4°”), with the log auto-scrolling to show the latest entry.

This tab is intentionally simple and focuses on the idea of rotation, angle wrapping, and logging, so it can run in environments where true Qt Quick 3D is not available.

---

## Worker start/stop behaviour

The QML project also demonstrates integrating a simple worker lifecycle with the shared backend:

- A pair of **Start Worker** / **Stop Worker** controls (for example, in one of the tabs) call `backend.start_worker()` and `backend.stop_worker()` on the Python side.  
- The backend manages the worker state to avoid duplicate starts or invalid stops; repeated start/stop cycles run without warnings or errors on the console.  
- Each worker event (started, already running, stopped, already stopped) is logged into the same bottom `TextArea` so users can see exactly what happened.

This mirrors the widgets project’s behaviour while using QML and signals/slots, and shows how to keep the worker logic entirely in Python while driving it from declarative QML.

---

## Learning goals

This QML project is intended to sit side-by-side with the original widgets/UI project so learners can:

- Compare **Qt Widgets (`.ui` + `helloworld.py`)** vs **Qt Quick (`.qml` + `main.py`)** using the same backend.  
- See how **StackView** and `TabBar + StackLayout` organize multi-page QML UIs.  
- Understand how to:
  - Expose a Python backend (`BackendFunctions`) into QML with a small `QObject` adapter (`QmlBackend`) and slots/signals.  
  - Log interactions (including worker lifecycle events) centrally while keeping QML declarative and clean.  
  - Share business logic and worker code between UI technologies with minimal duplication.  
  - Add extra “demo” tabs (like the pseudo‑3D rotation example) without changing the underlying backend structure.

This structure can be extended with more examples (charts, list models, real Qt Quick 3D scenes, etc.) while preserving the same Python backend and educational layout.
