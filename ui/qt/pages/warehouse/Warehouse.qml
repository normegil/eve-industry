import QtQuick 2.15
import QtQuick.Controls 2.15

import "../../components"
import "../../predefined" 1.0

Item {
    anchors.fill: parent
    Item {
        id: assetsGroups
        width: 1050
        anchors {
            top: parent.top
            bottom: parent.bottom
            left: parent.left
        }
        AssetsGroups {}
    }

    Item {
        id: details
        anchors {
            top: parent.top
            bottom: parent.bottom
            left: assetsGroups.right
            right: parent.right
        }

        Loader {
            anchors.fill: parent
            source: "./ItemDetails.qml"
        }
    }
}