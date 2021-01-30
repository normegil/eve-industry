import QtQuick 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.0

import "../../components"
import "../../predefined" 1.0

Item {
    property string fontFamily: FontFamilies.family0

    Text {
        id: title
        anchors {
            top: parent.top
            left: parent.left
            leftMargin: 20
            right: parent.right
        }
        text: "Statistiques"
        color: Colors.grey3
        font.family: FontFamilies.family0
        font.weight: Font.Normal
        font.pixelSize : FontSizes.size2
    }

    Item {
        anchors {
            top: title.bottom
            topMargin: 10
            bottom: parent.bottom
            left: parent.left
            leftMargin: 5
            right: parent.right
        }

        Text {
            id: minimumText
            anchors {
                top: parent.top
                topMargin: 5
                left: parent.left
            }
            text: "Minimum in stock:"
            color: Colors.grey2
            font.family: FontFamilies.family0
            font.weight: Font.Normal
            font.pixelSize : FontSizes.size2
        }

        TextField {
            id: minimumField
            height: 25
            width: 150
            anchors {
                top: parent.top
                left: minimumText.right
                leftMargin: 10
            }
            text: "50000"
            horizontalAlignment: TextInput.AlignRight
            font.pixelSize: FontSizes.size2
        }
    }
}