import QtQuick 2.15
import QtQuick.Controls 2.15

Page {
    id: loginPage

    Column {
        anchors.centerIn: parent
        spacing: 20

    // Header: logo + title + author + link
    Column {
        spacing: 8
        anchors.horizontalCenter: parent.horizontalCenter

        Image {
            id: qtLogo
            source: "assets/qt_logo.png"      // make sure this path exists
            fillMode: Image.PreserveAspectFit
            width: 260
            height: 80
        }

        Label {
            text: "Qt Educational Demo"
            font.pixelSize: 24
            font.bold: true
            horizontalAlignment: Text.AlignHCenter
        }

        Label {
            text: "by @gurulinuxer"
            font.pixelSize: 14
            color: "#555555"
            horizontalAlignment: Text.AlignHCenter
        }

        Label {
            text: "https://github.com/gurulinuxer/PyQt"
            font.pixelSize: 14
            color: "#2b6cb0"
            horizontalAlignment: Text.AlignHCenter
        }
    }

        // Small gap between header and form
        Item { width: 1; height: 16 }

        // Login form
        Column {
            spacing: 10
            anchors.horizontalCenter: parent.horizontalCenter

            TextField {
                id: user
                placeholderText: "Username"
                width: 300
            }

            TextField {
                id: pwd
                placeholderText: "Password"
                echoMode: TextInput.Password
                width: 300
            }

            Button {
                text: "Login"
                width: 300
                onClicked: {
                    console.log("Login clicked", user.text, pwd.text)
                    backend.login(user.text, pwd.text)
                }
            }

            Label {
                id: errorLabel
                color: "red"
            }

            Label {
                text: "Demo credentials →  Username: admin   Password: 1234"
                font.pixelSize: 12
                color: "#555555"
            }
        }
    }

    Connections {
        target: backend
        function onLoginFailed(message) {
            errorLabel.text = message
            console.log("Login failed:", message)
        }
    }
}
