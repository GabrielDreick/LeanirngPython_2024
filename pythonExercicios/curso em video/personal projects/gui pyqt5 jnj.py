from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(200, 200, 300, 300)  # xpos, ypos, width, height
        self.setWindowTitle("Tech With Tim!")
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("My First Label!")
        self.label.move(50, 50)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Click me")
        self.b1.clicked.connect(self.clicked)
        self.b1.clickcount = 0


    def clicked(self):
        self.label.setText("you clicked the button")
        self.b1.clickcount += 1
        self.update()


    def update(self):
        self.label.adjustSize()


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.setGeometry(200, 200, 300, 300)  # xpos, ypos, width, height
    win.setWindowTitle("Tech With Tim!")

    win.show()
    sys.exit(app.exec_())


window()
