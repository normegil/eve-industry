import QtQuick 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.0

import "../../components"
import "../../predefined" 1.0

Item {
    anchors.fill: parent

    Text {
        id: detailsTitle

        anchors {
            top: parent.top
            left: parent.left
            topMargin: 40
            right: parent.right
        }

        text: "Buy List"
        color: Colors.grey2
        font.family: FontFamilies.family0
        font.weight: Font.Normal
        font.pixelSize : FontSizes.size4
    }
}