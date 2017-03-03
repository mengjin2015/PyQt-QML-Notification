import sys
from PyQt5.QtNetwork import QLocalSocket
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget

import json

class connection(object):
	"""docstring for connection"""
	def __init__(self, servername):
		super(connection, self).__init__()
		self.servername = servername
	
	def connectAndSend(self, content):
		self.content = json.dumps(content)
		self.socket = QLocalSocket()
		self.socket.connectToServer(self.servername)
		# self.socket.connected.connect(self.ready)
		self.socket.write(self.content.encode('utf-8'))
		pass

	# def ready(self):
	# 	print('ready!')
	# 	self.socket.write(self.content.encode('utf-8'))
	# 	pass

if __name__ == '__main__':

	# app = QApplication(sys.argv)

	conn = connection('sample')
	conn.connectAndSend(
		{
			"process" : sys.argv[1],
			"action"  : sys.argv[2],
			"file" : sys.argv[3],
			"time" : sys.argv[4],
			"icon" : sys.argv[5],
			"color": sys.argv[6]
		}
		)

	# w = QWidget()
	# w.resize(250, 150)
	# w.move(300, 300)
	# w.setWindowTitle('Simple')
	# w.show()

	# sys.exit(app.exec_())
	