import QtQuick 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.0

import "../../predefined" 1.0

Item {
    id: clickableList

    property string title: ""
    property var listModel: ListModel{}
    property var onSelectedItem: function(selectedItem) {}

    Text {
        id: warehouseGroupsNotDisplayedLabel
        anchors {
            top: parent.top
            horizontalCenter: parent.horizontalCenter
        }
        text: title
        color: Colors.grey3
        font.family: FontFamilies.family0
        font.pixelSize: FontSizes.size1
    }

    Rectangle {
        color: Colors.grey9
        anchors {
            top: warehouseGroupsNotDisplayedLabel.bottom
            topMargin: 5
            left: parent.left
            right: parent.right
            bottom: parent.bottom
        }
        ScrollView {
            clip: true
            anchors.fill: parent
            ListView {
                anchors.fill: parent
                model: listModel
                delegate: Text {
                    text: name
                    color: Colors.grey1
                    font.family: FontFamilies.family0
                    font.pixelSize: FontSizes.size3

                    MouseArea {
                        anchors.fill: parent
                        cursorShape: Qt.PointingHandCursor
                        onPressed: {
                            onSelectedItem(identifier)
                        }
                    }
                }
            }
        }
    }
}