# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addEditCoffeeForm.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form2(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(562, 294)
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(20, 10, 531, 51))
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 70, 531, 211))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 2, 1, 1)
        self.description = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.description.setObjectName("description")
        self.gridLayout.addWidget(self.description, 0, 3, 1, 1)
        self.sort = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.sort.setObjectName("sort")
        self.gridLayout.addWidget(self.sort, 1, 1, 1, 1)
        self.type = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.type.setObjectName("type")
        self.gridLayout.addWidget(self.type, 3, 1, 1, 1)
        self.pb = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pb.setObjectName("pb")
        self.gridLayout.addWidget(self.pb, 3, 3, 1, 1)
        self.step = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.step.setObjectName("step")
        self.gridLayout.addWidget(self.step, 2, 1, 1, 1)
        self.id = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.id.setMaximum(100000000)
        self.id.setObjectName("id")
        self.gridLayout.addWidget(self.id, 0, 1, 1, 1)
        self.price = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.price.setMaximum(99999999.99)
        self.price.setObjectName("price")
        self.gridLayout.addWidget(self.price, 1, 3, 1, 1)
        self.volume = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.volume.setMaximum(99999.99)
        self.volume.setObjectName("volume")
        self.gridLayout.addWidget(self.volume, 2, 3, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Если ID 0 или указан не существующий, тогда создастся новая запись, иначе внесутся изменения в существующую запись </p></body></html>"))
        self.label_6.setText(_translate("Form", "Молотый/в зернах:"))
        self.label_4.setText(_translate("Form", "Цена:"))
        self.label_5.setText(_translate("Form", "Степень обжарки"))
        self.label_3.setText(_translate("Form", "Название сорта:"))
        self.label_7.setText(_translate("Form", "Обьем упаковки:"))
        self.label_2.setText(_translate("Form", "ID:"))
        self.label.setText(_translate("Form", "Описание вкуса:"))
        self.pb.setText(_translate("Form", "ОК"))
