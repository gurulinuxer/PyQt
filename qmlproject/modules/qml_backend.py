from PySide6.QtCore import QObject, Slot, Signal, QThread
import time
from .backend_functions import BackendFunctions  # already there

class ThreadWorker(QObject):
    progress = Signal(str)
    finished = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self._running = False

    @Slot()
    def run(self):
        # This runs in the worker thread
        self._running = True
        counter = 0
        while self._running:
            counter += 1
            self.progress.emit(f"[{counter}] Worker tick")
            time.sleep(0.5)
        self.finished.emit()

    @Slot()
    def stop(self):
        self._running = False



class QmlBackend(QObject):
    loginSuccess = Signal()
    loginFailed = Signal(str)
    goToLogin = Signal()

    # signal name must match QML handler onThreadLog
    threadLog = Signal(str)
    stopWorker = Signal()  

    def __init__(self, parent=None):
        super().__init__(parent)
        self._backend = BackendFunctions()

        # init worker/thread attributes so AttributeError goes away
        self._worker_thread: QThread | None = None
        self._worker: ThreadWorker | None = None

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
    
    @Slot()
    def start_thread_example(self):
        if self._worker_thread is not None:
            # already running
            return

        self._worker_thread = QThread()
        self._worker = ThreadWorker()
        self._worker.moveToThread(self._worker_thread)

        self._worker_thread.started.connect(self._worker.run)
        self._worker.progress.connect(self.threadLog)
        self._worker.finished.connect(self._on_worker_finished)

        self._worker_thread.start()
        self.threadLog.emit("[Threads] Worker thread started")

    @Slot()
    def stop_thread_example(self):
        if self._worker is None:
            return
        # Direct call is fine because this slot is invoked in GUI thread,
        # Qt delivers it to worker thread as queued connection
        self._worker.stop()
        self.threadLog.emit("[Threads] Stop requested from QML")

    @Slot()
    def _on_worker_finished(self):
        self.threadLog.emit("[Threads] Worker finished")
        if self._worker_thread is not None:
            self._worker_thread.quit()
            self._worker_thread.wait()
        self._worker = None
        self._worker_thread = None



