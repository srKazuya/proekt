# Form implementation generated from reading ui file 'e:\Folders\planer\PyQt5-Daily-Task-Planner-App\output\planirovka_zadaniy\_internal\main.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(852, 554)
        self.calendarWidget = QtWidgets.QCalendarWidget(parent=Form)
        self.calendarWidget.setGeometry(QtCore.QRect(40, 180, 411, 311))
        self.calendarWidget.setStyleSheet("font: 75 16pt \"OriginalGaramond BT\";\n"
"background :#6DE0E6;\n"
"color : black;\n"
"")
        self.calendarWidget.setObjectName("calendarWidget")
        self.tasksListWidget = QtWidgets.QListWidget(parent=Form)
        self.tasksListWidget.setGeometry(QtCore.QRect(480, 180, 341, 301))
        self.tasksListWidget.setStyleSheet("\n"
"font: 75 14pt \"OriginalGaramond BT\";")
        self.tasksListWidget.setObjectName("tasksListWidget")
        self.saveButton = QtWidgets.QPushButton(parent=Form)
        self.saveButton.setGeometry(QtCore.QRect(480, 490, 341, 28))
        self.saveButton.setStyleSheet("font: 75 16pt \"OriginalGaramond BT\";\n"
"\n"
"background :#6DE0E6;\n"
"color : black;\n"
"border-radius:8px;")
        self.saveButton.setObjectName("saveButton")
        self.addButton = QtWidgets.QPushButton(parent=Form)
        self.addButton.setGeometry(QtCore.QRect(730, 140, 93, 28))
        self.addButton.setStyleSheet("\n"
"font: 75 16pt \"OriginalGaramond BT\";\n"
"background :#6DE0E6;\n"
"color : black;\n"
"border-radius:8px;\n"
"")
        self.addButton.setObjectName("addButton")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(40, 30, 781, 101))
        self.label.setStyleSheet("\n"
"font: 36pt \"AvantGardeGothicBkITC\";\n"
"background : #3DC6CD;\n"
"color : white;\n"
"border-radius:8px;\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.taskLineEdit = QtWidgets.QLineEdit(parent=Form)
        self.taskLineEdit.setGeometry(QtCore.QRect(480, 140, 241, 31))
        self.taskLineEdit.setStyleSheet("font: 75 14pt \"OriginalGaramond BT\";")
        self.taskLineEdit.setObjectName("taskLineEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.saveButton.setText(_translate("Form", "Сохранить"))
        self.addButton.setText(_translate("Form", "Добавить"))
        self.label.setText(_translate("Form", "Планировка Заданий"))
