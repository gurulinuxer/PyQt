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
        
        Calendar {
            id: calendar
            Layout.fillWidth: true
        }
        
        TextEdit {
            id: descriptionText
            text: "Display examples demonstration"
            readOnly: true
            Layout.fillWidth: true
            Layout.fillHeight: true
            wrapMode: TextEdit.Wrap
        }
    }
}
