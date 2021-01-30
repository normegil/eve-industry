import QtQuick 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.0

import "../../components/warehouse"
import "../../predefined" 1.0

Item {
    Text {
        id: detailsBuyOrdersTitle
        height: 22
        anchors {
            top: parent.top
            left: parent.left
            leftMargin: 20
            right: parent.right
        }

        text: "Buy Orders"
        color: titlesColor

        font.family: FontFamilies.family0
        font.weight: Font.Normal
        font.pixelSize : FontSizes.size2
    }

    Item {
        id: detailsBuyOrdersContainer
        z: 10

        anchors {
            top: detailsBuyOrdersTitle.bottom
            left: parent.left
            right: parent.right
            rightMargin: 40
            bottom: parent.bottom
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
                color: buyOrderHeaderColor
                font.family: fontFamily
                font.weight: buyOrderHeaderWeight
                font.pixelSize: buyOrderHeaderSize
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
                color: buyOrderHeaderColor
                font.family: fontFamily
                font.weight: buyOrderHeaderWeight
                font.pixelSize: buyOrderHeaderSize
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
                color: buyOrderHeaderColor
                font.family: fontFamily
                font.weight: buyOrderHeaderWeight
                font.pixelSize: buyOrderHeaderSize
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
            right: parent.right
            rightMargin: 20
            bottom: parent.bottom
            bottomMargin: 20
        }
        source: detailsBuyOrdersContainer
        horizontalOffset: 2
        verticalOffset: 2
        radius: 3
        color: Colors.grey6
        z: 0
    }
}