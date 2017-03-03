import sys
from PyQt5.QtNetwork import QLocalServer, QLocalSocket
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QIODevice

import notification
import json

class NotificaitonServer(object):
	"""docstring for NotificaitonServer"""

	notifications = []

	def __init__(self, name, app):
		super(NotificaitonServer, self).__init__()
		self.name = name
		self.app = app
	
	def startServer(self):
		self.server = QLocalServer()
		self.server.listen(self.name)
		self.server.newConnection.connect(self.connected)
		pass		

	def connected(self):
		# print("conncted!")
		if self.server.hasPendingConnections():
			self.conn = self.server.nextPendingConnection()
			# print(type(self.conn))
			self.conn.readyRead.connect(self.received)
			pass
		pass

	def received(self):
		# print("received!")
		content = self.conn.readAll()
		# print()
		self.notifications = [w for w in self.notifications if w.isVisible()]
		# print(len(self.notifications))
		for w in self.notifications:
			w.moveDown()
			pass

		payload = json.loads(bytes(content).decode("utf-8"))
		no = notification.NotifyOnce(payload)
		
		self.notifications.append(no)
		# ret = app.exec_()
		# print("app able to exit")
		# sys.exit(ret)
		pass

if __name__ == '__main__':
	
	app = QApplication(sys.argv)

	server = NotificaitonServer('sample', app)
	server.startServer()

	# no = notification.NotifyOnce('test')
	# notification.Notify('test')
	# w = QWidget()
	# w.resize(250, 150)
	# w.move(300, 300)
	# w.setWindowTitle('Simple')
	# w.show()
	ret = app.exec_()
	# print(ret)
	while ret==0:
		ret = app.exec_()
		pass
	print("app able to exit 0 ")	
	# ret = app.exec_()
	# print("app able to exit 1 ")	
	
	sys.exit(ret)
		