# This Python file uses the following encoding: utf-8
"""Main application module for the Qt educational demo.

This module wires the generated UI (`ui_form.py`) to simple backend
helpers (in `modules/backend_functions.py`). The `Helloworld` class
initializes the UI, connects widget signals to handlers and demonstrates
how to log widget events to in-UI text browsers for educational purposes.

Run this file to start the demo application.
"""

import sys
import os

from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QLabel
from PySide6.QtCore import Qt, QDate, QUrl
from PySide6.QtGui import QAction, QDesktopServices, QPixmap, QPainter
from PySide6.QtSvg import QSvgRenderer
from PySide6.QtSvgWidgets import QSvgWidget
from modules.backend_functions import BackendFunctions

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Helloworld

class Helloworld(QMainWindow):
    """Main window controller.

    Responsibilities:
    - instantiate and configure the generated UI class `Ui_Helloworld`
    - create a `BackendFunctions` instance for logic/helpers
    - wire widget signals (clicks, value changes) to handler methods
    - provide small helper dialogs and navigation between stacked pages
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Helloworld()
        self.ui.setupUi(self)

        self.backend = BackendFunctions()

        # Add a Help -> About Demo menu action that shows demo credentials
        # Make the existing top-level menu more friendly
        try:
            self.ui.menumenu.setTitle("Help")
        except Exception:
            pass
        self.about_action = QAction("About Demo", self)
        self.about_action.triggered.connect(self.show_about_dialog)
        try:
            self.ui.menumenu.addAction(self.about_action)
        except Exception:
            # If menumenu not available for some reason, ignore gracefully
            pass

        # ==================== SETUP LOGIN PAGE ====================
        self.setup_login_page()
        
        # ==================== SETUP TAB 1: BUTTONS ====================
        self.setup_tab1_buttons()
        
        # ==================== SETUP TAB 2: INPUT/DISPLAY WIDGETS ====================
        self.setup_tab2_input_widgets()
        
        # ==================== SETUP TAB 3: DISPLAY WIDGETS ====================
        self.setup_tab3_display_widgets()

    # ==================== SETUP LOGIN PAGE ====================
    def setup_login_page(self) -> None:
        """Setup login page connections and show hint"""
        self.ui.Login_pushbutton.clicked.connect(self.on_login_clicked)
        
        # Display login hint in tooltip with credentials and description
        login_info = self.backend.get_login_info()
        hint_text = f"""<b>Educational Qt Application</b>
