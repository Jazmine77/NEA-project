# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\neals\Documents\computer science\NEA-project\Humpback whale.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Info_hump(object):
    def setupUi(self, Info_hump):
        Info_hump.setObjectName("Info_hump")
        Info_hump.resize(770, 599)
        Info_hump.setStyleSheet("font: 18pt \"Palatino Linotype\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(77, 98, 175);")
        self.title = QtWidgets.QLabel(Info_hump)
        self.title.setGeometry(QtCore.QRect(230, 20, 271, 31))
        self.title.setStyleSheet("\n"
"font: 24pt \"Palatino Linotype\";\n"
"text-decoration: underline;\n"
"color: rgb(255, 170, 255);\n"
"")
        self.title.setObjectName("title")
        self.info_box = QtWidgets.QTextBrowser(Info_hump)
        self.info_box.setGeometry(QtCore.QRect(10, 70, 751, 341))
        self.info_box.setStyleSheet("")
        self.info_box.setObjectName("info_box")
        self.photo = QtWidgets.QLabel(Info_hump)
        self.photo.setGeometry(QtCore.QRect(10, 420, 351, 181))
        self.photo.setText("")
        self.photo.setPixmap(QtGui.QPixmap("C:\\Users\\neals\\Documents\\computer science\\NEA-project\\hbw.png"))
        self.photo.setScaledContents(True)
        self.photo.setObjectName("photo")

        self.retranslateUi(Info_hump)
        QtCore.QMetaObject.connectSlotsByName(Info_hump)

    def retranslateUi(self, Info_hump):
        _translate = QtCore.QCoreApplication.translate
        Info_hump.setWindowTitle(_translate("Info_hump", "Information"))
        self.title.setText(_translate("Info_hump", "Humpback Whales"))
        self.info_box.setHtml(_translate("Info_hump", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Palatino Linotype\'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-style:italic; color:#ffaaff;\">Population</span><span style=\" font-size:14pt;\">:</span> around 135,000</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-style:italic; color:#ffaaff;\">Fun fact</span><span style=\" font-size:20pt; color:#ffaaff;\">: longest migrations of any mammal some swimming 5,000 miles (8,047 km) </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-style:italic; color:#ffaaff;\">Dangers</span>: Populations reduced by more then 95% due to commercial fishing but now the main threats are entanglement in gear, vessel strikes and underwater noise</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-style:italic; color:#ffaaff;\">Diet:</span> During warmer months humpback whales spend alot of time feeding and building blubber(fat stores) to sustain them in cooler months.  They are eat mostly small crustaceans(krill ) and small fish<span style=\" font-family:\'Open Sans\',\'sans-serif\'; font-size:16px; color:#000000; background-color:#ffffff;\"> </span><span style=\" color:#ffaaff;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-style:italic; color:#ffaaff;\">General location</span><span style=\" font-size:20pt; color:#ffaaff;\">: </span><span style=\" color:#000000;\">Travel great distances between high lattitude summer feeding grounds( in cold productive waters)  and winter mating grounds in tropical areas. When in winter for calving season they prefer shallow, warm waters near offshore reef systems or shores.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-style:italic; color:#ffaaff;\">Role in ecosystem :</span><span style=\" color:#000000;\">They are at the top of the ecosystem and play an important role have an important role in overall health of the marine environment.Each whale sequesters 30 tons of CO2 on aveage taking that carbon out of the atmosphere for centuries.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-style:italic; color:#ffaaff;\">Life span: </span><span style=\" color:#000000;\"> 80-90 years </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-style:italic; color:#ffaaff;\">Description</span><span style=\" color:#000000;\">: Bodies are primarily black but individuals have varying amount of white markings on their pectoral fins,bellies and tails They can grow up to 16 metres in length and have 30 broad ventral grooves on throat and chest.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://uk.whales.org/support/adopt/humpback/\"><span style=\" text-decoration: underline; color:#0000ff;\">Adopt a humpback whale</span></a></p></body></html>"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Info_hump = QtWidgets.QDialog()
    ui = Info_hump()
    ui.setupUi(Info_hump)
    Info_hump.show()
    sys.exit(app.exec_())
