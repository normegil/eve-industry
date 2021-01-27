import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Window 2.15

import "components"
import "predefined" 1.0

Window {
    visibility: Window.Maximized
    visible: true
    title: qsTr("Eve Industry")

    color: Colors.grey8

    Loader {
        anchors.fill: parent
        source: "pages/warehouse.qml"
    }
}
