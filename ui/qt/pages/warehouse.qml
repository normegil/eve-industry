import QtQuick 2.15

import "../components"

Item {
    WarehouseWatchList {
        x: 10
        y: 10
    }

    Connections {
        target: backend
    }
}