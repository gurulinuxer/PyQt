import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

Page {
    id: secondPage

    ColumnLayout {
        anchors.fill: parent
        anchors.margins: 8
        spacing: 8

        // Top row with Next button on the right
        RowLayout {
            Layout.fillWidth: true

            Item { Layout.fillWidth: true }   // spacer pushes button to the right

            Button {
                id: nextButton
                text: "Next"
                Layout.preferredWidth: 120    // bigger button
                Layout.preferredHeight: 40
                font.pixelSize: 18
                onClicked: {
                    console.log("SecondPage: Next clicked, requesting goToLogin")
                    backend.back_to_login()
                }
            }
        }

        // Tabs and content below
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

            Loader { source: "ButtonsTab.qml" }
            Loader { source: "DisplayTab.qml" }
            Loader { source: "InputTab.qml" }
        }
    }
}
