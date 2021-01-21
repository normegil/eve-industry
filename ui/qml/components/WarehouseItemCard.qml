import QtQuick 2.0
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.0

import "../predefined" 1.0

Rectangle {
    id: warehouseItemCard

    property string itemName: "Tritanium"
    property color itemNameColor: Colors.grey4

    property string itemQuantity: "50.000k"
    property color itemQuantityColor: Colors.grey0

    property string itemPrice: "2.000k"
    property color itemPriceColor: Colors.grey2

    property color itemPriceTagColor: Colors.grey4
    property color iconDetailsColor: Colors.grey5
    property color shadowColor: Colors.grey0

    property string fontFamily: "Roboto"

    property color bgMainColor: Colors.grey9
    property color bgIconColor: Colors.grey7

    property int iconWidth: 18
    property int iconHeight: iconWidth

    implicitWidth: 230
    implicitHeight: 60
    color: "#00000000"

    Rectangle {
        id: bgContainer
        anchors.fill: parent
        z: 10

        Rectangle {
            id: mainBgWarehouseItemCard

            width: 195
            anchors {
                left: parent.left
                top: parent.top
                bottom: parent.bottom
            }

            color: warehouseItemCard.bgMainColor

            Text {
                text: itemName
                color: itemNameColor

                font.family: fontFamily
                font.weight: Font.Normal
                font.pixelSize : 12

                verticalAlignment: Text.AlignBottom

                anchors {
                    left: parent.left
                    leftMargin: 10
                    top: parent.top
                    topMargin: 5
                }
            }

            Text {
                text: itemQuantity
                color: itemQuantityColor
                font.family: fontFamily
                font.pixelSize : 24

                verticalAlignment: Text.AlignBottom

                anchors {
                    left: parent.left
                    leftMargin: 10
                    bottom: parent.bottom
                    bottomMargin: 5
                }
            }

            Text {
                id: itemPriceWarehouseItemCard
                text: itemPrice
                color: itemPriceColor
                font.family: fontFamily
                font.pixelSize : 16

                horizontalAlignment: Text.AlignRight
                verticalAlignment: Text.AlignBottom

                anchors {
                    right: parent.right
                    rightMargin: 35
                    top: parent.top
                    topMargin: 3
                }
            }

            Text {
                text: "ISK/u"
                color: itemPriceTagColor
                font.family: fontFamily
                font.pixelSize : 10

                verticalAlignment: Text.AlignBottom

                anchors {
                    left: itemPriceWarehouseItemCard.right
                    leftMargin: 4
                    top: parent.top
                    topMargin: 8
                }
            }
        }

        Button {
            id: btnWarehouseItemCard

            anchors {
                left: mainBgWarehouseItemCard.right
                top: parent.top
                bottom: parent.bottom
                right: parent.right
            }

            background: Rectangle {
                id: bgBtnWarehouseItemCard
                color: warehouseItemCard.bgIconColor
            }

            Image {
                id: iconDetailsWarehouseItemCard
                source: "../../resources/icons/view-details.svg"
                width: iconWidth
                height: iconHeight

                anchors {
                    right: parent.right
                    rightMargin: 7
                    verticalCenter: parent.verticalCenter
                }

                fillMode: Image.PreserveAspectFit
                visible: false
                antialiasing: true
            }

            ColorOverlay {
                anchors.fill: iconDetailsWarehouseItemCard
                source: iconDetailsWarehouseItemCard
                color: iconDetailsColor
                antialiasing: true
                anchors.verticalCenter: parent.verticalCenter
                width: iconWidth
                height: iconHeight
            }
        }
    }

    DropShadow {
        anchors.fill: parent
        source: bgContainer
        horizontalOffset: 2
        verticalOffset: 2
        radius: 5
        color: shadowColor
        z: 0
    }
}

/*##^##
Designer {
    D{i:0;autoSize:true;formeditorZoom:1.3300000429153442;height:480;width:640}
}
##^##*/