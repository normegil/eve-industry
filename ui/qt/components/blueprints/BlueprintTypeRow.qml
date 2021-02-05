import QtQuick 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.0

import "../controls"
import "../../predefined" 1.0

Item {

    implicitHeight: 45
    implicitWidth: 800

    property int runLeft: 0
    property int timeEfficiency: 0
    property int materialEfficiency: 0

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

        Item {
            id: locationColumn

            width: 400
            anchors {
                top: parent.top
                bottom: parent.bottom
                left: parent.left
            }

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
                font.family: FontFamilies.family0
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
                font.family: FontFamilies.family0
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

        Item {
            id: runsColumn
            width: 100
            anchors {
                top: parent.top
                bottom: parent.bottom
                left: locationColumn.right
            }

            Text {
                id: runsNbText
                anchors {
                    top: parent.top
                    right: parent.right
                    rightMargin: 30
                    topMargin: 8
                }
                text: runLeft
                horizontalAlignment: Text.AlignRight
                verticalAlignment: Text.AlignBottom
                color: Colors.grey1
                font.family: FontFamilies.family0
                font.pixelSize : FontSizes.size1
            }

            Text {
                anchors {
                    left: runsNbText.right
                    leftMargin: 4
                    top: parent.top
                    topMargin: 10
                }
                text: "runs left"
                verticalAlignment: Text.AlignBottom
                color: Colors.grey4
                font.family: FontFamilies.family0
                font.pixelSize : FontSizes.size0
            }
        }

        Item {
            id: efficiencyColumn
            width: 100
            anchors {
                top: parent.top
                bottom: parent.bottom
                left: runsColumn.right
            }

            Text {
                id: materialEfficiencyText
                anchors {
                    top: parent.top
                    right: parent.right
                    rightMargin: 30
                    topMargin: 8
                }
                text: "-" + materialEfficiency + " %"
                horizontalAlignment: Text.AlignRight
                verticalAlignment: Text.AlignBottom
                color: Colors.grey1
                font.family: FontFamilies.family0
                font.pixelSize : FontSizes.size1
            }

            Text {
                anchors {
                    left: materialEfficiencyText.right
                    leftMargin: 4
                    top: parent.top
                    topMargin: 10
                }
                text: "materials"
                verticalAlignment: Text.AlignBottom
                color: Colors.grey4
                font.family: FontFamilies.family0
                font.pixelSize : FontSizes.size0
            }

            Text {
                id: timeEfficiencyText
                anchors {
                    bottom: parent.bottom
                    bottomMargin: 8
                    right: parent.right
                    rightMargin: 30
                }
                text: "-" + timeEfficiency + " %"
                horizontalAlignment: Text.AlignRight
                verticalAlignment: Text.AlignBottom
                color: Colors.grey1
                font.family: FontFamilies.family0
                font.pixelSize : FontSizes.size1
            }

            Text {
                anchors {
                    left: timeEfficiencyText.right
                    leftMargin: 4
                    bottom: parent.bottom
                    bottomMargin: 8
                }
                text: "time"
                verticalAlignment: Text.AlignBottom
                color: Colors.grey4
                font.family: FontFamilies.family0
                font.pixelSize : FontSizes.size0
            }
        }
    }
}