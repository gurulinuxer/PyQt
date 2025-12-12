import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

Page {
    id: threeDTab

    ColumnLayout {
        anchors.fill: parent
        anchors.margins: 8
        spacing: 8

        Label {
            text: "Pseudo-3D cube rotation demo (drag to rotate)"
            font.bold: true
            Layout.alignment: Qt.AlignLeft
        }

        // TOP: fixed-height area with centered square
        Item {
            Layout.fillWidth: true
            Layout.preferredHeight: 260

            Rectangle {
                id: cube
                width: 160
                height: 160
                color: "#3daee9"
                border.color: "#1a5a7a"
                radius: 8
                anchors.centerIn: parent

                transform: Rotation {
                    id: rot
                    origin.x: cube.width / 2
                    origin.y: cube.height / 2
                    axis.x: 0
                    axis.y: 0
                    axis.z: 1
                    angle: 0
                }

                MouseArea {
                    anchors.fill: parent
                    property real lastX: 0

                    onPressed: lastX = mouse.x

                    onPositionChanged: {
                        var dx = mouse.x - lastX
                        lastX = mouse.x

                        // update angle and wrap to 0–360
                        var newAngle = rot.angle + dx * 0.7
                        newAngle = ((newAngle % 360) + 360) % 360
                        rot.angle = newAngle

                        var msg = "[" + Qt.formatDateTime(new Date(), "hh:mm:ss.zzz") + "] "
                                + "Pseudo-3D cube angle: "
                                + newAngle.toFixed(1) + "°"
                        logText.appendText(msg)
                    }
                }

                Label {
                    anchors.centerIn: parent
                    text: Math.round(rot.angle) + "°"
                    color: "white"
                    font.pixelSize: 26
                    font.bold: true
                }
            }
        }

        // BOTTOM: log area
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
}
