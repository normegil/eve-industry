import QtQuick 2.15
import QtQuick.Controls 2.15

import "../components"
import "../predefined" 1.0

Rectangle {
    id: menu
    z: 10
    width: 75
    color: Colors.grey6

    property int iconsSize: FontSizes.size3
    property int buttonWidth: menu.width
    property int buttonHeight: menu.width - 10

    Connections {
        target: mainController
    }

    Connections {
        target: warehouseController
    }

    Button {
        id: warehouseBtn
        height: buttonHeight
        width: buttonWidth
        anchors {
            top: parent.top
        }

        flat: true
        onClicked: {
            warehouseController.refresh()
            mainController.changePage("warehouse")
        }

        icon.source:"../../resources/icons/warehouse-solid.svg"
        icon.width: iconsSize
        icon.height: iconsSize
        icon.color: warehouseBtn.down ? Colors.grey0 : Colors.grey2
        antialiasing: true
    }

    Rectangle {
        id: warehouseBorder
        width: buttonWidth
        anchors {
            top: warehouseBtn.bottom
            left: parent.left
        }
        height: 2
        border.width: 1
        border.color: Colors.grey7
    }

    Button {
        id: blueprintBtn
        height: buttonHeight
        width: buttonWidth
        anchors {
            top: warehouseBorder.bottom
        }

        flat: true
        onClicked: {
            warehouseController.refresh()
            mainController.changePage("blueprints")
        }

        icon.source:"../../resources/icons/file-contract-solid.svg"
        icon.width: iconsSize
        icon.height: iconsSize
        icon.color: blueprintBtn.down ? Colors.grey0 : Colors.grey2
        antialiasing: true
    }

    Rectangle {
        id: blueprintBorder
        width: buttonWidth
        anchors {
            top: blueprintBtn.bottom
            left: parent.left
        }
        height: 2
        border.width: 1
        border.color: Colors.grey7
    }

    Button {
        id: industryBtn
        height: buttonHeight
        width: buttonWidth
        anchors {
            top: blueprintBorder.bottom
        }

        flat: true
        onClicked: {
            mainController.changePage("industry")
        }

        icon.source:"../../resources/icons/industry-solid.svg"
        icon.width: iconsSize
        icon.height: iconsSize
        icon.color: industryBtn.down ? Colors.grey0 : Colors.grey2
        antialiasing: true
    }

    Rectangle {
        id: industryBorder
        width: buttonWidth
        anchors {
            top:industryBtn.bottom
            left: parent.left
        }
        height: 2
        border.width: 1
        border.color: Colors.grey7
    }

    Button {
        id: scienceBtn
        height: buttonHeight
        width: buttonWidth
        anchors {
            top: industryBorder.bottom
        }

        flat: true
        onClicked: {
            mainController.changePage("science")
        }

        icon.source:"../../resources/icons/flask-solid.svg"
        icon.width: iconsSize
        icon.height: iconsSize
        icon.color: scienceBtn.down ? Colors.grey0 : Colors.grey2
        antialiasing: true
    }

    Rectangle {
        id: scienceBorder
        width: buttonWidth
        anchors {
            top:scienceBtn.bottom
            left: parent.left
        }
        height: 2
        border.width: 1
        border.color: Colors.grey7
    }

    Button {
        id: marketBtn
        height: buttonHeight
        width: buttonWidth
        anchors {
            top: scienceBorder.bottom
        }

        flat: true
        onClicked: {
            mainController.changePage("market")
        }

        icon.source:"../../resources/icons/chart-line-solid.svg"
        icon.width: iconsSize
        icon.height: iconsSize
        icon.color: marketBtn.down ? Colors.grey0 : Colors.grey2
        antialiasing: true
    }

    Rectangle {
        id: marketBorder
        width: buttonWidth
        anchors {
            top:marketBtn.bottom
            left: parent.left
        }
        height: 2
        border.width: 1
        border.color: Colors.grey7
    }

    // -----------------------------------------------------------------------------

    Rectangle {
        id: settingsBorder
        width: buttonWidth
        anchors {
            bottom:settingsBtn.top
            left: parent.left
        }
        height: 2
        border.width: 1
        border.color: Colors.grey7
    }

    Button {
        id: settingsBtn
        height: buttonHeight
        width: buttonWidth
        anchors {
            bottom: parent.bottom
        }

        flat: true
        onClicked: {
            mainController.changePage("settings")
        }

        icon.source:"../../resources/icons/cogs-solid.svg"
        icon.width: iconsSize
        icon.height: iconsSize
        icon.color: settingsBtn.down ? Colors.grey0 : Colors.grey2
        antialiasing: true
    }
}