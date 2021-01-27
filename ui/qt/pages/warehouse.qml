import QtQuick 2.15

import "../components"
import "../predefined" 1.0

Item {
    anchors.fill: parent

    Text {
        id: stockTitle
        height: 50
        width: WarehouseItemGroup.width

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

    ListView {
        id: groups
        anchors {
            top: stockTitle.bottom
            left: parent.left
            leftMargin: 50
            right: parent.right
            bottom: parent.bottom
        }
        model: itemGroupsModel
        delegate: WarehouseItemGroup {
            name: groupName
            assets: groupAssets
        }
    }
}