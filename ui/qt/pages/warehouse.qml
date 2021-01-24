import QtQuick 2.15

import "../components"

Item {
    ListView {
        x: 10
        y: 10
        model: itemGroupsModel
        delegate: WarehouseItemGroup {
            name: groupName
        }
    }
}