from PyQt5.QtQuick import QQuickImageProvider
from PyQt5.QtGui import QImage
from PyQt5.QtCore import QSize

class BicImageProvider(QQuickImageProvider):
	"""docstring for BicImageProvider"""
	def __init__(self):
		super(BicImageProvider, self).__init__(QQuickImageProvider.Image)
		# super().__init__(QQuickImageProvider.Image)

	def requestImage(self, id_, requestedSize):
		qimage = QImage(id_)
		# print(id_)
		# print(requestedSize)
		if requestedSize.isValid():
			qimage = qimage.scaled(requestedSize)
			pass
		# print(qimage.size())
		return qimage, qimage.size()
		pass
