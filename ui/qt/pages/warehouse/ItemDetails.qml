import QtQuick 2.15
import QtQuick.Controls 2.15

import "../../components"
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
            right: parent.right
        }

        text: title

        font.family: FontFamilies.family0
        font.weight: Font.Normal
        font.pixelSize : FontSizes.size4
    }

    Text {
        id: detailsLocationTitle
        height: 30
        anchors {
            top: detailsTitle.bottom
            left: parent.left
            topMargin: 10
            leftMargin: 20
            right: parent.right
        }

        text: "Locations"

        font.family: FontFamilies.family0
        font.weight: Font.Normal
        font.pixelSize : FontSizes.size3
    }

    ScrollView {
        id: assetRegionView
        clip: true
        height: 300
        anchors {
            top: detailsLocationTitle.bottom
            left: parent.left
            leftMargin: detailsLocationTitle.anchors.leftMargin + 20
            right: parent.right
            rightMargin: 20
        }
        ListView {
            anchors.fill: parent
            spacing: 10

            model: warehouseItemDetailsLocations
            delegate: WarehouseItemLocationCard {
                regionName: region
                constellationName: constellation
                systemName: system
                stationName: station
                itemQuantity: quantity
            }
        }
    }

    Text {
        id: detailsBuyOrdersTitle
        height: 30
        anchors {
            top: assetRegionView.bottom
            left: parent.left
            topMargin: 10
            leftMargin: 20
            right: parent.right
        }

        text: "Buy Orders"

        font.family: FontFamilies.family0
        font.weight: Font.Normal
        font.pixelSize : FontSizes.size3
    }
}