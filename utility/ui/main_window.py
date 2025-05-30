# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(70, 110, 341, 91))
        self.groupBox.setObjectName("groupBox")
        self.json_file_path_textEdit = QtWidgets.QTextEdit(self.groupBox)
        self.json_file_path_textEdit.setGeometry(QtCore.QRect(10, 30, 200, 40))
        self.json_file_path_textEdit.setObjectName("json_file_path_textEdit")
        self.open_file_btn = QtWidgets.QPushButton(self.groupBox)
        self.open_file_btn.setGeometry(QtCore.QRect(230, 30, 100, 40))
        self.open_file_btn.setObjectName("open_file_btn")
        self.test_type_TextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.test_type_TextEdit.setGeometry(QtCore.QRect(190, 30, 491, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.test_type_TextEdit.setFont(font)
        self.test_type_TextEdit.setObjectName("test_type_TextEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 40, 91, 31))
        self.label.setObjectName("label")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 210, 751, 351))
        self.groupBox_2.setObjectName("groupBox_2")
        self.output_test_edit = QtWidgets.QTextEdit(self.groupBox_2)
        self.output_test_edit.setGeometry(QtCore.QRect(10, 20, 731, 311))
        self.output_test_edit.setObjectName("output_test_edit")
        self.run_test_btn = QtWidgets.QPushButton(self.centralwidget)
        self.run_test_btn.setGeometry(QtCore.QRect(510, 120, 121, 71))
        self.run_test_btn.setObjectName("run_test_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "文件"))
        self.open_file_btn.setText(_translate("MainWindow", "打开文件"))
        self.label.setText(_translate("MainWindow", "测试类别："))
        self.groupBox_2.setTitle(_translate("MainWindow", "输出"))
        self.run_test_btn.setText(_translate("MainWindow", "执行测试"))
