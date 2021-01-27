import QtQuick 2.15
import QtQuick.Controls 2.15

import "../components"
import "../predefined" 1.0

Item {
    anchors.fill: parent

    Item {
        id: stockScreenPart
        width: groupsView.width + 60

        anchors {
            top: parent.top
            bottom: parent.bottom
            left: parent.left
        }

        Text {
            id: stockTitle
            height: 50
            width: groupsView.width

            anchors {
                top: parent.top
                left: parent.left
                topMargin: 25
                leftMargin: 25
            }
            text: "Stock"

            font.family: FontFamilies.family0
            font.weight: Font.Normal
            font.pixelSize : FontSizes.size5
        }

        ScrollView {
            id: groupsView
            clip: true
            width: 1125
            anchors {
                top: stockTitle.bottom
                bottom: parent.bottom
                left: parent.left
                leftMargin: 50
            }

            ListView {
                id: groupListView
                anchors.fill: parent
                model: itemGroupsModel
                delegate: WarehouseItemGroup {
                    name: groupName
                    assets: groupAssets
                }
            }
        }
    }

    Rectangle {
        id: verticalSeparator
        width: 2
        anchors {
            top: parent.top
            bottom: parent.bottom
            left: stockScreenPart.right
        }
        border.width: 1
        border.color: Colors.grey7
    }
}