import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15
import QtGraphicalEffects 1.0

import "../predefined" 1.0

Rectangle {
    id: warehouseItemGroup
    width: 790
    color: "#00000000"

    property string text: "Minerals"

    Rectangle {
        width: warehouseItemGroup.width
        height: 2
        border.width: 1
        border.color: Colors.grey7
    }

    Text {
        text: warehouseItemGroup.text
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
        width: 500

        anchors {
            top: parent.top
            bottom: parent.bottom
            right: parent.right
            rightMargin: 20
            topMargin: 20
            bottomMargin: 20
        }

        GridLayout {
            id: itemContainerLayout
            anchors.fill: parent.fill

            columns: 2
            columnSpacing: 20
            rowSpacing: itemContainerLayout.columnSpacing

            WarehouseItemCard {}
            WarehouseItemCard {}
            WarehouseItemCard {}
            WarehouseItemCard {}
            WarehouseItemCard {}
        }
    }
}

/*##^##
Designer {
    D{i:0;autoSize:true;formeditorZoom:1.3300000429153442;height:480;width:640}
}
##^##*/
