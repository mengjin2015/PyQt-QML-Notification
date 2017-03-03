import QtQuick 2.0

Rectangle {
	id: root
    width: 800; height: 160
    color: "black"
    Image {
    	id: img
    	width: 160; height: 160
    	anchors.top: root.top
    	anchors.left: root.left
    	objectName: "img"
    	source: "Stop_sign.png"
    }
    Text {
    	id: textprocess
    	width: 240; height: 80
    	color: "#FFFF00"
    	anchors.left: img.right
    	anchors.top: root.top
    	text: "test_process"
    	font.pointSize: 18
    	verticalAlignment: Text.AlignVCenter
    	objectName: "textprocess"
    }
    Text {
    	id: textaction
    	width: 240; height: 80
    	color: "#FF0000"
    	anchors.left: textprocess.right
    	anchors.top: root.top
    	text: "was block!"
    	font.pointSize: 18
    	verticalAlignment: Text.AlignVCenter
    	objectName: "textaction"
        style: Text.Outline; styleColor: "#AAAAAA" 
        SequentialAnimation on styleColor {
            loops: Animation.Infinite
            ColorAnimation { from: "#AAAAAA"; to: "#000000"; duration: 1000 }
            ColorAnimation { from: "#000000"; to: "#AAAAAA"; duration: 1000 }
        }
    }
    Text {
    	id: filename
    	width: 480; height: 80
    	color: "#E0E0E0"
    	anchors.left: img.right
    	anchors.bottom: root.bottom
    	text: "file: something!"
    	font.pointSize: 12
    	verticalAlignment: Text.AlignVCenter
    	objectName: "filename"
    }
    Text {
    	id: timestr
    	width: 160; height: 160
    	color: "#F0F0F0"
    	anchors.right: root.right
    	anchors.bottom: root.bottom
    	text: "55:00!"
    	font.pointSize: 20
    	verticalAlignment: Text.AlignVCenter
    	objectName: "timestr"
    }
}