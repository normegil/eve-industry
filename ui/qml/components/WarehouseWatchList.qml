import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15
import QtGraphicalEffects 1.0

import "../predefined" 1.0

Rectangle {
    id: warehouseWatchList
    anchors.fill: parent.fill

    ColumnLayout {
        anchors.fill: parent.fill
        spacing: 60

        WarehouseItemGroup {}
        WarehouseItemGroup {}
    }
}

/*##^##
Designer {
    D{i:0;autoSize:true;formeditorZoom:1.3300000429153442;height:480;width:640}
}
##^##*/
