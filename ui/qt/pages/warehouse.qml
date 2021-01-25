import QtQuick 2.15

import "../components"

Item {
    anchors.fill: parent

    ListView {
        anchors.fill: parent
        model: itemGroupsModel
        delegate: WarehouseItemGroup {
            name: groupName
            assets: groupAssets
        }
    }
}