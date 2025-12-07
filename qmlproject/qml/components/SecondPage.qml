import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

Page {
    id: secondPage

    ColumnLayout {
        anchors.fill: parent

        TabBar {
            id: tabBar
            Layout.fillWidth: true

            TabButton { text: "Buttons" }
            TabButton { text: "Display" }
            TabButton { text: "Input" }
        }

        StackLayout {
            id: tabStack
            Layout.fillWidth: true
            Layout.fillHeight: true
            currentIndex: tabBar.currentIndex

            // Each of these files should have root Item/Page (not recursive)
            Loader { source: "ButtonsTab.qml" }
            Loader { source: "DisplayTab.qml" }
            Loader { source: "InputTab.qml" }
        }
    }
}
