# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\neals\Documents\computer science\NEA-project\Sperm whale.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Info_sw(object):
    def setupUi(self, Information_sw):
        Information_sw.setObjectName("Information_sw")
        Information_sw.resize(770, 743)
        Information_sw.setStyleSheet("background-color: rgb(77, 98, 175);\n"
"color: rgb(0, 0, 0);\n"
"\n"
"font: 18pt \"Palatino Linotype\";")
        self.title = QtWidgets.QLabel(Information_sw)
        self.title.setGeometry(QtCore.QRect(260, 30, 201, 31))
        self.title.setStyleSheet("\n"
"font: 24pt \"Palatino Linotype\";\n"
"text-decoration: underline;\n"
"color: rgb(255, 170, 255);\n"
"")
        self.title.setObjectName("title")
        self.prediction = QtWidgets.QPushButton(Information_sw)
        self.prediction.setGeometry(QtCore.QRect(480, 470, 241, 61))
        self.prediction.setObjectName("prediction")
        self.photo = QtWidgets.QLabel(Information_sw)
        self.photo.setGeometry(QtCore.QRect(50, 410, 351, 181))
        self.photo.setText("")
        self.photo.setPixmap(QtGui.QPixmap("C:\\Users\\neals\\Documents\\computer science\\NEA-project\\spw.png"))
        self.photo.setScaledContents(True)
        self.photo.setObjectName("photo")
        self.info_box = QtWidgets.QTextBrowser(Information_sw)
        self.info_box.setGeometry(QtCore.QRect(10, 80, 751, 341))
        self.info_box.setObjectName("info_box")

        self.retranslateUi(Information_sw)
        QtCore.QMetaObject.connectSlotsByName(Information_sw)

    def retranslateUi(self, Information_sw):
        _translate = QtCore.QCoreApplication.translate
        Information_sw.setWindowTitle(_translate("Information_sw", "Information"))
        self.title.setText(_translate("Information_sw", "Sperm Whale"))
        self.prediction.setText(_translate("Information_sw", "Predicted movement"))
        self.info_box.setHtml(_translate("Information_sw", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Palatino Linotype\'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-style:italic; color:#ffaaff;\">Population</span><span style=\" color:#000000;\">: 300,000 and are listed as endangered under the Endangered Species Act</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-style:italic; color:#ffaaff;\">Fun fact: </span><span style=\" color:#ffaaff;\">They have the largest brain of any animal weighing up to 4.2 kg</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-style:italic; color:#ffaaff;\">Dangers: </span><span style=\" color:#000000;\">Climate change, ocean noise, oil spills and contaminants, vessel strikes, entanglement in fishing gear</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-style:italic; color:#ffaaff;\">Diet</span><span style=\" font-size:20pt; font-style:italic; color:#000000;\">: </span><span style=\" color:#000000;\">They hunt for food during deep dives that routinely reach depths of 2,000 feet therefore eat mainly squid, sharks, skates and fish</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-style:italic; color:#ffaaff;\">General location</span><span style=\" color:#000000;\">:There population distrubtion is dependant on their food source and breeding conditions.There migration patterns are not as well understood or predictable however some populations appear to have different migration patterns by life history like females and young staying in tropical water</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-style:italic; color:#ffaaff;\">Fun fact</span><span style=\" color:#000000;\">: </span><span style=\" color:#ffaaff;\">Posses most the most asymmetrical skull of any mammal</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-style:italic; color:#ffaaff;\">Role in ecosystem</span><span style=\" color:#000000;\">: Regulate flow of food and help to maintain a stable marine food chain by ensuring that certain species do not overpopulate the ocean</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-style:italic; color:#ffaaff;\">Life span</span><span style=\" color:#000000;\">: up to 60 years</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-style:italic; color:#ffaaff;\">Description</span><span style=\" color:#000000;\">: dark grey with variations of white patchs on belly. Only cetacean with a single blowhole asymmetrically placed on left side of the crown of the head.Their heads account for one-third of their total body length</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://www.firmm.org/en/adoption/sperm-whales\"><span style=\" text-decoration: underline; color:#0000ff;\">Adopt a sperm whale</span></a></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Information_sw = QtWidgets.QDialog()
    ui = Info_sw()
    ui.setupUi(Information_sw)
    Information_sw.show()
    sys.exit(app.exec_())