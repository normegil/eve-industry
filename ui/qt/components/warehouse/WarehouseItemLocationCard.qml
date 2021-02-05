import QtQuick 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.0

import "../controls"
import "../../predefined" 1.0

Item {
    id: warehouseItemLocationCard

    property int regionID: -1
    property string regionName: "???"
    property int constellationID: -1
    property string constellationName: "???"
    property int systemID: -1
    property string systemName: "???"
    property int stationID: -1
    property string stationName: "???"

    property string itemQuantity: "0"

    property string separator: "<"
    property color separatorColor: Colors.grey4

    property string fontFamily: FontFamilies.family0

    height: 45
    width: 655

    Rectangle {
        id: backgroundContainer
        anchors.fill: parent
        z: 10

        color: Colors.grey9

        ItemLocationText {
            id: systemNameWarehouseItemLocationCard

            anchors {
                left: parent.left
                leftMargin: 10
                top: parent.top
                topMargin: 5
            }

            name: systemName
            locationType: LocationsType.system
            locationID: systemID
            fontSize : FontSizes.size3
        }

        Text {
            id: systemConstellationSeparator

            anchors {
                left: systemNameWarehouseItemLocationCard.right
                leftMargin: 5
                top: parent.top
                topMargin: 8
            }

            text: separator
            color: separatorColor
            verticalAlignment: Text.AlignVCenter
            font.family: fontFamily
            font.weight: Font.Normal
            font.pixelSize : FontSizes.size0
        }

        ItemLocationText {
            id: constellationNameWarehouseItemLocationCard

            anchors {
                left: systemConstellationSeparator.right
                leftMargin: 5
                top: parent.top
                topMargin: 8
            }

            name: constellationName
            locationType: LocationsType.constellation
            locationID: constellationID
        }

        Text {
            id: constellationRegionSeparator

            anchors {
                left: constellationNameWarehouseItemLocationCard.right
                leftMargin: 5
                top: parent.top
                topMargin: 8
            }

            text: separator
            color: separatorColor
            verticalAlignment: Text.AlignVCenter
            font.family: fontFamily
            font.weight: Font.Normal
            font.pixelSize : FontSizes.size0
        }

        ItemLocationText {
            anchors {
                left: constellationRegionSeparator.right
                leftMargin: 5
                top: parent.top
                topMargin: 8
            }
            name: regionName
            locationType: LocationsType.region
            locationID: regionID
        }

        ItemLocationText {
            anchors {
                left: parent.left
                leftMargin: 10
                bottom: parent.bottom
                bottomMargin: 5
            }
            name: stationName
            locationType: LocationsType.station
            locationID: stationID
        }

        Text {
            anchors {
                right: parent.right
                rightMargin: 10
                bottom: parent.bottom
                bottomMargin: 11
            }
            text: itemQuantity
            color: Colors.grey1
            verticalAlignment: Text.AlignVCenter
            font.family: fontFamily
            font.weight: Font.Normal
            font.pixelSize : FontSizes.size5
        }
    }

    DropShadow {
        anchors.fill: parent
        source: backgroundContainer
        horizontalOffset: 2
        verticalOffset: 2
        radius: 3
        color: Colors.grey6
        z: 0
    }
}
