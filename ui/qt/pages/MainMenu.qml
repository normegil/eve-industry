import QtQuick 2.15
import QtQuick.Controls 2.15

import "../components"
import "../predefined" 1.0

Rectangle {
    id: menu
    z: 10
    width: 75
    color: Colors.grey6

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

        contentItem: Text {
            text: "" // LA Warehouse
            color: warehouseBtn.down ? Colors.grey0 : Colors.grey2
            font.family: FontFamilies.icons0
            font.pixelSize: FontSizes.size6
            verticalAlignment: Text.AlignVCenter
            horizontalAlignment: Text.AlignHCenter
        }
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
        id: industryBtn
        height: buttonHeight
        width: buttonWidth
        anchors {
            top: warehouseBorder.bottom
        }

        flat: true
        onClicked: {
            mainController.changePage("industry")
        }

        contentItem: Text {
            text: "" // LA Industry
            color: industryBtn.down ? Colors.grey0 : Colors.grey2
            font.family: FontFamilies.icons0
            font.pixelSize: FontSizes.size6
            verticalAlignment: Text.AlignVCenter
            horizontalAlignment: Text.AlignHCenter
        }
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

        contentItem: Text {
            text: "" // LA Flask
            color: scienceBtn.down ? Colors.grey0 : Colors.grey2
            font.family: FontFamilies.icons0
            font.pixelSize: FontSizes.size6
            verticalAlignment: Text.AlignVCenter
            horizontalAlignment: Text.AlignHCenter
        }
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

        contentItem: Text {
            text: "" // LA Chart Area
            color: marketBtn.down ? Colors.grey0 : Colors.grey2
            font.family: FontFamilies.icons0
            font.pixelSize: FontSizes.size6
            verticalAlignment: Text.AlignVCenter
            horizontalAlignment: Text.AlignHCenter
        }
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

        contentItem: Text {
            text: "" // LA Cog
            color: settingsBtn.down ? Colors.grey0 : Colors.grey2
            font.family: FontFamilies.icons0
            font.pixelSize: FontSizes.size6
            verticalAlignment: Text.AlignVCenter
            horizontalAlignment: Text.AlignHCenter
        }
    }
}