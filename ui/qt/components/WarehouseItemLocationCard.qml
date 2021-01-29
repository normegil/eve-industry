import QtQuick 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.0

import "../predefined" 1.0

Item {
    id: warehouseItemLocationCard

    property string regionName: "???"
    property string constellationName: "???"
    property string systemName: "???"
    property string stationName: "???"

    property string itemQuantity: "0"
    property color itemQuantityColor: Colors.grey1

    property string separator: "<"
    property color separatorColor: Colors.grey4

    property color shadowColor: Colors.grey6

    property string fontFamily: FontFamilies.family0

    property color bgMainColor: Colors.grey9

    height: 45
    width: 640
    anchors {
        left: parent.left
    }

    Rectangle {
        id: bgContainer
        anchors.fill: parent
        z: 10

        color: warehouseItemLocationCard.bgMainColor

        WarehouseItemLocationText {
            id: systemNameWarehouseItemLocationCard
            name: systemName
            fontSize : FontSizes.size3
            anchors {
                left: parent.left
                leftMargin: 10
                top: parent.top
                topMargin: 5
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
                topMargin: 8
            }
        }

        WarehouseItemLocationText {
            id: constellationNameWarehouseItemLocationCard
            name: constellationName
            anchors {
                left: systemConstellationSeparator.right
                leftMargin: 5
                top: parent.top
                topMargin: 8
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
                topMargin: 8
            }
        }

        WarehouseItemLocationText {
            name: regionName
            anchors {
                left: constellationRegionSeparator.right
                leftMargin: 5
                top: parent.top
                topMargin: 8
            }
        }

        WarehouseItemLocationText {
            name: stationName
            anchors {
                left: parent.left
                leftMargin: 10
                bottom: parent.bottom
                bottomMargin: 5
            }
        }

        Text {
            text: itemQuantity
            color: itemQuantityColor

            font.family: fontFamily
            font.weight: Font.Normal
            font.pixelSize : FontSizes.size5

            verticalAlignment: Text.AlignVCenter

            anchors {
                right: parent.right
                rightMargin: 10
                bottom: parent.bottom
                bottomMargin: 11
            }
        }
    }

    DropShadow {
        anchors.fill: parent
        source: bgContainer
        horizontalOffset: 1
        verticalOffset: 1
        radius: 3
        color: shadowColor
        z: 0
    }
}

/*##^##
Designer {
    D{i:0;autoSize:true;formeditorZoom:1.3300000429153442;height:480;width:640}
}
##^##*/
