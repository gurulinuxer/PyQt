import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Window 2.15

ApplicationWindow {
    id: window
    width: 919
    height: 674
    title: "QML Widget Explorer"
    visible: true

    StackView {
        id: stackView
        anchors.fill: parent
        initialItem: "components/LoginPage.qml"
    }

    Connections {
        target: backend

        function onLoginSuccess() {
            console.log("Main.qml: loginSuccess received, pushing SecondPage")
            stackView.push("components/SecondPage.qml")
        }
    }
}
