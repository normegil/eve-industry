import QtQuick 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.0

import "../../predefined" 1.0

Item {
    property string title
    property var individuals: ListModel{}

    height: titleIdentifier.height + locationList.height + 20
    width: 1300

    Text {
        id: titleIdentifier
        anchors {
            left: parent.left
            leftMargin: 50
        }
        text: title
        color: Colors.grey3
        font.family: FontFamilies.family0
        font.weight: Font.Normal
        font.pixelSize : FontSizes.size2
    }

    ListView {
        id: locationList
        height: locationList.count * 50
        spacing: 5
        anchors {
            top: titleIdentifier.bottom
            topMargin: 5
            left: parent.left
        }
        model: locations
        delegate: BlueprintTypeRow {
            runLeft: runs
            timeEfficiency: time
            materialEfficiency: mats
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