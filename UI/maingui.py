# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\H.Ali\Desktop\Auto mux mkv\UI\maingui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(650, 690)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        Form.setFont(font)
        Form.setAcceptDrops(False)
        self.search_btn = QtWidgets.QPushButton(Form)
        self.search_btn.setGeometry(QtCore.QRect(560, 10, 75, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.search_btn.setFont(font)
        self.search_btn.setObjectName("search_btn")
        self.folder_path_LE = QtWidgets.QLineEdit(Form)
        self.folder_path_LE.setGeometry(QtCore.QRect(120, 10, 430, 25))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.folder_path_LE.setFont(font)
        self.folder_path_LE.setAcceptDrops(True)
        self.folder_path_LE.setText("")
        self.folder_path_LE.setDragEnabled(False)
        self.folder_path_LE.setObjectName("folder_path_LE")
        self.output_PTE = QtWidgets.QPlainTextEdit(Form)
        self.output_PTE.setGeometry(QtCore.QRect(10, 139, 630, 541))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.output_PTE.setFont(font)
        self.output_PTE.setAcceptDrops(False)
        self.output_PTE.setReadOnly(True)
        self.output_PTE.setObjectName("output_PTE")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 111, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.start_btn = QtWidgets.QPushButton(Form)
        self.start_btn.setEnabled(False)
        self.start_btn.setGeometry(QtCore.QRect(10, 100, 421, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.start_btn.setFont(font)
        self.start_btn.setObjectName("start_btn")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(8, 75, 47, 13))
        self.label_2.setObjectName("label_2")
        self.default_cbox = QtWidgets.QComboBox(Form)
        self.default_cbox.setGeometry(QtCore.QRect(53, 70, 45, 22))
        self.default_cbox.setObjectName("default_cbox")
        self.default_cbox.addItem("")
        self.default_cbox.addItem("")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(103, 75, 47, 13))
        self.label_3.setObjectName("label_3")
        self.forced_cbox = QtWidgets.QComboBox(Form)
        self.forced_cbox.setGeometry(QtCore.QRect(148, 70, 45, 22))
        self.forced_cbox.setObjectName("forced_cbox")
        self.forced_cbox.addItem("")
        self.forced_cbox.addItem("")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(198, 75, 48, 13))
        self.label_4.setObjectName("label_4")
        self.language_cbox = QtWidgets.QComboBox(Form)
        self.language_cbox.setGeometry(QtCore.QRect(248, 70, 45, 22))
        self.language_cbox.setObjectName("language_cbox")
        self.language_cbox.addItem("")
        self.language_cbox.addItem("")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(298, 75, 75, 13))
        self.label_5.setObjectName("label_5")
        self.delay_LE = QtWidgets.QLineEdit(Form)
        self.delay_LE.setGeometry(QtCore.QRect(378, 70, 50, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.delay_LE.setFont(font)
        self.delay_LE.setAcceptDrops(False)
        self.delay_LE.setInputMethodHints(QtCore.Qt.ImhNone)
        self.delay_LE.setObjectName("delay_LE")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(433, 75, 35, 13))
        self.label_6.setObjectName("label_6")
        self.name_LE = QtWidgets.QLineEdit(Form)
        self.name_LE.setGeometry(QtCore.QRect(470, 70, 171, 22))
        self.name_LE.setAcceptDrops(False)
        self.name_LE.setObjectName("name_LE")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(5, 40, 111, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.search_output_btn = QtWidgets.QPushButton(Form)
        self.search_output_btn.setEnabled(False)
        self.search_output_btn.setGeometry(QtCore.QRect(560, 40, 75, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.search_output_btn.setFont(font)
        self.search_output_btn.setObjectName("search_output_btn")
        self.output_path_LE = QtWidgets.QLineEdit(Form)
        self.output_path_LE.setEnabled(False)
        self.output_path_LE.setGeometry(QtCore.QRect(120, 40, 430, 25))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.output_path_LE.setFont(font)
        self.output_path_LE.setAcceptDrops(True)
        self.output_path_LE.setText("")
        self.output_path_LE.setDragEnabled(False)
        self.output_path_LE.setObjectName("output_path_LE")
        self.delete_chbox = QtWidgets.QCheckBox(Form)
        self.delete_chbox.setGeometry(QtCore.QRect(440, 107, 203, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.delete_chbox.setFont(font)
        self.delete_chbox.setObjectName("delete_chbox")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Auto add sub to video"))
        self.search_btn.setText(_translate("Form", "Search"))
        self.folder_path_LE.setPlaceholderText(_translate("Form", "Type your path or use the Search Button"))
        self.label.setText(_translate("Form", "Video Path Folder :"))
        self.start_btn.setText(_translate("Form", "Start Mux"))
        self.label_2.setText(_translate("Form", "Default:"))
        self.default_cbox.setItemText(0, _translate("Form", "Yes"))
        self.default_cbox.setItemText(1, _translate("Form", "No"))
        self.label_3.setText(_translate("Form", "Forced:"))
        self.forced_cbox.setItemText(0, _translate("Form", "Yes"))
        self.forced_cbox.setItemText(1, _translate("Form", "No"))
        self.label_4.setText(_translate("Form", "languge:"))
        self.language_cbox.setItemText(0, _translate("Form", "ara"))
        self.language_cbox.setItemText(1, _translate("Form", "eng"))
        self.label_5.setText(_translate("Form", "Delay(in ms):"))
        self.delay_LE.setText(_translate("Form", "0"))
        self.label_6.setText(_translate("Form", "Name:"))
        self.name_LE.setText(_translate("Form", "Arabic"))
        self.label_7.setText(_translate("Form", "Output Path Folder :"))
        self.search_output_btn.setText(_translate("Form", "Search"))
        self.output_path_LE.setPlaceholderText(_translate("Form", "Leave it Blank will Create \"Done\" Folder in your path with your mux files"))
        self.delete_chbox.setText(_translate("Form", "Delete Original Files After Finish?"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
