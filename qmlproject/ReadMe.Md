# QML Widget Explorer (PySide6 + Qt Quick)

This project is a QML-based version of the original **Qt Widgets UI Explorer**, built with **PySide6 (Qt for Python)** and **Qt Quick Controls 2**. It is designed as an educational example to compare:

- `.ui` (widgets) vs `.qml` (Qt Quick) UIs  
- How to **reuse the same Python backend** (`modules/backend_functions.py`) from both projects  
- How to structure a small QML app with **StackView**, **tabs**, and a **Python backend adapter**

The app shows a login page, then a tabbed “widget explorer” with **Buttons**, **Display**, and **Input** examples, each logging interactions into a text browser-style area.

---

## Project structure
qmlproject/
├─ main.py # Starts QGuiApplication, loads QML, exposes backend
├─ modules/
│ ├─ backend_functions.py # Shared backend logic from the UI project
│ └─ qml_backend.py # QObject wrapper exposing backend to QML (slots/signals)
└─ qml/
├─ main.qml # ApplicationWindow + StackView (navigation)
└─ components/
├─ LoginPage.qml # Login (admin / 1234) → SecondPage
├─ SecondPage.qml # Tabs + Next button back to login
├─ ButtonsTab.qml # Button-like widgets + log area
├─ DisplayTab.qml # Display widgets (progress, value, etc.) + log area
└─ InputTab.qml # Input widgets (combo, sliders, dial, spinbox) + log area

The **Python backend** is reused as-is from the widgets project, with `qml_backend.QmlBackend` acting as a thin adapter to expose:

- `login(username, password)` / `loginSuccess`, `loginFailed`, `goToLogin`  
- Logging helpers: `logButtonClick`, `logCheckboxToggle`, `logRadioToggle`, `logComboSelection`, `logSpinBoxValue`, `logSliderValue`, `logDialValue` (delegating to `BackendFunctions`). [web:117][web:138]

---

## Setup

Use the same virtual environment and dependencies as the UI project.

From the top-level workspace (where `Helloworld/` and `qmlproject/` live):


To run the QML project:

cd ..\qmlproject
..\Helloworld\venv\Scripts\activate
python main.py


If you use VS Code, there is a `tasks.json` entry **“Run QML main.py”** which:

1. Creates/updates the venv in `Helloworld/`  
2. Installs dependencies from `requirements.txt`  
3. Activates that venv and runs `qmlproject/main.py`. [file:120]

---

## How the QML app works

### main.py / main.qml

- `main.py` creates `QGuiApplication`, sets up a `QQmlApplicationEngine`, and exposes an instance of `QmlBackend` to QML as a context property named `backend`. [web:123][web:124]  
- `qml/main.qml` defines an `ApplicationWindow` with a single `StackView`:
  - Initial page: `"components/LoginPage.qml"`.
  - A `Connections` block listens to `backend.loginSuccess` / `backend.goToLogin` and pushes or resets to `SecondPage.qml` / `LoginPage.qml`. [web:129][web:141]

### Login flow

`LoginPage.qml`:

- Simple `Page` with `TextField` for username and password and a **Login** button.
- On click, calls `backend.login(user.text, pwd.text)`.
- On `loginSuccess`, `main.qml` pushes `"components/SecondPage.qml"` onto the `StackView`.
- On `loginFailed`, the page shows an error label.

Credentials are the same as the UI project: **admin / 1234**, implemented in `BackendFunctions.validate_login`. [file:118]

### Second page and tabs

`SecondPage.qml`:

- `TabBar` + `StackLayout` hosting three tabs:
  - **Buttons** → `ButtonsTab.qml`
  - **Display** → `DisplayTab.qml`
  - **Input** → `InputTab.qml` [web:132]
- A **Next** button in the top-right calls `backend.back_to_login()`, which triggers `backend.goToLogin` and returns to the login page via `main.qml`.

---

## Tabs overview

All tabs follow the same teaching pattern:

- Top area: widgets to experiment with.
- Bottom area: a scrollable `TextArea` acting like a **TextBrowser**.
- Every interaction calls a backend logging helper so the user sees timestamped, readable log lines (e.g., “Button 'X' clicked”, “CheckBox 'Option 1' checked”). [file:118][web:134]

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

---

## Learning goals

This QML project is intended to sit side-by-side with the original widgets/UI project so learners can:

- Compare **Qt Widgets (`.ui` + `helloworld.py`)** vs **Qt Quick (`.qml` + `main.py`)** using the same backend. [web:126][web:138]  
- See how **StackView** and `TabBar + StackLayout` organize multi-page QML UIs. [web:132][web:141]  
- Understand how to:
  - Expose a Python backend (`BackendFunctions`) into QML with a small `QObject` adapter (`QmlBackend`) and slots/signals.  
  - Log interactions centrally while keeping QML declarative and clean.  
  - Share business logic between UI technologies with minimal duplication.

This structure can be extended with more examples (charts, list models, etc.) while preserving the same Python backend and educational layout.
