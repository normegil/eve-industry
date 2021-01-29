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
            font.pixelSize : FontSizes.size6
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

    Item {
        id: detailsScreenPart
        anchors {
            top: parent.top
            bottom: parent.bottom
            left: stockScreenPart.right
            right: parent.right
        }

        Loader {
            anchors.fill: parent
            source: "warehouse/ItemDetails.qml"
        }
    }
}