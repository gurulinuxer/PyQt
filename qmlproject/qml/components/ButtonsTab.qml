import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

Page {
    id: buttonsTab

    ColumnLayout {
        anchors.fill: parent
        anchors.margins: 8
        spacing: 8

        // Row of buttons / toggles
        RowLayout {
            Layout.fillWidth: true
            spacing: 10

            Button {
                text: "Push Button"
                onClicked: logText.appendText(backend.logButtonClick("Push Button"))
            }

            ToolButton {
                text: "Tool"
                onClicked: logText.appendText(backend.logButtonClick("ToolButton"))
            }

            CheckBox {
                id: checkBox1
                text: "Option 1"
                onToggled: {
                    logText.appendText(
                        backend.logCheckboxToggle("Option 1", checked)
                    )
                }
            }

            CheckBox {
                id: checkBox2
                text: "Option 2"
                onToggled: {
                    logText.appendText(
                        backend.logCheckboxToggle("Option 2", checked)
                    )
                }
            }

            RadioButton {
                id: radioA
                text: "Choice A"
                onToggled: {
                    if (checked)
                        logText.appendText(
                            backend.logRadioToggle("Choice A", true)
                        )
                    else
                        logText.appendText(
                            backend.logRadioToggle("Choice A", false)
                        )
                }
            }

            RadioButton {
                id: radioB
                text: "Choice B"
                onToggled: {
                    if (checked)
                        logText.appendText(
                            backend.logRadioToggle("Choice B", true)
                        )
                    else
                        logText.appendText(
                            backend.logRadioToggle("Choice B", false)
                        )
                }
            }
        }

        // Log area similar to TextBrowser
        TextArea {
            id: logText
            Layout.fillWidth: true
            Layout.fillHeight: true
            readOnly: true
            wrapMode: TextArea.Wrap

            function appendText(t) {
                if (text.length > 0)
                    text += "\n"
                text += t
            }
        }
    }
}
