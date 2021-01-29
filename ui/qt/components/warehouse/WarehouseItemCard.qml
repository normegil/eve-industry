import QtQuick 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.0

import "../../predefined" 1.0

Item {
    property int assetID: -1

    property string itemName: "Tritanium"
    property string itemQuantity: "0"
    property string itemPrice: "0"

    property string fontFamily: FontFamilies.family0

    property color iconDetailsColorDefault: Colors.grey6
    property color iconDetailsColorHovered: Colors.grey5

    property color bgIconColorDefault: Colors.grey8
    property color bgIconColorHovered: Colors.grey7

    property int iconWidth: 18
    property int iconHeight: iconWidth


    implicitWidth: 380
    implicitHeight: 60

    Item {
        id: bgContainer
        anchors.fill: parent
        z: 10

        Rectangle {
            id: mainBackground

            width: 345
            anchors {
                left: parent.left
                top: parent.top
                bottom: parent.bottom
            }

            color: Colors.grey9

            Text {
                anchors {
                    left: parent.left
                    leftMargin: 10
                    top: parent.top
                    topMargin: 5
                }

                text: itemName
                verticalAlignment: Text.AlignBottom
                color: Colors.grey4
                font.family: fontFamily
                font.weight: Font.Normal
                font.pixelSize : FontSizes.size1
            }

            Text {
                id: itemQuantityText

                anchors {
                    right: parent.right
                    rightMargin: 35
                    bottom: parent.bottom
                    bottomMargin: 5
                }

                text: itemQuantity
                verticalAlignment: Text.AlignBottom
                color: Colors.grey1
                font.family: fontFamily
                font.pixelSize : FontSizes.size6
            }

            Text {
                anchors {
                    left: itemQuantityText.right
                    leftMargin: 4
                    bottom: parent.bottom
                    bottomMargin: 8
                }

                text: "Units"
                color: Colors.grey4
                verticalAlignment: Text.AlignBottom
                font.family: fontFamily
                font.pixelSize : FontSizes.size0
            }

            Text {
                id: itemPriceText

                anchors {
                    right: parent.right
                    rightMargin: 35
                    top: parent.top
                    topMargin: 3
                }

                text: itemPrice
                horizontalAlignment: Text.AlignRight
                verticalAlignment: Text.AlignBottom
                color: Colors.grey2
                font.family: fontFamily
                font.pixelSize : FontSizes.size3
            }

            Text {
                anchors {
                    left: itemPriceText.right
                    leftMargin: 4
                    top: parent.top
                    topMargin: 8
                }

                text: "ISK/u"
                verticalAlignment: Text.AlignBottom
                color: Colors.grey4
                font.family: fontFamily
                font.pixelSize : FontSizes.size0
            }
        }

        Button {
            id: btn

            QtObject {
                id: btnInternal

                function onHovered(hovered) {
                    if (hovered) {
                        btnBackground.color = bgIconColorHovered
                        iconOverlay.color = iconDetailsColorHovered
                    } else {
                        btnBackground.color = bgIconColorDefault
                        iconOverlay.color = iconDetailsColorDefault
                    }
                }
            }

            anchors {
                left: mainBackground.right
                top: parent.top
                bottom: parent.bottom
                right: parent.right
            }

            background: Rectangle {
                id: btnBackground
                color: bgIconColorDefault
            }

            HoverHandler {
                id: btnHoveredHandler
                onHoveredChanged: {
                    btnInternal.onHovered(hovered)
                }
            }

            Connections {
                target: warehouseAssetDetails
            }

            MouseArea {
                anchors.fill: parent
                cursorShape: Qt.PointingHandCursor

                onPressed: {
                    btnBackground.color = bgIconColorDefault
                    iconOverlay.color = iconDetailsColorDefault
                }

                onReleased: {
                    btnBackground.color = bgIconColorDefault
                    iconOverlay.color = iconDetailsColorDefault
                    btnInternal.onHovered(btnHoveredHandler.hovered)
                    warehouseAssetDetails.loadAsset(assetID)
                }
            }

            Image {
                id: iconComponent

                width: iconWidth
                height: iconHeight
                anchors {
                    right: parent.right
                    rightMargin: 7
                    verticalCenter: parent.verticalCenter
                }

                source: "../../../resources/icons/view-details.svg"
                fillMode: Image.PreserveAspectFit
                visible: false
                antialiasing: true
            }

            ColorOverlay {
                id: iconOverlay

                width: iconWidth
                height: iconHeight
                anchors.fill: iconComponent
                anchors.verticalCenter: parent.verticalCenter

                source: iconComponent
                color: iconDetailsColorDefault
                antialiasing: true
            }
        }
    }

    DropShadow {
        anchors.fill: parent
        z: 0

        source: bgContainer
        horizontalOffset: 2
        verticalOffset: 2
        radius: 5
        color: Colors.grey6
    }
}
