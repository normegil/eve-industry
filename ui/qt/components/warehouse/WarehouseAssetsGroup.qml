import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15
import QtGraphicalEffects 1.0

import "../../predefined" 1.0

Item {
    id: warehouseItemGroup

    property string name: "Minerals"
    property var assets: ListModel{}

    height: itemContainer.height + 40 + 2
    width: itemContainer.width + 200


    Rectangle {
        width: warehouseItemGroup.width
        height: 2
        border.width: 1
        border.color: Colors.grey7
    }

    Text {
        anchors {
            top: parent.top
            left: parent.left
            topMargin: 20
            leftMargin: 20
        }
        text: warehouseItemGroup.name
        color: Colors.grey3
        font.family: FontFamilies.family0
        font.pixelSize: FontSizes.size2

    }

    Item {
        id: itemContainer

        width: itemContainerLayout.cellWidth * 2
        height: itemContainerLayout.count / 2 * itemContainerLayout.cellHeight + 20
        anchors {
            top: parent.top
            right: parent.right
            rightMargin: 20
            topMargin: 20
        }

        GridView {
            id: itemContainerLayout

            anchors.fill: parent

            cellWidth: 400
            cellHeight: 80

            model: assets
            delegate: WarehouseItemCard {
                assetID: typeID
                itemName: name
                itemQuantity: quantity
                itemPrice: price
            }
        }
    }
}
