from PySide6.QtCore import QObject, Slot, Signal
from .backend_functions import BackendFunctions  # already there

class QmlBackend(QObject):
    loginSuccess = Signal()
    loginFailed = Signal(str)
    goToLogin = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self._backend = BackendFunctions()

    @Slot(str, str)
    def login(self, username: str, password: str) -> None:
        if self._backend.validate_login(username, password):
            self.loginSuccess.emit()
        else:
            self.loginFailed.emit("Invalid username or password")

    @Slot()
    def back_to_login(self):
        self.goToLogin.emit()

    # NEW: input/log helpers reused from backend_functions.py
    @Slot(str, result=str)
    def logButtonClick(self, button_name: str) -> str:
        return self._backend.log_button_click(button_name)

    @Slot(str, str, int, result=str)
    def logComboSelection(self, combo_name: str, item: str, index: int) -> str:
        return self._backend.log_combo_selection(combo_name, item, index)

    @Slot(str, int, result=str)
    def logSpinBoxValue(self, spinbox_name: str, value: int) -> str:
        return self._backend.log_spinbox_value(spinbox_name, value)

    @Slot(str, int, result=str)
    def logSliderValue(self, slider_name: str, value: int) -> str:
        return self._backend.log_slider_value(slider_name, value)

    @Slot(str, int, result=str)
    def logDialValue(self, dial_name: str, value: int) -> str:
        return self._backend.log_dial_value(dial_name, value)
    @Slot(str, bool, result=str)
    def logCheckboxToggle(self, name: str, checked: bool) -> str:
        return self._backend.log_checkbox_toggle(name, checked)

    @Slot(str, bool, result=str)
    def logRadioToggle(self, name: str, checked: bool) -> str:
        return self._backend.log_radio_button_toggle(name, checked)
    @Slot(str, bool, result=str)
    def logSwitchToggle(self, switchName: str, isChecked: bool) -> str:
        """Log SwitchDelegate toggle events"""
        status = "ON" if isChecked else "OFF"
        message = f"Switch '{switchName}' → {status}"
        print(f"QML: {message}")
        return message  # Now returns for QML appendText()



