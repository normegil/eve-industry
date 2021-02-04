import QtQuick 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.0

import "../../components"
import "../../predefined" 1.0

Item {
    anchors.fill: parent

    Connections {
        target: warehouseAssetsBuyList
    }

    Text {
        id: title

        anchors {
            top: parent.top
            left: parent.left
            topMargin: 40
            right: parent.right
        }

        text: "Buy List"
        color: Colors.grey2
        font.family: FontFamilies.family0
        font.weight: Font.Normal
        font.pixelSize : FontSizes.size4
    }

    Rectangle {
        z: 0
        id: buyListContainer
        color: Colors.grey9

        anchors {
            top: title.bottom
            topMargin: 10
            left: parent.left
            right: parent.right
            bottom: parent.bottom
        }

        ScrollView {
            clip: true
            anchors.fill: parent

            TextEdit {
                anchors {
                    top: parent.top
                    bottom: parent.bottom
                    left: parent.left
                    right: parent.right

                    topMargin: 10
                    bottomMargin: 10
                    leftMargin: 10
                    rightMargin: 10
                }

                text: warehouseAssetsBuyList.buylist
                color: Colors.grey1
                font.family: FontFamilies.family0
                font.weight: Font.Normal
                font.pixelSize : FontSizes.size3
                readOnly: true
                selectByMouse: true
            }
        }
    }

    InnerShadow {
        z: 5
        anchors.fill: buyListContainer
        source: buyListContainer
        samples: 4
        horizontalOffset: 3
        verticalOffset: 3
        radius: 5
        color: Colors.grey7
    }
}