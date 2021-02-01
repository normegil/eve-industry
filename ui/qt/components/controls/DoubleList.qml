import QtQuick 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.0

import "../../predefined" 1.0

Item {
    property string titleLeft: ""
    property string titleRight: ""

    property var listModelLeft: ListModel{}
    property var listModelRight: ListModel{}

    ClickableList {
        title: titleLeft
        listModel: listModelLeft
        anchors {
            top: parent.top
            left: parent.left
            bottom: parent.bottom
            right: parent.horizontalCenter
            rightMargin: 5
        }

        onSelectedItem: function(id) {
            listModelLeft.removeItem(id)
            listModelRight.addItem(id)
        }
    }

    ClickableList {
        title: titleRight
        listModel: listModelRight
        anchors {
            top: parent.top
            left: parent.horizontalCenter
            leftMargin: 5
            bottom: parent.bottom
            right: parent.right
        }

        onSelectedItem: function(id) {
            listModelRight.removeItem(id)
            listModelLeft.addItem(id)
        }
    }
}