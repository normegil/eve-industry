import QtQuick 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.0

import "../../components/warehouse"
import "../../predefined" 1.0

Item {
    anchors.fill: parent

    Connections {
        target: warehouseController
    }

    Text {
        id: title

        height: 40
        anchors {
            top: parent.top
            left: parent.left
            leftMargin: 25
        }

        text: "Warehouse"
        color: Colors.grey3
        font.family: FontFamilies.family0
        font.weight: Font.Normal
        font.pixelSize : FontSizes.size5
    }

    Item {
        id: controls

        height: 40
        anchors {
            top: title.bottom
            left: parent.left
            right: parent.right
        }

        Item {
            anchors {
                top: parent.top
                topMargin: 5
                bottom: parent.bottom
                left: parent.left
                leftMargin: 750
            }

            Button {
                id: refreshBtn
                flat: true
                onClicked: {
                    warehouseController.refreshData()
                }

                contentItem: Text {
                    text: "Refresh"
                    color: refreshBtn.down ? Colors.grey2 : Colors.grey4
                    font: FontFamilies.family0
                    verticalAlignment: Text.AlignVCenter
                    horizontalAlignment: Text.AlignHCenter
                }

                height: 30
            }

            Button {
                id: buyingListBtn
                onClicked: {
                    warehouseController.changePage("buylist")
                }

                anchors {
                    top: parent.top
                    left: refreshBtn.right
                    leftMargin: 10
                }

                contentItem: Text {
                    text: "Buying List"
                    color: buyingListBtn.down ? Colors.grey2 : Colors.grey3
                    font: FontFamilies.family0
                    verticalAlignment: Text.AlignVCenter
                    horizontalAlignment: Text.AlignHCenter
                }

                background: Rectangle {
                    id: buyingListBtnBackground
                    implicitWidth: 100
                    implicitHeight: 30
                    color: buyingListBtn.down ? Colors.grey8 : Colors.grey9
                }
            }
        }
    }

    ScrollView {
        id: groupsView
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
            model: warehouseAssetsGroups
            delegate: WarehouseAssetsGroup {
                name: groupName
                assets: groupAssets
            }
        }
    }
}