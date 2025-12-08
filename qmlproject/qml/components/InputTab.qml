import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

Page {
    id: inputTab

    ColumnLayout {
        anchors.fill: parent
        anchors.margins: 8
        spacing: 10

        // TOP: all input widgets with fixed height
        RowLayout {
            id: inputsRow
            spacing: 10
            Layout.fillWidth: true
            Layout.preferredHeight: 140   // fixed height so widgets don't move

            ComboBox {
                id: comboBox
                model: ["Option 1", "Option 2", "Option 3"]
                Layout.preferredWidth: 150
                onCurrentIndexChanged: {
                    logText.appendText(
                        backend.logComboSelection(
                            "Input ComboBox",
                            currentText,
                            currentIndex
                        )
                    )
                }
            }

            ComboBox {
                id: fontComboBox
                model: ["Arial", "Times New Roman", "Courier New"]
                Layout.preferredWidth: 150
                onCurrentIndexChanged: {
                    logText.appendText(
                        backend.logComboSelection(
                            "Font ComboBox",
                            currentText,
                            currentIndex
                        )
                    )
                }
            }

            Dial {
                id: dial
                from: 0
                to: 100
                value: 50
                Layout.preferredHeight: 100
                Layout.preferredWidth: 100
                onValueChanged: {
                    logText.appendText(
                        backend.logDialValue("Input Dial", Math.round(value))
                    )
                }
            }

            Slider {
                id: verticalSlider
                orientation: Qt.Vertical
                from: 0
                to: 100
                value: 50
                Layout.fillHeight: true
                onValueChanged: {
                    logText.appendText(
                        backend.logSliderValue("Vertical Slider", Math.round(value))
                    )
                }
            }

            Slider {
                id: horizontalSlider
                from: 0
                to: 100
                value: 50
                Layout.fillWidth: true
                onValueChanged: {
                    logText.appendText(
                        backend.logSliderValue("Horizontal Slider", Math.round(value))
                    )
                }
            }

            SpinBox {
                id: spinBox
                from: 0
                to: 100
                value: 50
                Layout.preferredWidth: 80
                onValueChanged: {
                    logText.appendText(
                        backend.logSpinBoxValue("Input SpinBox", value)
                    )
                }
            }

            Slider {
                id: progressSlider
                from: 0
                to: 100
                value: 24
                Layout.preferredWidth: 150
                onValueChanged: {
                    logText.appendText(
                        backend.logSliderValue("Progress Slider", Math.round(value))
                    )
                }
            }
        }

        Button {
            text: "Log input snapshot"
            Layout.alignment: Qt.AlignLeft
            onClicked: {
                var lines = []
                lines.push(
                    backend.logComboSelection(
                        "Input ComboBox",
                        comboBox.currentText,
                        comboBox.currentIndex
                    )
                )
                lines.push(
                    backend.logComboSelection(
                        "Font ComboBox",
                        fontComboBox.currentText,
                        fontComboBox.currentIndex
                    )
                )
                lines.push(
                    backend.logDialValue("Input Dial", Math.round(dial.value))
                )
                lines.push(
                    backend.logSliderValue("Vertical Slider", Math.round(verticalSlider.value))
                )
                lines.push(
                    backend.logSliderValue("Horizontal Slider", Math.round(horizontalSlider.value))
                )
                lines.push(
                    backend.logSpinBoxValue("Input SpinBox", spinBox.value)
                )
                lines.push(
                    backend.logSliderValue("Progress Slider", Math.round(progressSlider.value))
                )
                logText.appendText(lines.join("\n"))
            }
        }

        // BOTTOM: text browser-style log with auto-scroll, fills remaining space
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

                    // move cursor to end; ScrollView will keep latest part visible
                    cursorPosition = text.length
                }
            }
        }
    }
}
