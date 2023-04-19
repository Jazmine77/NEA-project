# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\neals\Documents\computer science\NEA-project\Fin whale.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Info_fw(object):
    def setupUi(self, Info_fw):
        Info_fw.setObjectName("Info_fw")
        Info_fw.resize(770, 599)
        Info_fw.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        Info_fw.setStyleSheet("background-color: rgb(77, 98, 175);\n"
"color: rgb(0, 0, 0);\n"
"font: 18pt \"Palatino Linotype\";")
        self.title = QtWidgets.QLabel(Info_fw)
        self.title.setGeometry(QtCore.QRect(320, 20, 181, 31))
        self.title.setStyleSheet("\n"
"font: 24pt \"Palatino Linotype\";\n"
"text-decoration: underline;\n"
"color: rgb(255, 170, 255);\n"
"")
        self.title.setObjectName("title")
        self.textBrowser = QtWidgets.QTextBrowser(Info_fw)
        self.textBrowser.setGeometry(QtCore.QRect(10, 70, 751, 341))
        self.textBrowser.setObjectName("textBrowser")
        self.prediction_fw = QtWidgets.QPushButton(Info_fw)
        self.prediction_fw.setGeometry(QtCore.QRect(420, 420, 241, 61))
        self.prediction_fw.setObjectName("prediction")
        self.photo = QtWidgets.QLabel(Info_fw)
        self.photo.setGeometry(QtCore.QRect(40, 420, 361, 191))
        self.photo.setText("")
        self.photo.setPixmap(QtGui.QPixmap("C:\\Users\\neals\\Documents\\computer science\\NEA-project\\fw.jpg"))
        self.photo.setScaledContents(True)
        self.photo.setObjectName("photo")

        self.retranslateUi(Info_fw)
        QtCore.QMetaObject.connectSlotsByName(Info_fw)

    def retranslateUi(self, Info_fw):
        _translate = QtCore.QCoreApplication.translate
        Info_fw.setWindowTitle(_translate("Info_fw", "Information"))
        self.title.setText(_translate("Info_fw", "Fin whales"))
        self.textBrowser.setHtml(_translate("Info_fw", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Palatino Linotype\'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-style:italic; color:#ffaaff;\">Population</span><span style=\" color:#000000;\">: between 100,000 to 119,000 </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-style:italic; color:#ffaaff;\">Fun fact</span><span style=\" font-style:italic; color:#ffaaff;\">:</span><span style=\" color:#ffaaff;\">Fin whales are the second largest whale species</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-style:italic; color:#ffaaff;\">Dangers</span><span style=\" color:#ffaaff;\">: </span><span style=\" color:#000000;\">Like other large whales, fin whales are threatened by environmental changes including habitat loss, toxins and climate change.However commercial whaling remains a threat to fin whales</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-style:italic; color:#ffaaff;\">Diet</span><span style=\" font-size:20pt; font-style:italic; color:#000000;\">: </span><span style=\" color:#000000;\">During the summer they feed on krill, small schooling fish and squid.In winter they fast. Fin whales eat up to 2 tons of food daily</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-style:italic; color:#ffaaff;\">General location</span><span style=\" color:#000000;\">:They live in deep, offshore waters in most major oceans but primiraly in temperate to polar latitudes and are less common in tropics.Most migrate from the Arctic and antarctic feeding areas in the summer to tropical breeding areas in winter</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-style:italic; color:#ffaaff;\">Fun fact</span><span style=\" color:#000000;\">:</span><span style=\" color:#ffaaff;\"> The location of winter breeding areas are not know as fin whales travel in deep open sea and are difficult to track</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-style:italic; color:#ffaaff;\">Role in ecosystem</span><span style=\" color:#000000;\">: They are at the top of the ecosystem and play an important role have an important role in overall health of the marine environment.Each whale sequesters 33 tons of CO2 on aveage taking that carbon out of the atmosphere for centuries.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-style:italic; color:#ffaaff;\">Life span</span><span style=\" color:#000000;\">: 80-90 years</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-style:italic; color:#ffaaff;\">Description</span><span style=\" color:#000000;\">: Sleek, streamlined bodies with V-shaped bodies.They have a tall, hooked dorsal fin that rises at a shallow angle from the back. They have distinctive colours of black or dark brownish-gray on the back and sides.Many have several light-grey, V-shaped chevron behind their heads on the underside of the tail flukes is white with a grey border.This markings are unique and can be used to identify indiviuals</span></p></body></html>"))
        self.prediction_fw.setText(_translate("Info_fw", "Predicted movement"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Info_fw = QtWidgets.QDialog()
    ui = Info_fw()
    ui.setupUi(Info_fw)
    Info_fw.show()
    sys.exit(app.exec_())
