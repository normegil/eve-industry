import QtQuick 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.0

import "../../components"
import "../../predefined" 1.0

Item {
    id: itemsDetail
    anchors.fill: parent

    property color titlesColor: Colors.grey3

    property string fontFamily: FontFamilies.family0

    property color buyOrderHeaderColor: Colors.grey4
    property int buyOrderHeaderSize: FontSizes.size2
    property int buyOrderHeaderWeight: Font.Normal
    property color shadowColor: Colors.grey6

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

    Text {
        id: detailsLocationTitle
        anchors {
            top: detailsTitle.bottom
            left: parent.left
            topMargin: 10
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
        height: 300
        anchors {
            top: detailsLocationTitle.bottom
            topMargin: 5
            left: parent.left
            right: parent.right
            rightMargin: 15
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

    Text {
        id: detailsBuyOrdersTitle
        height: 22
        anchors {
            top: assetRegionView.bottom
            left: parent.left
            topMargin: 10
            leftMargin: 20
            right: parent.right
        }

        text: "Buy Orders"
        color: titlesColor

        font.family: FontFamilies.family0
        font.weight: Font.Normal
        font.pixelSize : FontSizes.size2
    }

    Rectangle {
        id: detailsBuyOrdersContainer
        z: 10

        color: Colors.transparent

        anchors {
            top: detailsBuyOrdersTitle.bottom
            left: parent.left
            leftMargin: assetRegionView.anchors.leftMargin
            right: parent.right
            rightMargin: 20
            bottom: parent.bottom
            bottomMargin: 20
        }

        Rectangle {
            id: detailsBuyOrdersViewHeader
            color: Colors.grey9
            anchors {
                top: parent.top
                left: parent.left
                right: parent.right
            }
            height: 30

            Text {
                id: issuedHeader
                width: 150
                anchors {
                    left: parent.left
                    leftMargin: 15
                    top: parent.top
                    topMargin: 8
                    bottom: parent.bottom
                }
                text: "Issued"
                color: itemsDetail.buyOrderHeaderColor
                font.family: itemsDetail.fontFamily
                font.weight: itemsDetail.buyOrderHeaderWeight
                font.pixelSize: itemsDetail.buyOrderHeaderSize
            }
            Text {
                id: locationHeader
                width: 300
                anchors {
                    left: issuedHeader.right
                    top: parent.top
                    topMargin: 8
                    bottom: parent.bottom
                }
                text: "Location"
                color: itemsDetail.buyOrderHeaderColor
                font.family: itemsDetail.fontFamily
                font.weight: itemsDetail.buyOrderHeaderWeight
                font.pixelSize: itemsDetail.buyOrderHeaderSize
            }
            Text {
                anchors {
                    left: locationHeader.right
                    top: parent.top
                    topMargin: 8
                    bottom: parent.bottom
                    right: parent.right
                    rightMargin: 15
                }

                text: "Price & Volume"

                horizontalAlignment: Text.AlignRight
                color: itemsDetail.buyOrderHeaderColor
                font.family: itemsDetail.fontFamily
                font.weight: itemsDetail.buyOrderHeaderWeight
                font.pixelSize: itemsDetail.buyOrderHeaderSize
            }
        }
        Rectangle {
            id: detailsBuyOrdersViewHeaderSeparator
            anchors {
                top: detailsBuyOrdersViewHeader.bottom
                left: parent.left
                right: parent.right
            }
            width: detailsBuyOrdersViewHeader.width
            height: 2
            border.width: 1
            border.color: Colors.grey7
        }
        ScrollView {
            id: detailsBuyOrdersView
            clip: true
            anchors {
                top: detailsBuyOrdersViewHeaderSeparator.bottom
                left: parent.left
                right: parent.right
                bottom: parent.bottom
            }
            ListView {
                anchors.fill: parent

                model: warehouseAssetDetailsBuyOrders
                delegate: WarehouseItemBuyOrderRow {
                    expiredOrder: expired
                    issuedDate: issued
                    price: pricePerUnit
                    volumeRemaining: volumeRem
                    volumeTotal: volumeTot

                    regionName: region
                    regionID: regionIdentifier
                    constellationName: constellation
                    constellationID: constellationIdentifier
                    systemName: system
                    systemID: systemIdentifier
                    stationName: station
                    stationID: stationIdentifier
                }
            }
        }
    }

    DropShadow {
        anchors {
            top: detailsBuyOrdersTitle.bottom
            left: parent.left
            leftMargin: assetRegionView.anchors.leftMargin
            right: parent.right
            rightMargin: 20
            bottom: parent.bottom
            bottomMargin: 20
        }
        source: detailsBuyOrdersContainer
        horizontalOffset: 2
        verticalOffset: 2
        radius: 3
        color: shadowColor
        z: 0
    }
}