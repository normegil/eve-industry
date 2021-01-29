import QtQuick 2.15
import QtQuick.Controls 2.15

import "../../components/warehouse"
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

        text: "Stock"
        color: Colors.grey3
        font.family: FontFamilies.family0
        font.weight: Font.Normal
        font.pixelSize : FontSizes.size5
    }

    ScrollView {
        clip: true
        anchors {
            top: title.bottom
            bottom: parent.bottom
            left: parent.left
            right: parent.right
        }

        ListView {
            anchors.fill: parent
            model: warehouseAssetsGroups
            delegate: WarehouseAssetsGroup {
                name: groupName
                assets: groupAssets
            }
        }
    }
}