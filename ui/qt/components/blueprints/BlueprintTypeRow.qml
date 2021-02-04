import QtQuick 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.0

import "../../predefined" 1.0

Item {
    property string title
    property var locations

    height: titleIdentifier.height + locationList.count * locationBlueprintBg.height

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
        font.pixelSize : FontSizes.size3
    }

    ListView {
        id: locationList
        anchors {
            top: titleIdentifier.bottom
            left: parent.left
        }
        model: locations
        delegate: Rectangle {
            id: locationBlueprintBg
            color: Colors.grey9
            height: 45
        }
    }
}