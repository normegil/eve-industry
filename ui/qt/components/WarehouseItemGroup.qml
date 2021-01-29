import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15
import QtGraphicalEffects 1.0

import "../predefined" 1.0

Rectangle {
    id: warehouseItemGroup
    height: itemContainer.height + 40 + 2
    width: itemContainer.width + 300
    color: "#00000000"

    property string name: "Minerals"
    property var assets: ListModel{}

    Rectangle {
        width: warehouseItemGroup.width
        height: 2
        border.width: 1
        border.color: Colors.grey7
    }

    Text {
        text: warehouseItemGroup.name
        font.family: FontFamilies.family0
        font.pixelSize: FontSizes.size2
        color: Colors.grey3

        anchors {
            top: parent.top
            left: parent.left
            topMargin: 20
            leftMargin: 20
        }
    }

    Rectangle {
        id: itemContainer
        width: itemContainerLayout.cellWidth * 2
        height: itemContainerLayout.count / 2 * itemContainerLayout.cellHeight + 20
        color: "#00000000"

        anchors {
            top: parent.top
            right: parent.right
            rightMargin: 20
            topMargin: 20
        }

        GridView {
            id: itemContainerLayout
            cellWidth: 400
            cellHeight: 80
            anchors.fill: parent

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

/*##^##
Designer {
    D{i:0;autoSize:true;formeditorZoom:1.3300000429153442;height:480;width:640}
}
##^##*/
