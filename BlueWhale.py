# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\neals\Documents\computer science\NEA-project\blueWhales.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Info_BW(object):
    def setupUi(self, Information_BW):
        Information_BW.setObjectName("Information_BW")
        Information_BW.resize(770, 599)
        Information_BW.setMinimumSize(QtCore.QSize(0, 0))
        Information_BW.setStyleSheet("background-color: rgb(77, 98, 175);\n"
"color: rgb(0, 0, 0);\n"
"font: 18pt \"Palatino Linotype\";\n"
"")
        self.title = QtWidgets.QLabel(Information_BW)
        self.title.setGeometry(QtCore.QRect(320, 20, 181, 31))
        self.title.setStyleSheet("\n"
"font: 24pt \"Palatino Linotype\";\n"
"text-decoration: underline;\n"
"color: rgb(255, 170, 255);\n"
"")
        self.title.setObjectName("title")
        self.photo = QtWidgets.QLabel(Information_BW)
        self.photo.setGeometry(QtCore.QRect(20, 410, 361, 191))
        self.photo.setText("")
        self.photo.setPixmap(QtGui.QPixmap("C:\\Users\\neals\\Documents\\computer science\\NEA-project\\bw.jpg"))
        self.photo.setScaledContents(True)
        self.photo.setObjectName("photo")

        self.info_box = QtWidgets.QTextBrowser(Information_BW)
        self.info_box.setGeometry(QtCore.QRect(10, 70, 751, 341))
        self.info_box.setStyleSheet("")
        self.info_box.setObjectName("info_box")

        self.retranslateUi(Information_BW)
        QtCore.QMetaObject.connectSlotsByName(Information_BW)

    def retranslateUi(self, Information_BW):
        _translate = QtCore.QCoreApplication.translate
        Information_BW.setWindowTitle(_translate("Information_BW", "Information"))
        self.title.setText(_translate("Information_BW", "Blue whales"))

        self.info_box.setHtml(_translate("Information_BW", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Palatino Linotype\'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-style:italic; color:#ffaaff;\">Population</span><span style=\" font-size:14pt;\">: </span>is between 10,000 and 25,000 and they are listed as endangered under the Endangered Species Act and protected under the Marine Mammal Protection Act</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-style:italic; color:#ffaaff;\">Fun fact</span><span style=\" font-size:20pt; color:#ffaaff;\">: Their tongues weighs as much as an elephant</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-style:italic; color:#ffaaff;\">Dangers</span>: Due to early 1900s commercial fishing the blue whale populations have been significantly reducing. However<span style=\" font-size:16pt;\"> </span>today their biggest threats are vessel strikes and getting stuck in fishing gear </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-style:italic; color:#ffaaff;\">Diet:</span> Primarily krill but can eat  but fish and copepods</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-style:italic; color:#ffaaff;\">Fun fact</span><span style=\" color:#ffaaff;\">: They are the largest animal ever recorded to live on earth</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-style:italic; color:#ffaaff;\">General location</span><span style=\" font-size:20pt; color:#ffaaff;\">:</span> All oceans except the Arctic. They generally migrate seasonally between winter breeding grounds which are closer to the equator and summer feeding grounds</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-style:italic; color:#ffaaff;\">Role in ecosystem</span><span style=\" font-size:20pt; font-style:italic; color:#ffffff;\">: </span><span style=\" color:#000000;\"> Whales fertilize marine ecosystems as they migrate as their fecal matter increases phytoplankton production which geneate over half of the atmospheres oxgen and 40% of all the carbon dioxide absorbed.They also capture the same amount of carbon from the atmosphere as thousands of trees in their lifetime. Which is important as it reduces the amount of greenhouse gases in the atmosphere</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-style:italic; color:#ffaaff;\">Life span: </span><span style=\" color:#000000;\">Blue whales live on average around 80-90 years </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-style:italic; color:#ffaaff;\">Description</span><span style=\" color:#000000;\">: Long body(24m) and generally slender shape with mottled blue-gray colouring that appears light blue under water.A wide head and 80-90 long groves lengthwise down the throat and chest its mouth contains up to 800 plates of baleen and thick corse bristles for catching food</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://gifts.worldwildlife.org/gift-center/gifts/Species-Adoptions/Blue-Whale.aspx?sc=AWY1800OQ18317A01909RX&amp;_ga=2.222029272.1925783259.1679854196-319976745.1675645274\"><span style=\" text-decoration: underline; color:#0000ff;\">Adopt a blue whale</span></a></p></body></html>"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Information_BW = QtWidgets.QDialog()
    ui = Info_BW()
    ui.setupUi(Information_BW)
    Information_BW.show()
    sys.exit(app.exec_())
