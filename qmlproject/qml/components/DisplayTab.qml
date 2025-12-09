import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

Page {
    id: displayTab

    ColumnLayout {
        anchors.fill: parent
        anchors.margins: 8
        spacing: 8

        Label {
            text: "Display widgets demo"
            font.bold: true
            Layout.alignment: Qt.AlignHCenter
        }

        ProgressBar {
            id: progress
            from: 0
            to: 100
            value: 40
            Layout.fillWidth: true
        }

        Slider {
            id: slider
            from: 0
            to: 100
            value: 40
            Layout.fillWidth: true
            onValueChanged: {
                progress.value = value
                logText.appendText(
                    backend.logSliderValue("Display Progress/Slider", Math.round(value))
                )
            }
        }

        Label {
            text: "Value: " + Math.round(slider.value)
        }

        // Replace the existing TextArea with this block

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

                    // move cursor to end and ensure it is visible
                    cursorPosition = text.length
                }
            }
        }
    }
}
