import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Window 2.15

import "components"
import "predefined" 1.0

Window {
    visibility: Window.Maximized
    visible: true
    title: qsTr("Eve Industry")

    minimumHeight: 300
    minimumWidth: 1300

    color: Colors.grey8

    Loader {
        property int margin: 20
        anchors {
            top: parent.top
            bottom: parent.bottom
            left: parent.left
            right: parent.right
            topMargin: margin
            bottomMargin: margin
            leftMargin: margin
            rightMargin: margin
        }
        source: "pages/warehouse/Warehouse.qml"
    }
}
