import QtQuick 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.0

import "../../components/blueprints"
import "../../predefined" 1.0

Item {
    anchors.fill: parent

    Text {
        id: title

        height: 40
        anchors {
            top: parent.top
            left: parent.left
            leftMargin: 25
        }

        text: "Blueprints"
        color: Colors.grey3
        font.family: FontFamilies.family0
        font.pixelSize : FontSizes.size5
    }

    ScrollView {
        clip: true
        anchors {
            top: title.bottom
            topMargin: 10
            bottom: parent.bottom
            left: parent.left
            right: parent.right
        }

        ListView {
            anchors.fill: parent
            model: blueprintList
            delegate: BlueprintTypeSection {
                title: name
                individuals: locations
            }
        }
    }
}