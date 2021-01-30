import QtQuick 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.0

import "../../components"
import "../../predefined" 1.0

Item {
    anchors.fill: parent

    property color titlesColor: Colors.grey3

    property string fontFamily: FontFamilies.family0
    property color buyOrderHeaderColor: Colors.grey4
    property int buyOrderHeaderSize: FontSizes.size2
    property int buyOrderHeaderWeight: Font.Normal

    Component.onCompleted: {
        warehouseAssetDetails.reloadUI()
    }
    Connections {
        target: warehouseAssetDetails
        function onNameChanged() {
            detailsTitle.text = warehouseAssetDetails.name
        }
    }

    Text {
        id: detailsTitle

        anchors {
            top: parent.top
            left: parent.left
            topMargin: 40
            right: parent.right
        }

        text: ""
        color: Colors.grey2
        font.family: FontFamilies.family0
        font.weight: Font.Normal
        font.pixelSize : FontSizes.size4
    }

    AssetStatistics {
        id: assetStatisticsID

        height: 100
        anchors {
            top: detailsTitle.bottom
            topMargin: 15
            left: parent.left
            right: parent.right
        }
    }

    AssetLocations {
        id: assetLocationsID

        height: 350
        anchors {
            top: assetStatisticsID.bottom
            topMargin: 15
            left: parent.left
            right: parent.right
        }
    }

    AssetBuyOrders {
        anchors {
            top: assetLocationsID.bottom
            topMargin: 15
            left: parent.left
            right: parent.right
            bottom: parent.bottom
        }
    }
}