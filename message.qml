import QtQuick 2.0

Rectangle {
	id: root
    width: 900; height: 180
    color: "black"
    Image {
    	id: img
    	width: 180; height: 180
    	anchors.top: root.top
    	anchors.left: root.left
    	objectName: "img"
    	source: "go.png"
    }
    Text {
    	id: textprocess
    	width: 270; height: 90
    	color: "#FFFF00"
    	anchors.left: img.right
    	anchors.top: root.top
    	text: "test_process"
    	font.pointSize: 20
    	verticalAlignment: Text.AlignVCenter
    	objectName: "textprocess"
    }
    Text {
    	id: textaction
    	width: 270; height: 90
    	color: "#FF0000"
    	anchors.left: textprocess.right
    	anchors.top: root.top
    	text: "was block!"
    	font.pointSize: 20
    	verticalAlignment: Text.AlignVCenter
    	objectName: "textaction"
        style: Text.Outline; styleColor: "#AAAAAA" 
    }
    Text {
    	id: filename
    	width: 540; height: 90
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
    	width: 180; height: 180
    	color: "#F0F0F0"
    	anchors.right: root.right
    	anchors.bottom: root.bottom
    	text: "55:00!"
    	font.pointSize: 20
    	verticalAlignment: Text.AlignVCenter
    	objectName: "timestr"
    }
}