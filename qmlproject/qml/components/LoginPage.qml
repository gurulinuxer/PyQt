import QtQuick 2.15
import QtQuick.Controls 2.15

Page {
    id: loginPage

    Column {
        anchors.centerIn: parent
        spacing: 10

        TextField {
            id: user
            placeholderText: "Username"
        }

        TextField {
            id: pwd
            placeholderText: "Password"
            echoMode: TextInput.Password
        }

        Button {
            text: "Login"
            onClicked: {
                console.log("Login clicked", user.text, pwd.text)
                backend.login(user.text, pwd.text)
            }
        }

        Label {
            id: errorLabel
            color: "red"
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
