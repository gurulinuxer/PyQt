import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

Page {
    id: threadsTab

    ColumnLayout {
        anchors.fill: parent
        anchors.margins: 8
        spacing: 8

        Label {
            text: "Threads demo (QThread worker logging to QML)"
            font.bold: true
            Layout.alignment: Qt.AlignLeft
        }

        RowLayout {
            Layout.fillWidth: true
            spacing: 8

            Button {
                text: "Start worker"
                onClicked: {
                    logText.appendText("[Threads] Start requested")
                    backend.start_thread_example()
                }
            }

            Button {
                text: "Stop worker"
                onClicked: {
                    logText.appendText("[Threads] Stop requested")
                    backend.stop_thread_example()
                }
            }
        }

        ScrollView {
            Layout.fillWidth: true
            Layout.fillHeight: true

            TextArea {
                id: logText
                width: parent.width
                wrapMode: TextArea.Wrap
                readOnly: true

                function appendText(t) {
                    if (text.length > 0)
                        text += "\n"
                    text += t
                    cursorPosition = text.length
                }
            }
        }
    }

    Connections {
        target: backend
        function onThreadLog(message) {
            logText.appendText(message)
        }
    }
}
