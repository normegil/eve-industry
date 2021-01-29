import QtQuick 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.0

import "../predefined" 1.0

Text {
    id: label
    property string name: "???"

    property color nameColorNormal: Colors.grey2
    property color nameColorHover: Colors.grey0

    property int fontSize: FontSizes.size1

    property int locationType: -1
    property int locationID: -1

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
        onPressed: {
            warehouseItemDetails.showInBrowser(locationType, locationID)
        }
    }

    Connections {
        target: warehouseItemDetails
    }
}