import QtQuick 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.0

import "../../components/warehouse"
import "../../predefined" 1.0

Item {
    Text {
        id: detailsLocationTitle

        anchors {
            top: parent.top
            left: parent.left
            leftMargin: 20
            right: parent.right
        }

        text: "Locations"
        color: titlesColor
        font.family: FontFamilies.family0
        font.weight: Font.Normal
        font.pixelSize : FontSizes.size2
    }

    ScrollView {
        id: assetRegionView
        clip: true

        anchors {
            top: detailsLocationTitle.bottom
            topMargin: 5
            left: parent.left
            right: parent.right
            bottom: parent.bottom
        }

        ListView {
            anchors.fill: parent
            spacing: 10

            model: warehouseAssetDetailsLocations
            delegate: WarehouseItemLocationCard {
                regionName: region
                regionID: regionIdentifier
                constellationName: constellation
                constellationID: constellationIdentifier
                systemName: system
                systemID: systemIdentifier
                stationName: station
                stationID: stationIdentifier
                itemQuantity: quantity
            }
        }
    }
}