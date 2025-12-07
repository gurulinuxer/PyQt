import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

ScrollView {
    contentWidth: parent.width
    contentHeight: columnLayout.height
    
    ColumnLayout {
        id: columnLayout
        spacing: 10
        padding: 10
        
        RowLayout {
            spacing: 10
            Layout.fillWidth: true
            
            ComboBox {
                id: comboBox
                model: ["Option 1", "Option 2", "Option 3"]
                Layout.fillWidth: true
            }
            
            Rectangle {
                width: 1; height: parent.height
                color: "lightgray"
            }
            
            FontComboBox {
                id: fontComboBox
                Layout.fillWidth: true
            }
            
            Rectangle {
                width: 1; height: parent.height
                color: "lightgray"
            }
            
            Dial {
                id: dial
                value: 50
                minimumValue: 0
                maximumValue: 100
                Layout.preferredHeight: 100
                Layout.preferredWidth: 100
            }
            
            Rectangle {
                width: 1; height: parent.height
                color: "lightgray"
            }
            
            Slider {
                id: verticalSlider
                orientation: Qt.Vertical
                value: 0.5
                Layout.fillHeight: true
            }
            
            Rectangle {
                width: 1; height: parent.height
                color: "lightgray"
            }
            
            Slider {
                id: horizontalSlider
                value: 0.5
                Layout.fillWidth: true
            }
            
            Rectangle {
                width: 1; height: parent.height
                color: "lightgray"
            }
            
            SpinBox {
                id: spinBox
                from: 0
                to: 100
                value: 50
                Layout.preferredWidth: 80
            }
            
            Rectangle {
                width: 1; height: parent.height
                color: "lightgray"
            }
            
            Slider {
                id: progressSlider
                value: 0.24
                Layout.fillWidth: true
            }
        }
        
        TextEdit {
            id: descriptionText
            text: "Input examples demonstration"
            readOnly: true
            Layout.fillWidth: true
            Layout.fillHeight: true
            wrapMode: TextEdit.Wrap
        }
    }
}
