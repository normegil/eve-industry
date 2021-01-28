import QtQuick 2.15
import QtQuick.Controls 2.15

import "../../predefined" 1.0

Item {
    anchors.fill: parent

    property string title: "Item Name"

    Text {
        id: detailsTitle
        height: 50
        anchors {
            top: parent.top
            left: parent.left
            topMargin: 30
            leftMargin: 25
            right: parent.right
        }

        text: warehouseItemDetails.name

        font.family: FontFamilies.family0
        font.weight: Font.Normal
        font.pixelSize : FontSizes.size4
    }

    Connections {
        target: warehouseItemDetails
    }

    Component.onCompleted: {

    }
}