<br><br>
This is a comprehensive Qt learning application demonstrating:
<br>• Widget layouts and stacking
<br>• Event handling and signals
<br>• Real-time data updates
<br>• Navigation between screens
<br><br>
<b>Demo Credentials (for learning):</b>
<br>Username: <b>{login_info['username']}</b>
<br>Password: <b>{login_info['password']}</b>
<br><br>
After login, explore all three tabs to see different widget examples!"""
        
        self.ui.username_label.setToolTip(hint_text)
        self.ui.password_label.setToolTip(hint_text)
        self.ui.username_lineEdit.setPlaceholderText("Enter username")
        self.ui.password_lineedit.setPlaceholderText("Enter password")

        # Add a small SVG logo above the login form for visual polish.
        # We create a QSvgWidget and insert it into the same grid used by the
        # generated UI (`gridLayout_3`). This avoids changing the generated
        # `ui_form.py` and keeps visual tweaks in this controller code.
        try:
            # Prefer an official Qt logo if the user placed one at assets/qt_logo.svg
            svg_candidate = os.path.join("assets", "qt_logo.svg")
            png_candidate = os.path.join("assets", "qt_logo.png")
            # Use a cached combined banner image if present, otherwise compose it
            banner_w, banner_h = 700, 140
            combined_path = os.path.join("assets", "combined_banner.png")

            if os.path.exists(combined_path):
                # Load the pre-composed banner directly
                composed = QPixmap(combined_path)
            else:
                # Compose banner SVG into a single QPixmap (use `logo.svg` only)
                banner_svg = os.path.join("assets", "logo.svg")
                composed = QPixmap(banner_w, banner_h)
                composed.fill(Qt.GlobalColor.transparent)

                # Render SVG banner if available; we specifically use the SVG
                # artwork as the authoritative banner (no PNG overlay).
                if os.path.exists(banner_svg):
                    renderer = QSvgRenderer(banner_svg)
                    if renderer.isValid():
                        painter = QPainter(composed)
                        renderer.render(painter)
                        painter.end()

                # Save composed banner for future runs
                try:
                    os.makedirs(os.path.dirname(combined_path), exist_ok=True)
                    composed.save(combined_path, "PNG")
                except Exception:
                    pass

            # Show the composed banner in a QLabel
            banner_label = QLabel(parent=self.ui.page)
            banner_label.setPixmap(composed)
            banner_label.setFixedSize(banner_w, banner_h)
            banner_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            banner_label.setContentsMargins(0, 0, 0, 0)
            banner_label.mousePressEvent = lambda ev: self.open_github()
            self.ui.gridLayout_3.addWidget(banner_label, 0, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter)
        except Exception:
            # If SVG support is missing, ignore gracefully — the app remains functional.
            pass

    def open_github(self) -> None:
        """Open the project GitHub repository in the default web browser."""
        try:
            url = QUrl("https://github.com/gurulinuxer/PyQt")
            QDesktopServices.openUrl(url)
        except Exception:
            QMessageBox.information(self, "Open GitHub", "Unable to open the browser.")

    def on_login_clicked(self) -> None:
        """Handle login button click.

        Reads the username and password text widgets and performs
        basic validation before calling the backend validator.
        """
        username = self.ui.username_lineEdit.text().strip()
        password = self.ui.password_lineedit.text().strip()

        if not username or not password:
            error_msg = "Validation Error!\n\n"
            if not username:
                error_msg += "• Username field is empty\n"
            if not password:
                error_msg += "• Password field is empty\n"
            error_msg += "\nPlease fill in all fields."
            QMessageBox.warning(self, "Validation Error", error_msg)
            return

        if self.backend.validate_login(username, password):
            QMessageBox.information(self, "Login Success", f"Welcome {username}!")
            # Switch to second page (page_2)
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_2)
        else:
            login_info = self.backend.get_login_info()
            hint_message = f"""Invalid username or password!

<b>You entered:</b>
Username: {username}
Password: {'*' * len(password)} (hidden)

<b>Hint for educational purposes:</b>
Username: {login_info['username']}
Password: {login_info['password']}

Tip: You can also find demo credentials from the top menu: <b>Help → About Demo</b>.

