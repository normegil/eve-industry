import QtQuick 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.0

import "../../components/blueprints"
import "../../predefined" 1.0

Item {
    anchors.fill: parent

    Connections {
        target: blueprintController
    }

    Text {
        id: title

        height: 40
        anchors {
            top: parent.top
            left: parent.left
            leftMargin: 25
        }

        text: "Blueprints"
        color: Colors.grey3
        font.family: FontFamilies.family0
        font.pixelSize : FontSizes.size5
    }

    Item {
        width: 850
        anchors {
            top: title.bottom
            bottom: parent.bottom
            left: parent.left
        }
        Item {
            id: controls

            height: 40
            anchors {
                top: parent.top
                left: parent.left
                right: parent.right
            }

            Text {
                id: locationLabel
                width: 150
                anchors {
                    top: parent.top
                    topMargin: 3
                    left: parent.left
                    leftMargin: 40
                }
                text: "Manufacturing location:"
                color: Colors.grey4
                font.family: FontFamilies.family0
                font.pixelSize : FontSizes.size2
            }

            Connections {
                target: blueprintController
            }

            ComboBox {
                id: regionBox
                height: 25
                width: 200
                anchors {
                    top: parent.top
                    left: locationLabel.right
                }
                model: blueprintRegionList
                textRole: "name"
                valueRole: "identifier"
                font.family: FontFamilies.family0
                font.pixelSize : FontSizes.size2
                onActivated: {
                    blueprintController.setCurrentRegion(currentValue)
                }
                Component.onCompleted: {
                    regionBox.currentIndex = blueprintController.initialRegionIndex
                }
            }
        }

        ScrollView {
            clip: true
            anchors {
                top: controls.bottom
                topMargin: 10
                bottom: parent.bottom
                left: parent.left
                right: parent.right
            }

            ListView {
                anchors.fill: parent
                model: blueprintList
                delegate: BlueprintTypeSection {
                    title: name
                    individuals: locations
                }
            }
        }
    }
}