import QtQuick 2.15
import QtQuick.Controls 2.15

import "../predefined" 1.0

Item {
    id: warehouseItemBuyOrderRow

    property bool expiredOrder: False
    property string issuedDate: ""
    property string price: ""
    property string volumeRemaining: ""
    property string volumeTotal: ""

    property int regionID: -1
    property string regionName: "???"
    property int constellationID: -1
    property string constellationName: "???"
    property int systemID: -1
    property string systemName: "???"
    property int stationID: -1
    property string stationName: "???"

    property string separator: "<"
    property color separatorColor: Colors.grey4

    property string fontFamily: FontFamilies.family0
    property color itemColor: Colors.grey2
    property int itemSize: FontSizes.size2
    property int itemWeight: Font.Normal

    width: 715
    height: 60

    Rectangle {
        id: bgContainer
        anchors.fill: parent

        color: expiredOrder ? Colors.grey8 : Colors.grey9

        Text {
            id: issuedCell
            width: 150
            anchors {
                left: parent.left
                leftMargin: 15
                top: parent.top
                topMargin: 20
                bottom: parent.bottom
            }
            text: warehouseItemBuyOrderRow.issuedDate

            color: warehouseItemBuyOrderRow.itemColor
            font.family: warehouseItemBuyOrderRow.fontFamily
            font.weight: warehouseItemBuyOrderRow.itemWeight
            font.pixelSize: warehouseItemBuyOrderRow.itemSize
        }

        Item {
            id: locationCell
            width: 300
            anchors {
                left: issuedCell.right
                top: parent.top
                bottom: parent.bottom
            }

            property int vMargin: 13
            property int topMarginAdjuster: 3

            WarehouseItemLocationText {
                id: systemNameWarehouseItemLocationCard
                name: systemName
                locationType: LocationsType.system
                locationID: systemID
                fontSize : FontSizes.size3
                anchors {
                    left: parent.left
                    top: parent.top
                    topMargin: locationCell.vMargin
                }
            }

            Text {
                id: systemConstellationSeparator
                text: separator
                color: separatorColor

                font.family: fontFamily
                font.weight: Font.Normal
                font.pixelSize : FontSizes.size0

                verticalAlignment: Text.AlignVCenter

                anchors {
                    left: systemNameWarehouseItemLocationCard.right
                    leftMargin: 5
                    top: parent.top
                    topMargin: locationCell.vMargin + locationCell.topMarginAdjuster
                }
            }

            WarehouseItemLocationText {
                id: constellationNameWarehouseItemLocationCard
                name: constellationName
                locationType: LocationsType.constellation
                locationID: constellationID
                anchors {
                    left: systemConstellationSeparator.right
                    leftMargin: 5
                    top: parent.top
                    topMargin: locationCell.vMargin + locationCell.topMarginAdjuster
                }
            }

            Text {
                id: constellationRegionSeparator
                text: separator
                color: separatorColor

                font.family: fontFamily
                font.weight: Font.Normal
                font.pixelSize : FontSizes.size0

                verticalAlignment: Text.AlignVCenter

                anchors {
                    left: constellationNameWarehouseItemLocationCard.right
                    leftMargin: 5
                    top: parent.top
                    topMargin: locationCell.vMargin + locationCell.topMarginAdjuster
                }
            }

            WarehouseItemLocationText {
                name: regionName
                locationType: LocationsType.region
                locationID: regionID
                anchors {
                    left: constellationRegionSeparator.right
                    leftMargin: 5
                    top: parent.top
                    topMargin: locationCell.vMargin + locationCell.topMarginAdjuster
                }
            }

            WarehouseItemLocationText {
                name: stationName
                locationType: LocationsType.station
                locationID: stationID
                anchors {
                    left: parent.left
                    bottom: parent.bottom
                    bottomMargin: locationCell.vMargin
                }
            }
        }

        Item {
            id: priceVolCell
            anchors {
                left: locationCell.right
                top: parent.top
                bottom: parent.bottom
                right: parent.right
                rightMargin: 15
            }

            Text {
                id: priceText
                width: 80
                anchors {
                    right: parent.right
                    rightMargin: 20
                    top: parent.top
                    topMargin: 13
                }

                text: warehouseItemBuyOrderRow.price
                horizontalAlignment: Text.AlignRight

                color: Colors.grey2
                font.family: warehouseItemBuyOrderRow.fontFamily
                font.weight: warehouseItemBuyOrderRow.itemWeight
                font.pixelSize: FontSizes.size3
            }

            Text {
                text: "ISK/u"
                color: Colors.grey3
                font.family: warehouseItemBuyOrderRow.fontFamily
                font.pixelSize : FontSizes.size0

                verticalAlignment: Text.AlignBottom

                anchors {
                    left: volumeText.right
                    leftMargin: 4
                    top: parent.top
                    topMargin: 17
                }
            }

            Text {
                id: volumeText
                width: 80
                anchors {
                    right: parent.right
                    rightMargin: 20
                    bottom: parent.bottom
                    bottomMargin: 12
                }

                text: warehouseItemBuyOrderRow.volumeRemaining + " / " + warehouseItemBuyOrderRow.volumeTotal
                horizontalAlignment: Text.AlignRight

                color: Colors.grey2
                font.family: warehouseItemBuyOrderRow.fontFamily
                font.weight: warehouseItemBuyOrderRow.itemWeight
                font.pixelSize: FontSizes.size1
            }

            Text {
                text: "Units"
                color: Colors.grey3
                font.family: warehouseItemBuyOrderRow.fontFamily
                font.pixelSize : FontSizes.size0

                verticalAlignment: Text.AlignBottom

                anchors {
                    left: volumeText.right
                    leftMargin: 4
                    bottom: parent.bottom
                    bottomMargin: 13
                }
            }
        }
    }
}