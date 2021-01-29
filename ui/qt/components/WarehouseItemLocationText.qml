import QtQuick 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.0

import "../predefined" 1.0

Text {
    id: label
    property string name: "???"

    property color nameColorNormal: Colors.grey4
    property color nameColorHover: Colors.grey1

    property int fontSize: FontSizes.size1

    text: name
    color: nameColorNormal

    font.family: fontFamily
    font.weight: Font.Normal
    font.pixelSize : fontSize

    verticalAlignment: Text.AlignBottom

    HoverHandler {
        id: bgBtnWarehouseItemCardHoveredHandler
        onHoveredChanged: {
            if (hovered) {
                label.color = nameColorHover
            } else {
                label.color = nameColorNormal
            }
        }
    }

    MouseArea {
        anchors.fill: parent
        cursorShape: Qt.PointingHandCursor
    }
}