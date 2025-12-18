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

            Item { Layout.fillWidth: true }   // spacer pushes button to right

            Button {
                id: nextButton
                text: "Next"
                Layout.preferredWidth: 120
                Layout.preferredHeight: 40
                font.pixelSize: 18
                onClicked: {
                    console.log("SecondPage: Next clicked, requesting goToLogin")
                    backend.back_to_login()
                }
            }
        }

        // Tab bar
        TabBar {
            id: tabBar
            Layout.fillWidth: true
            Layout.preferredHeight: 44    // make tabs taller

            TabButton {
                text: "Buttons"
                font.pixelSize: 14
            }
            TabButton {
                text: "Input"            // center tab
                font.pixelSize: 14
            }
            TabButton {
                text: "Display"          // right tab
                font.pixelSize: 14
            }
            TabButton { 
                text: "3D";      
                font.pixelSize: 14 
            }
            TabButton { 
                text: "Threads"; 
                font.pixelSize: 14 
            }    

        }

        // Tab contents
        StackLayout {
            id: tabStack
            Layout.fillWidth: true
            Layout.fillHeight: true
            Layout.topMargin: 4           // small gap below tabs
            currentIndex: tabBar.currentIndex

            Loader { source: "ButtonsTab.qml" }   // index 0
            Loader { source: "InputTab.qml" }     // index 1
            Loader { source: "DisplayTab.qml" }   // index 2
            Loader { source: "ThreeDTab.qml" }    // index 3
            Loader { source: "ThreadsTab.qml" }   // index 4
        }
    }
}
