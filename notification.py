import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, QTimer
from PyQt5.QtGui import QImage, QPixmap
OS = 0

try:
    from ctypes import windll
except:    
	OS = 1
import time

from ui_notification_qml import Ui_Notification

class Notification(QtWidgets.QMainWindow):
    closed = QtCore.pyqtSignal()
    y = 0
    threads = []
    timers = []
    percount = 30
    fading = False

    def __init__(self,mssg,y=0,parent=None):
        QtWidgets.QWidget.__init__(self,parent)
        self.parent = parent
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.text_color = mssg["color"]
        self.mssg = mssg
        
        self.ui = Ui_Notification()
        self.ui.setupUi(self)
        self.y = y
        self.createNotification(mssg)
        
    def closeEvent(self,event):
        # print("done")
        self.closed.emit()
        
    def createNotification(self,mssg):
        global OS
        if (OS!= 1):
            user32 = windll.user32
            #Get X coordinate of screen
            self.x = user32.GetSystemMetrics(0)
            self.sh = user32.GetSystemMetrics(1)
        else:
            cp = QtWidgets.QDesktopWidget().availableGeometry()
            self.x = cp.width()
            self.sh = cp.height()

        self.x -= 10
        #self.x -= self.ui.twidth
        # self.y -= (self.ui.theight - 100)
        self.move(self.x, self.y)

        # print(self.x)
        # print(self.y)

        # Set the opacity
        self.f = 1.0

        # Set the message 

        # self.moveDown()
        self.appearFromLeft()
        return

    def appearFromLeft(self):
        # Start Worker
        workThread = WorkThread(int(self.ui.twidth/self.percount),0.25/self.ui.twidth*self.percount)

        workThread.update.connect(self.appear)
        workThread.vanish.connect(self.disappear)
        workThread.finished.connect(self.done)

        workThread.start()
        # print("appear")
        self.threads.append(workThread)
        pass

    def fade(self):
        #Start Worker
        workThread = WorkThread(50,0.01)

        workThread.update.connect(self.disappear)
        # workThread.vanish.connect(self.disappear)
        workThread.finished.connect(self.done)

        workThread.start()
        # print("fade")
        self.threads.append(workThread)
        pass

    def moveDown(self):

        if self.y <= self.sh:
            #Start Worker
            workThread = WorkThread(int(self.ui.theight/self.percount), 0.25/self.ui.theight*self.percount)

            workThread.update.connect(self.animate)
            workThread.vanish.connect(self.disappear)
            workThread.finished.connect(self.done)

            workThread.start()
            # print("moveDown")
            self.threads.append(workThread)   
            pass
        else:
            self.hide()
            pass
        pass

    #Quit when done
    def done(self):
        if self.fading:
            # print("done")
            self.close()
            pass
        else:
            timer = QTimer()
            timer.timeout.connect(self.checkdone)
            timer.setInterval(1000)
            timer.setSingleShot(True)
            timer.start()
            self.timers.append(timer)
            pass

        return

    def checkdone(self):
        # print("done")
        self.threads = [th for th in self.threads if th.isFinished()==False]

        if len(self.threads)==0:
            self.fading = True
            self.fade()
            pass
        pass

    #Reduce opacity of the window
    def disappear(self):
        self.f -= 0.02
        self.setWindowOpacity(self.f)
        return
    
    #Move in animation
    def appear(self):
        # print("update")
        self.x -= self.percount
        self.move(self.x,self.y)
        return    
        
    #Move in animation
    def animate(self):
        # print("update")
        self.y += self.percount
        self.move(self.x,self.y)

        return
        
#The Worker
class WorkThread(QtCore.QThread):
    def __init__(self, count=336, interval=0.001):
        QtCore.QThread.__init__(self)
        self.count = count
        self.interval = interval

    update = pyqtSignal('QString')
    vanish = pyqtSignal('QString')
    finished = pyqtSignal()

    def run(self):
        # print("start")
        for i in range(self.count):
            time.sleep(self.interval)
            self.update.emit("ping")

        time.sleep(5)
        # print("finish")
        self.finished.emit()    
        return

def Notify(msg):
    app = QtWidgets.QApplication(sys.argv)
    myapp = Notification(msg, 0)
    # myapp.moveDown()
    # myapp.moveDown()
    myapp.show()

    #print("done!")
    sys.exit(app.exec_())

def NotifyOnce(msg):
    myapp = Notification(msg, 30)
    myapp.show()
    # print(msg)
    return myapp
     

        
        
        
