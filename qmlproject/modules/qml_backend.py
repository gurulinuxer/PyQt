from PySide6.QtCore import QObject, Slot, Signal
from .backend_functions import BackendFunctions

class QmlBackend(QObject):
    loginSuccess = Signal()
    loginFailed = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self._backend = BackendFunctions()

    @Slot(str, str)
    def login(self, username: str, password: str) -> None:
        if self._backend.validate_login(username, password):
            self.loginSuccess.emit()
        else:
            self.loginFailed.emit("Invalid username or password")
