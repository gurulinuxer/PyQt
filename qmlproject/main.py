import sys
from pathlib import Path
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import QUrl
from modules.qml_backend import QmlBackend

if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    backend = QmlBackend()
    engine.rootContext().setContextProperty("backend", backend)

    base_dir = Path(__file__).parent
    qml_file = base_dir / "qml" / "main.qml"
    engine.load(QUrl.fromLocalFile(str(qml_file)))
    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec())
