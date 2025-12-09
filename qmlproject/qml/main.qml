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

    // NEW: Help menu with About entry
    menuBar: MenuBar {
        Menu {
            title: "Menu"
            Action {
                text: "Widgets Explorer"
                onTriggered: {
                    stackView.clear()
                    stackView.push("components/LoginPage.qml")
                }
            }
        }

        Menu {
            title: "Help"
            Action {
                text: "About"
                onTriggered: aboutDialog.open()
            }
        }
    }

    Dialog {
        id: aboutDialog
        title: "About QML Widget Explorer"
        modal: true
        standardButtons: Dialog.Ok
        x: (window.width - implicitWidth) / 2
        y: (window.height - implicitHeight) / 2

        Column {
            id: aboutContent
            anchors.fill: parent
            anchors.margins: 16
            spacing: 8

            Label {
                text: "Project: QML Widget Explorer\n"
                    + "Version: 1.0.0\n\n"
                    + "This demo shows Qt Quick (QML) widgets with a\n"
                    + "shared Python backend, for beginners.\n\n"
                    + "Login details to get started:\n"
                    + "  Username: admin\n"
                    + "  Password: 1234"
                wrapMode: Text.Wrap
            }
        }
    }


    Connections {
        target: backend
        function onLoginSuccess() {
            console.log("Main.qml: loginSuccess received, pushing SecondPage")
            stackView.push("components/SecondPage.qml")
        }
        function onGoToLogin() {
            console.log("Main.qml: goToLogin received, going back to LoginPage")
            stackView.clear()
            stackView.push("components/LoginPage.qml")
        }
    }
}
