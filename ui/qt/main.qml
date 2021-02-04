import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Window 2.15
import QtGraphicalEffects 1.0

import "components"
import "pages"
import "predefined" 1.0

Window {
    visibility: Window.Maximized
    visible: true
    title: qsTr("Eve Industry")

    minimumHeight: 500
    minimumWidth: 1300

    color: Colors.grey8

    MainMenu {
        id: leftMenu
        z: 10
        anchors {
            top: parent.top
            bottom: parent.bottom
            left: parent.left
        }
    }

    DropShadow {
        z: 0
        width: 75
        anchors {
            top: parent.top
            bottom: parent.bottom
            left: parent.left
        }
        source: leftMenu
        horizontalOffset: 1
        radius: 5
        color: Colors.grey7
    }

    Loader {
        id: mainLoader
        property int margin: 20
        anchors {
            top: parent.top
            bottom: parent.bottom
            left: leftMenu.right
            right: parent.right
            topMargin: margin
            bottomMargin: margin
            leftMargin: margin
            rightMargin: margin
        }
    }

    Component.onCompleted: {
        mainLoader.source = mainController.pageSource
    }

    Connections {
        target: mainController

        function onPageSourceChanged() {
            mainLoader.source = mainController.pageSource
        }
    }
}
