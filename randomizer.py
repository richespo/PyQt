
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QFileDialog
import os, shutil
import random, platform

class Ui_MainWindow(QObject):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(458, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.leNewName = QtWidgets.QLineEdit(self.centralwidget)
        self.leNewName.setGeometry(QtCore.QRect(150, 130, 191, 31))
        self.leNewName.setObjectName("leNewName")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 140, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pTE = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.pTE.setGeometry(QtCore.QRect(150, 180, 191, 71))
        self.pTE.setObjectName("pTE")
        self.pbBegin = QtWidgets.QPushButton(self.centralwidget)
        self.pbBegin.setGeometry(QtCore.QRect(150, 300, 191, 31))
        self.pbBegin.setObjectName("pbBegin")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.pbBegin.clicked.connect(self.chooseDirectory)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    @pyqtSlot()
    def chooseDirectory(self):
        fdialog = QFileDialog()
        fdialog.setFileMode(QFileDialog.DirectoryOnly)
        uname = platform.uname()
        if uname.system == 'Windows':
            start_dir = "C:\\Users\\riche"
        elif uname.system == 'OS X':
            start_dir = "/Users/rich"
        else:
            start_dir = "/home/rich"
        file_name = QFileDialog.getExistingDirectory(None, 'Choose Directory', start_dir)
        if file_name:
            newDir = file_name + "/newfiles/"
            if os.path.isdir(newDir):
                print("Directory exists")
                exit()
            else:
                os.makedirs(newDir)
                fileList = os.listdir(file_name)
                random.shuffle(fileList)
                random.shuffle(fileList)
                random.shuffle(fileList)
                random.shuffle(fileList)
                i = 0
                for fileName in fileList:
                    if fileName.endswith(".jpg") or fileName.endswith(".JPG"):
                        name = self.leNewName.text() + str(i) + ".jpg"
                        shutil.copy(file_name + "/" + fileName, newDir + name)
                        i = i + 1
                self.pTE.document().setPlainText(str(i))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Randomizer"))
        self.label_2.setText(_translate("MainWindow", "New Name"))
        self.pbBegin.setText(_translate("MainWindow", "Begin"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

