import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Window 2.13

import "components"
import "predefined" 1.0

Window {
    width: 1200
    height: 600
    visible: true
    title: qsTr("Eve Industry")

    color: Colors.grey8

//    Rectangle {
//        width: 1000
//        height: 800
//
//        ListView {
//            width: 600
//            height: 600
//            model: warehouseModel
//            delegate: Rectangle {
//                id: rectDel
//                anchors.centerIn: parent
//                color: "#000000"
//
//                width: 200
//                height: 100
//
//                Text {
//                    anchors.centerIn: parent
//                    id: restDelTest
//
//                    color: "#FFFFFF"
//
//                    text: name
//                }
//            }
//        }
//    }

    Loader {
        anchors.fill: parent.fill
        source: "pages/warehouse.qml"
    }
}
