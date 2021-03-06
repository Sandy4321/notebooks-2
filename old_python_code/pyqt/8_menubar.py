import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # A QAction is an abstraction for actions performed with a menubar, 
        # toolbar, or with a custom keyboard shortcut.
        exitAction = QAction(QIcon('web.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        # connect the signal from selected action with method quit()
        exitAction.triggered.connect(qApp.quit)

        self.statusBar()

        # create menubar
        menubar = self.menuBar()
        # add a menu
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        self.setGeometry(30,50,300,200)
        self.setWindowTitle('Menubar')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())