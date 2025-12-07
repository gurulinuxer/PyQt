import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

Item {
    id: secondPage
    
    ColumnLayout {
        anchors.fill: parent
        
        Button {
            text: "Navigate to login page"
            Layout.alignment: Qt.AlignLeft
            onClicked: stackView.pop()
        }
        
        TabBar {
            id: tabBar
            currentIndex: 0
            
            TabButton { text: "Buttons" }
            TabButton { text: "Input" }
            TabButton { text: "Display" }
        }
        
        StackLayout {
            currentIndex: tabBar.currentIndex
            Layout.fillWidth: true
            Layout.fillHeight: true
            
            ButtonsTab {}
            InputTab {}
            DisplayTab {}
        }
    }
}
