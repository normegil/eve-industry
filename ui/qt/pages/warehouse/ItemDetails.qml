import QtQuick 2.15
import QtQuick.Controls 2.15

import "../../predefined" 1.0

Item {
    id: itemsDetail
    anchors.fill: parent

    property string title: "Item Name"

    Component.onCompleted: {
        warehouseItemDetails.reloadUI()
    }

    Connections {
        target: warehouseItemDetails

        function onNameChanged() {
            title = warehouseItemDetails.name
        }
    }

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

        text: title

        font.family: FontFamilies.family0
        font.weight: Font.Normal
        font.pixelSize : FontSizes.size4
    }

    ListView {
        id: assetRegionView
        height: 500
        anchors {
            top: detailsTitle.top
            left: parent.left
            leftMargin: 50
            right: parent.right
        }
        model: warehouseItemDetailsLocations
        delegate: Text {
            text: "Test"
        }
    }
}