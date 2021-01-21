import QtQuick 2.13
import QtQuick.Window 2.13

import "components"
import "predefined" 1.0

Window {
    width: 640
    height: 480
    visible: true
    title: qsTr("Hello World")

    color: Colors.grey8

    WarehouseItemCard {
        id: warehouseItemCard
        x: 115
        y: 98
    }
}
