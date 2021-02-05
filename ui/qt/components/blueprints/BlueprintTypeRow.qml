import QtQuick 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.0

import "../control" 1.0
import "../../predefined" 1.0

Item {

    implicitHeight: 45
    implicitWidth: 380

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

    Rectangle {
        id: mainBackground
        anchors.fill: parent
        color: Colors.grey9

        ItemLocationText {
            id: systemNameBlueprintTypeRow

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
                left: systemNameBlueprintTypeRow.right
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
            id: constellationNameBlueprintTypeRow

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
                left: constellationNameBlueprintTypeRow.right
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
    }
}