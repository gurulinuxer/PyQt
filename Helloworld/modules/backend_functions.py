from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton

class BackendFunctions:
    def __init__(self):
        pass

    class Dialogs:
        def show_message_dialog(self, title: str, message: str):
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
    
    def open_helloworld_dialog(self):
        dialog = self.Dialogs()
        dialog.show_message_dialog("Hello World", "This is a Hello World dialog from the backend functions.")