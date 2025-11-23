# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from modules.backend_functions import BackendFunctions

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Helloworld

class Helloworld(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Helloworld()
        self.ui.setupUi(self)

        self.backend = BackendFunctions()

        self.ui.pushButton_hello.clicked.connect(self.backend.open_helloworld_dialog)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Helloworld()
    widget.show()
    sys.exit(app.exec())
