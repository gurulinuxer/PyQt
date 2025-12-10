import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

Page {
    ColumnLayout {
        anchors.fill: parent
        anchors.margins: 16
        spacing: 8

        Label {
            text: "3D examples require Qt Quick 3D (QtQuick3D)."
            font.pixelSize: 18
            font.bold: true
        }

        Label {
            text: "Install a PySide6 build that includes QtQuick3D, " +
                  "then this tab can show a rotating 3D cube with angle logging."
            wrapMode: Text.Wrap
        }
    }
}
