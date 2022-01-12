from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(812, 632)
        Dialog.setStyleSheet("background-color: rgb(10, 10, 125);")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 700, 700))
        self.frame.setStyleSheet("background-color: rgb(200, 251, 251);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.plant_label = QtWidgets.QLabel(self.frame)
        self.plant_label.setGeometry(QtCore.QRect(0, 165, 250, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.plant_label.setFont(font)
        self.plant_label.setStyleSheet("color: rgb(0, 0, 0);")
        self.plant_label.setObjectName("plant_label")

        self.plantEdit = QtWidgets.QLineEdit(self.frame)
        self.plantEdit.setGeometry(QtCore.QRect(260, 165, 250, 30))
        self.plantEdit.setStyleSheet("color: rgb(0, 0, 0);")
        self.plantEdit.setStyleSheet("background-color: rgb(10, 207, 255); color: rgb(0, 0, 0);")
        self.plantEdit.setObjectName("plantEdit")

        self.length_label = QtWidgets.QLabel(self.frame)
        self.length_label.setGeometry(QtCore.QRect(0, 250, 250, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.length_label.setFont(font)
        self.length_label.setStyleSheet("color: rgb(0, 0, 0);")
        self.length_label.setObjectName("length_label")

        self.lengthEdit = QtWidgets.QLineEdit(self.frame)
        self.lengthEdit.setGeometry(QtCore.QRect(260, 250, 250, 30))
        self.lengthEdit.setStyleSheet("color: rgb(0, 0, 0);")
        self.lengthEdit.setStyleSheet("background-color: rgb(10, 207, 255); color: rgb(0, 0, 0);")
        self.lengthEdit.setObjectName("lengthEdit")

        self.weight_label = QtWidgets.QLabel(self.frame)
        self.weight_label.setGeometry(QtCore.QRect(0, 335, 250, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.weight_label.setFont(font)
        self.weight_label.setStyleSheet("color: rgb(0, 0, 0);")
        self.weight_label.setObjectName("weight_label")

        self.weigthEdit = QtWidgets.QLineEdit(self.frame)
        self.weigthEdit.setGeometry(QtCore.QRect(260, 335, 250, 30))
        self.weigthEdit.setStyleSheet("color: rgb(0, 0, 0);")
        self.weigthEdit.setStyleSheet("background-color: rgb(10, 207, 255); color: rgb(0, 0, 0);")
        self.weigthEdit.setObjectName("weigthEdit")

        self.write = QtWidgets.QPushButton(self.frame)
        self.write.setGeometry(QtCore.QRect(350, 400, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.write.setFont(font)
        self.write.setStyleSheet("background-color: rgb(0, 170, 0);")
        self.write.setObjectName("pushButton")

        self.go_one_line = QtWidgets.QPushButton(self.frame)
        self.go_one_line.setGeometry(QtCore.QRect(0, 450, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.go_one_line.setFont(font)
        self.go_one_line.setStyleSheet("background-color: rgb(100, 170, 100);")
        self.go_one_line.setObjectName("pushButton1")

        self.go_last_line = QtWidgets.QPushButton(self.frame)
        self.go_last_line.setGeometry(QtCore.QRect(400, 450, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.go_last_line.setFont(font)
        self.go_last_line.setStyleSheet("background-color: rgb(100, 170, 100);")
        self.go_last_line.setObjectName("pushButton2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.plant_label.setText(_translate("Dialog", "Название растения"))
        self.write.setText(_translate("Dialog", "Записать"))
        self.go_one_line.setText(_translate("Dialog", "Все записи"))
        self.go_last_line.setText(_translate("Dialog", "Последняя запись"))
        self.length_label.setText(_translate("Dialog", "Длина стебля"))
        self.weight_label.setText(_translate("Dialog", "Вес"))