Please try again."""
            QMessageBox.critical(self, "Login Failed", hint_message)
            self.ui.password_lineedit.clear()

    # ==================== TAB 1: BUTTONS ====================
    def setup_tab1_buttons(self) -> None:
        """Setup all button tab connections."""
        # Add initial description to TextBrowser
        # Use backend-provided HTML snippet for clarity and reuse
        self.ui.textBrowser_buttons.setHtml(self.backend.get_tab_buttons_intro())
        
        # PushButton
        self.ui.pushButton.clicked.connect(self.on_push_button_clicked)
        
        # ToolButton
        self.ui.toolButton.clicked.connect(self.on_tool_button_clicked)
        
        # RadioButtons (original + new ones)
        self.ui.radioButton.toggled.connect(self.on_radio_button_toggled)
        self.ui.radioButton_2.toggled.connect(self.on_radio_button_2_toggled)
        self.ui.radioButton_3.toggled.connect(self.on_radio_button_3_toggled)
        
        # CheckBoxes (original + new ones)
        self.ui.checkBox.toggled.connect(self.on_checkbox_toggled)
        self.ui.checkBox_2.toggled.connect(self.on_checkbox_2_toggled)
        self.ui.checkBox_3.toggled.connect(self.on_checkbox_3_toggled)
        
        # CommandLinkButton
        self.ui.commandLinkButton.clicked.connect(self.on_command_link_button_clicked)
        
        # DialogButtonBox
        self.ui.buttonBox.accepted.connect(self.on_dialog_ok_clicked)
        self.ui.buttonBox.rejected.connect(self.on_dialog_cancel_clicked)

    def on_push_button_clicked(self) -> None:
        """Handle PushButton click."""
        log_msg = self.backend.log_button_click("PushButton")
        self.ui.textBrowser_buttons.append(log_msg)

    def on_tool_button_clicked(self) -> None:
        """Handle ToolButton click."""
        log_msg = self.backend.log_button_click("ToolButton")
        self.ui.textBrowser_buttons.append(log_msg)

    def on_radio_button_toggled(self, checked: bool) -> None:
        """Handle RadioButton toggle."""
        label = self.ui.radioButton.text()
        log_msg = self.backend.log_radio_button_toggle(label, checked)
        self.ui.textBrowser_buttons.append(log_msg)

    def on_radio_button_2_toggled(self, checked: bool) -> None:
        """Handle RadioButton_2 toggle."""
        label = self.ui.radioButton_2.text()
        log_msg = self.backend.log_radio_button_toggle(label, checked)
        self.ui.textBrowser_buttons.append(log_msg)

    def on_radio_button_3_toggled(self, checked: bool) -> None:
        """Handle RadioButton_3 toggle."""
        label = self.ui.radioButton_3.text()
        log_msg = self.backend.log_radio_button_toggle(label, checked)
        self.ui.textBrowser_buttons.append(log_msg)

    def on_checkbox_toggled(self, checked: bool) -> None:
        """Handle CheckBox toggle."""
        label = self.ui.checkBox.text()
        log_msg = self.backend.log_checkbox_toggle(label, checked)
        self.ui.textBrowser_buttons.append(log_msg)

    def on_checkbox_2_toggled(self, checked: bool) -> None:
        """Handle CheckBox_2 toggle."""
        label = self.ui.checkBox_2.text()
        log_msg = self.backend.log_checkbox_toggle(label, checked)
        self.ui.textBrowser_buttons.append(log_msg)

    def on_checkbox_3_toggled(self, checked: bool) -> None:
        """Handle CheckBox_3 toggle."""
        label = self.ui.checkBox_3.text()
        log_msg = self.backend.log_checkbox_toggle(label, checked)
        self.ui.textBrowser_buttons.append(log_msg)

    def on_command_link_button_clicked(self) -> None:
        """Handle CommandLinkButton click."""
        log_msg = self.backend.log_button_click("CommandLinkButton")
        self.ui.textBrowser_buttons.append(log_msg)

    def on_dialog_ok_clicked(self) -> None:
        """Handle DialogButtonBox OK."""
        log_msg = self.backend.log_button_click("DialogButtonBox (OK)")
        self.ui.textBrowser_buttons.append(log_msg)

    def on_dialog_cancel_clicked(self) -> None:
        """Handle DialogButtonBox Cancel."""
        log_msg = self.backend.log_button_click("DialogButtonBox (Cancel)")
        self.ui.textBrowser_buttons.append(log_msg)

    # ==================== TAB 2: INPUT/DISPLAY WIDGETS ====================
    def setup_tab2_input_widgets(self) -> None:
        """Setup all input widget connections for tab 2."""
        # Add initial description to TextBrowser
        # Use backend-provided HTML snippet for clarity and reuse
        self.ui.textBrowser_input.setHtml(self.backend.get_tab_input_intro())
        
        # ComboBox
        self.ui.comboBox.addItems(["Option 1", "Option 2", "Option 3", "Option 4"])
        self.ui.comboBox.currentIndexChanged.connect(self.on_combo_box_changed)
        
        # FontComboBox
        self.ui.fontComboBox.currentFontChanged.connect(self.on_font_combo_changed)
        
        # SpinBox
        self.ui.spinBox.valueChanged.connect(self.on_spinbox_value_changed)
        
        # DoubleSpinBox
        self.ui.doubleSpinBox.valueChanged.connect(self.on_double_spinbox_value_changed)
        
        # Dial
        self.ui.dial.valueChanged.connect(self.on_dial_value_changed)
        
        # Vertical Slider
        self.ui.verticalSlider.valueChanged.connect(self.on_vertical_slider_changed)
        
        # Horizontal Slider
        self.ui.horizontalSlider.valueChanged.connect(self.on_horizontal_slider_changed)
        
        # LCDNumber - display spinbox value
        self.ui.spinBox.valueChanged.connect(self.ui.lcdNumber.display)
        
        # ProgressBar_2 - show spinbox value as percentage
        self.ui.spinBox.setMaximum(100)
        self.ui.spinBox.valueChanged.connect(self.ui.progressBar_2.setValue)
        
        # TextBrowser click (for demonstration)
        self.ui.textBrowser_input.mousePressEvent = self.on_text_browser_clicked

    def on_combo_box_changed(self, index: int) -> None:
        """Handle ComboBox selection change."""
        item = self.ui.comboBox.currentText()
        log_msg = self.backend.log_combo_selection("ComboBox", item, index)
        self.ui.textBrowser_input.append(log_msg)

    def on_font_combo_changed(self, font) -> None:
        """Handle FontComboBox selection change."""
        font_name = font.family()
        log_msg = self.backend.log_combo_selection("FontComboBox", font_name, 0)
        self.ui.textBrowser_input.append(log_msg)

    def on_spinbox_value_changed(self, value: int) -> None:
        """Handle SpinBox value change."""
        log_msg = self.backend.log_spinbox_value("SpinBox", value)
        self.ui.textBrowser_input.append(log_msg)

    def on_double_spinbox_value_changed(self, value) -> None:
        """Handle DoubleSpinBox value change."""
        log_msg = self.backend.log_spinbox_value("DoubleSpinBox", value)
        self.ui.textBrowser_input.append(log_msg)

    def on_dial_value_changed(self, value: int) -> None:
        """Handle Dial value change."""
        log_msg = self.backend.log_dial_value("Dial", value)
        self.ui.textBrowser_input.append(log_msg)

    def on_vertical_slider_changed(self, value: int) -> None:
        """Handle Vertical Slider value change."""
        log_msg = self.backend.log_slider_value("VerticalSlider", value)
        self.ui.textBrowser_input.append(log_msg)

    def on_horizontal_slider_changed(self, value: int) -> None:
        """Handle Horizontal Slider value change."""
        log_msg = self.backend.log_slider_value("HorizontalSlider", value)
        self.ui.textBrowser_input.append(log_msg)

    def on_text_browser_clicked(self, event) -> None:
        """Handle TextBrowser click (educational log)."""
        log_msg = self.backend.log_text_browser_click()
        # Don't append to avoid infinite loop, just print to console
        print(log_msg)
        super(type(self.ui.textBrowser_input), self.ui.textBrowser_input).mousePressEvent(event)

    # ==================== TAB 3: DISPLAY WIDGETS ====================
    def setup_tab3_display_widgets(self) -> None:
        """Setup display widgets for tab 3."""
        # Next Button - navigate back to login page
        self.ui.pushButton_2.clicked.connect(self.on_next_button_clicked)
        
        # CalendarWidget - for date selection demonstration
        self.ui.calendarWidget.clicked.connect(self.on_calendar_date_clicked)
        
        # TextBrowser_display - show educational content
        # Use backend-provided HTML snippet for clarity and reuse
        self.ui.textBrowser_display.setHtml(self.backend.get_tab_display_intro())

    def on_next_button_clicked(self) -> None:
        """Handle Next button click - navigate back to login page (page 1)."""
        log_msg = self.backend.log_button_click("Next Button")
        self.ui.textBrowser_display.append(log_msg)
        
        # Clear the login fields for next login attempt
        self.ui.username_lineEdit.clear()
        self.ui.password_lineedit.clear()
        
        # Switch back to page 1 (login page)
        self.ui.stackedWidget.setCurrentWidget(self.ui.page)

    def on_calendar_date_clicked(self, date: QDate) -> None:
        """Handle calendar date selection."""
        date_str = date.toString("dddd, MMMM d, yyyy")
        log_msg = f"[{self.backend.format_timestamp()}] Calendar date selected: {date_str}"
        self.ui.textBrowser_display.append(log_msg)

    def show_about_dialog(self) -> None:
        """Show About dialog with demo credentials and short instructions."""
        info = self.backend.get_login_info()
        about_html = f"""
<b>Qt Educational Demo</b>
<br><br>
This demo showcases many Qt widgets and how their signals work.
<br><br>
<b>Demo credentials (for learning):</b>
<br>Username: <b>{info['username']}</b>
<br>Password: <b>{info['password']}</b>
<br><br>
Use these credentials on the login screen to explore the tabs and widgets.
"""
        QMessageBox.information(self, "About Demo", about_html)


if __name__ == "__main__":
    # Application entry point.
    # Run from command line or from an integrated terminal inside VS Code:
    # .\venv\Scripts\Activate.ps1; python helloworld.py
    app = QApplication(sys.argv)
    widget = Helloworld()
    widget.show()
    sys.exit(app.exec())
