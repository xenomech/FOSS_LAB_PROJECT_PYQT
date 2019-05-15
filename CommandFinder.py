# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '56.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import subprocess

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(581, 275)
        MainWindow.setStyleSheet("background-color: rgba(37, 46, 50, 243);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(240, 190, 101, 31))
        self.pushButton.setStyleSheet("background-color: rgb(33, 220, 37);")
        self.pushButton.setObjectName("pushButton")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 50, 561, 31))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit.setStyleSheet("color: rgb(33, 220, 37);")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(10, 130, 561, 31))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.plainTextEdit_2.setStyleSheet("color: rgb(33, 220, 37);")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 30, 221, 17))
        self.label.setStyleSheet("color: rgb(33, 220, 37);")
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 110, 111, 17))
        self.label_2.setStyleSheet("color: rgb(33, 220, 37);")
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 581, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.run)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Command Finder"))
        self.pushButton.setText(_translate("MainWindow", "Find"))
        self.label.setText(_translate("MainWindow", "Enter the command to be located :"))
        self.label_2.setText(_translate("MainWindow", "Location:"))
    def run(self):
        cmd="whereis " + str(self.plainTextEdit.toPlainText())
        process = subprocess.Popen(
            cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        location, err = process.communicate()
        self.plainTextEdit_2.insertPlainText(str(location, "utf-8"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

