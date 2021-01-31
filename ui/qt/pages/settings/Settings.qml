import QtQuick 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.0

import "../../components"
import "../../predefined" 1.0

Item {
    anchors.fill: parent

    property int borderWidth: 1200
    property int settingsControlWidth: 780
    property int settingsControlTopMargin: 24
    property int settingsControlLeftMargin: 400

    Text {
        id: title

        height: 40
        anchors {
            top: parent.top
            left: parent.left
            leftMargin: 25
        }

        text: "Settings"
        color: Colors.grey3
        font.family: FontFamilies.family0
        font.pixelSize : FontSizes.size5
    }

    Rectangle {
        id: titleBottomBorder
        anchors {
            top: title.bottom
            left: parent.left
            leftMargin: 50
            right: parent.right
            rightMargin: 50
        }
        height: 2
        border.width: 1
        border.color: Colors.grey7
    }

    ScrollView {
        width: 1200
        anchors {
            top: titleBottomBorder.bottom
            topMargin: 10
            bottom: parent.bottom
            horizontalCenter: parent.horizontalCenter
        }
        clip: true

        Rectangle {
            id: warehouseTopSeparator
            anchors {
                top: parent.top
                left: parent.left
                right: parent.right
            }
            height: 2
            border.width: 1
            border.color: Colors.grey7
        }

        Text {
            anchors {
                top: warehouseTopSeparator.top
                left: parent.left
                topMargin: 20
                leftMargin: 20
            }
            text: "Warehouse"
            color: Colors.grey3
            font.family: FontFamilies.family0
            font.pixelSize: FontSizes.size4
        }

        Rectangle {
            id: warehouseSettingsContainer
            color: Colors.grey5
            width: settingsControlWidth
            anchors {
                top: parent.top
                topMargin: settingsControlTopMargin
                left: parent.left
                leftMargin: settingsControlLeftMargin
            }

            Text {
                id: assetGroupsSelectorLabel
                text: "Select asset groups to show:"
                anchors {
                    left: parent.left
                    leftMargin: 20
                }
                color: Colors.grey3
                font.family: FontFamilies.family0
                font.pixelSize: FontSizes.size2
            }

            Item {
                height: 400
                anchors {
                    top: assetGroupsSelectorLabel.bottom
                    topMargin: 10
                    left: parent.left
                    right: parent.right
                }

                Item {
                    anchors {
                        top: parent.top
                        left: parent.left
                        bottom: parent.bottom
                        right: parent.horizontalCenter
                        rightMargin: 5
                    }

                    Text {
                        id: warehouseGroupsNotDisplayedLabel
                        anchors {
                            top: parent.top
                            horizontalCenter: parent.horizontalCenter
                        }
                        text: "Not Displayed"
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
                                model: settingsWarehouseGroupsNotFollowed
                                delegate: Text {
                                    anchors {
                                        left: parent.left
                                        right: parent.right
                                    }
                                    text: name
                                    color: Colors.grey1
                                    font.family: FontFamilies.family0
                                    font.pixelSize: FontSizes.size3

                                    MouseArea {
                                        anchors.fill: parent
                                        cursorShape: Qt.PointingHandCursor
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}