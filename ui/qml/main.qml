import QtQuick 2.15
import QtQuick.Window 2.13

import "components"
import "predefined" 1.0

Window {
    width: 1200
    height: 600
    visible: true
    title: qsTr("Hello World")

    color: Colors.grey8

    WarehouseItemGroup {
        id: warehouseItemCard
        x: 50
        y: 50
    }
}
