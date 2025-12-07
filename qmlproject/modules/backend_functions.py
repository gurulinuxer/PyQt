"""Backend helper functions for the Qt educational demo.

This module contains small, focused backend utilities used by the
`Helloworld` UI. It provides:
- small dialog helpers for simple popups
- login validation (demo credentials)
- timestamped event log message builders used by the UI text browsers

The code is intentionally minimal and synchronous to keep the
examples easy to follow for beginners.
"""

from datetime import datetime
from typing import Dict

from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton


class BackendFunctions:
    """Collection of backend helper methods for the demo UI.

    The class is intentionally stateless: all methods are pure helpers
    that build messages or show simple dialogs. Keeping business logic
    here demonstrates a minimal separation of concerns between UI and
    backend code.
    """

    def __init__(self) -> None:
        # No initialization state required for these stateless helpers.
        return None

    class Dialogs:
        """Small dialog helpers.

        These are lightweight helpers that create and show simple modal
        dialogs. They are implemented as an inner class to group
        dialog-related code together.
        """

        def show_message_dialog(self, title: str, message: str) -> None:
            """Show a simple modal dialog with an OK button.

            Parameters
            ----------
            title:
                Window title shown on the dialog.
            message:
                Plain text message placed in the dialog body.
            """
            dialog = QDialog()
            dialog.setWindowTitle(title)

            layout = QVBoxLayout()
            label = QLabel(message)
            layout.addWidget(label)

            ok_button = QPushButton("OK")
            ok_button.clicked.connect(dialog.accept)
            layout.addWidget(ok_button)

            dialog.setLayout(layout)
            dialog.exec()

    def open_helloworld_dialog(self) -> None:
        """Open a simple Hello World dialog (used as a demo callback).

        The UI wires a button directly to this helper in examples; keeping
        the dialog creation in the backend keeps the example tidy.
        """
        dialog = self.Dialogs()
        dialog.show_message_dialog(
            "Hello World",
            "This is a Hello World dialog from the backend functions.")

    # ==================== LOGIN FUNCTIONS ====================
    def validate_login(self, username: str, password: str) -> bool:
        """Return True when provided credentials match demo values.

        This function uses a fixed demo username/password pair for
        educational purposes only.
        """
        return username == "admin" and password == "1234"

    def get_login_info(self) -> Dict[str, str]:
        """Return example login credentials for educational purposes.

        Returns a small dictionary containing the demo username and
        password so the UI can display them in tooltips or dialogs.
        """
        return {
            "username": "admin",
            "password": "1234",
            "note": "Use these credentials to login",
        }

    # ==================== EVENT LOGGING FUNCTIONS ====================
    def format_timestamp(self) -> str:
        """Return current timestamp formatted to millisecond precision."""
        return datetime.now().strftime("%H:%M:%S.%f")[:-3]

    def log_button_click(self, button_name: str) -> str:
        """Return a timestamped message for a button click event."""
        return f"[{self.format_timestamp()}] Button '{button_name}' clicked"

    def log_radio_button_toggle(self, button_name: str, checked: bool) -> str:
        """Return a timestamped message when a radio button changes state."""
        status = "selected" if checked else "deselected"
        return f"[{self.format_timestamp()}] RadioButton '{button_name}' {status}"

    def log_checkbox_toggle(self, checkbox_name: str, checked: bool) -> str:
        """Return a timestamped message when a checkbox changes state."""
        status = "checked" if checked else "unchecked"
        return f"[{self.format_timestamp()}] CheckBox '{checkbox_name}' {status}"

    def log_combo_selection(self, combo_name: str, item: str, index: int) -> str:
        """Return a timestamped message when a combo box selection changes."""
        return (
            f"[{self.format_timestamp()}] {combo_name} changed to '{item}' "
            f"(index: {index})"
        )

    def log_spinbox_value(self, spinbox_name: str, value) -> str:
        """Return a timestamped message for spinbox value changes."""
        return f"[{self.format_timestamp()}] {spinbox_name} value: {value}"

    def log_slider_value(self, slider_name: str, value: int) -> str:
        """Return a timestamped message for slider value changes."""
        return f"[{self.format_timestamp()}] {slider_name} value: {value}"

    def log_dial_value(self, dial_name: str, value: int) -> str:
        """Return a timestamped message for dial value changes."""
        return f"[{self.format_timestamp()}] {dial_name} value: {value}"

    def log_text_browser_click(self) -> str:
        """Return a timestamped message for TextBrowser clicks."""
        return f"[{self.format_timestamp()}] TextBrowser clicked"

    # ==================== TAB INTRO TEXT HELPERS ====================
    def get_tab_buttons_intro(self) -> str:
        """Return initial HTML content for the Buttons tab TextBrowser.

        Keeping these HTML snippets in the backend centralizes content and
        makes the UI module (`helloworld.py`) cleaner and easier to read.
        """
        return (
            """
<b>Educational Widget Showcase - Tab 1: Buttons & Selection Widgets</b>
<br><br>
<b>Description:</b>
This tab demonstrates various button and selection widgets in Qt, including their interactions and events.
<br><br>
<b>Widgets shown:</b>
<br>• <b>PushButton:</b> Standard button - try clicking it
<br>• <b>ToolButton:</b> Button with tool icon style
<br>• <b>RadioButtons:</b> Mutually exclusive selection (Computer, Mobile, Laptop)
<br>• <b>CheckBoxes:</b> Independent toggle options (Option 1, 2, 3)
<br>• <b>CommandLinkButton:</b> Button with description text
<br>• <b>DialogButtonBox:</b> Standard Ok/Cancel buttons
<br><br>
<b>Features demonstrated:</b>
<br>• Button click events
<br>• Radio button selection (only one can be selected)
<br>• Checkbox toggling (multiple can be selected)
<br>• Real-time event logging with timestamps
<br>• Widget state tracking
<br><br>
<b>Try this:</b> Click buttons and toggle radio buttons/checkboxes below to see the event logs!
<br><hr>
            """
        )

    def get_tab_input_intro(self) -> str:
        """Return initial HTML content for the Input tab TextBrowser."""
        return (
            """
<b>Educational Widget Showcase - Tab 2: Input & Display Widgets</b>
<br><br>
<b>Description:</b>
This tab demonstrates input widgets that allow users to enter or select values, and display widgets that show real-time updates.
<br><br>
<b>Input Widgets shown:</b>
<br>• <b>ComboBox:</b> Dropdown selection (Option 1-4)
<br>• <b>FontComboBox:</b> Select system fonts
<br>• <b>SpinBox:</b> Integer value input (0-100)
<br>• <b>DoubleSpinBox:</b> Decimal value input
<br>• <b>Dial:</b> Circular value selector (rotatable)
<br>• <b>Sliders:</b> Vertical and Horizontal value selectors
<br><br>
<b>Display Widgets (synced with inputs):</b>
<br>• <b>LCDNumber:</b> Shows SpinBox value in LCD display style
<br>• <b>ProgressBar:</b> Shows SpinBox value as progress percentage
<br><br>
<b>Features demonstrated:</b>
<br>• Real-time value tracking
<br>• Signal connections across widgets
<br>• Multiple input methods for same value
<br>• Automatic display updates
<br>• Event logging with timestamps
<br><br>
<b>Try this:</b> Adjust the SpinBox, Sliders, or Dial - watch the LCDNumber and ProgressBar update in real-time!
<br><hr>
            """
        )

    def get_tab_display_intro(self) -> str:
        """Return initial HTML content for the Display tab TextBrowser."""
        return (
            """
<b>Educational Widget Showcase - Tab 3</b>
<br><br>
This tab demonstrates display and selection widgets in Qt:
<br><br>
<b>Widgets shown:</b>
<br>• <b>CalendarWidget:</b> Select dates - click on dates to see interaction
<br>• <b>Next Button:</b> Navigate back to login page (page 1)
<br>• <b>TextBrowser:</b> Shows rich text with formatting
<br><br>
<b>Features demonstrated:</b>
<br>• Widget signal connections across tabs
<br>• Navigation between pages
<br>• Date selection
<br>• Text formatting with HTML
<br><br>
<b>Try this:</b> Click the "Next" button to go back to the login page and experience the navigation flow!
            """
        )