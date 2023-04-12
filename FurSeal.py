# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\neals\Documents\computer science\NEA-project\Northern fur seal.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Info_fur(object):
    def setupUi(self, information_Fur):
        information_Fur.setObjectName("information_Fur")
        information_Fur.resize(770, 599)
        information_Fur.setStyleSheet("background-color: rgb(77, 98, 175);\n"
"color: rgb(0, 0, 0);\n"
"font: 18pt \"Palatino Linotype\";")
        self.title = QtWidgets.QLabel(information_Fur)
        self.title.setGeometry(QtCore.QRect(270, 20, 261, 31))
        self.title.setStyleSheet("\n"
"font: 24pt \"Palatino Linotype\";\n"
"text-decoration: underline;\n"
"color: rgb(255, 170, 255);\n"
"")
        self.title.setObjectName("title")
        self.photo = QtWidgets.QLabel(information_Fur)
        self.photo.setGeometry(QtCore.QRect(20, 400, 361, 191))
        self.photo.setText("")
        self.photo.setPixmap(QtGui.QPixmap("C:\\Users\\neals\\Documents\\computer science\\NEA-project\\northern-fur-seal.png"))
        self.photo.setScaledContents(True)
        self.photo.setObjectName("photo")
        self.info_box = QtWidgets.QTextBrowser(information_Fur)
        self.info_box.setGeometry(QtCore.QRect(20, 60, 751, 341))
        self.info_box.setObjectName("info_box")

        self.retranslateUi(information_Fur)
        QtCore.QMetaObject.connectSlotsByName(information_Fur)

    def retranslateUi(self, information_Fur):
        _translate = QtCore.QCoreApplication.translate
        information_Fur.setWindowTitle(_translate("information_Fur", "Information"))
        self.title.setText(_translate("information_Fur", "Northern Fur Seal"))
        self.info_box.setHtml(_translate("information_Fur", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Palatino Linotype\'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-style:italic; color:#ffaaff;\">Population</span><span style=\" color:#000000;\">: About 1.1 million (they listed as vulnerbale under the U.S Endangered Species Act due to a decrease in pup production)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-style:italic; color:#ffaaff;\">Fun fact: </span><span style=\" color:#ffaaff;\">They have external ears</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-style:italic; color:#ffaaff;\">Dangers: </span><span style=\" color:#000000;\">Predation by killer whales, competition with fishereis and climate change</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-style:italic; color:#ffaaff;\">Diet</span><span style=\" font-size:20pt; font-style:italic; color:#000000;\">: </span><span style=\" color:#000000;\">They eat a wide range of midwater fish and squid species.Walleye pollock is thier predominant preyand and examples of their primary prey include Pacific sand lance, Pacific herring and Atka mackerel.Their diet vary on whats available to them in the geographic area and time of year</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-style:italic; color:#ffaaff;\">Fun fact: N</span><span style=\" color:#ffaaff;\">orthern fur seals spend more then 300 days at sea</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-style:italic; color:#ffaaff;\">General location</span><span style=\" color:#000000;\">:In the open ocean and rocky or sandy beaches like in the Pribilof islands for resting and breeding. In winter and spring they occupy the North Pacific ocean as well as Bering and Okhotsk seas</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-style:italic; color:#ffaaff;\">Role in ecosystem</span><span style=\" color:#000000;\">:Help to maintain a balanced food web where they are a food source for larger predators like orcas and consume fish, squid and crustaceans</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-style:italic; color:#ffaaff;\">Life span</span><span style=\" color:#000000;\">: 18 years for males and 27 for females</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-style:italic; color:#ffaaff;\">Description</span><span style=\" color:#000000;\">: Have a stocky body,small head and very short snout.Their fur is extremely dense(46,500 fibres/cm2) to help maintain their body temperature in the cold water. Their flippers are the longest in the Otariidae family .Adult males are dark brown to black and adult females are dark gray to brown on their backs and light grey on their front.Adult males are</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-style:italic; color:#ffaaff;\">fun fact:</span><span style=\" font-size:20pt; color:#ffaaff;\">Due to their dtrong fore flippers they can outrun a human on slippery rocks and nearly climb vertical cliffs</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    information_Fur = QtWidgets.QDialog()
    ui = Info_fur()
    ui.setupUi(information_Fur)
    information_Fur.show()
    sys.exit(app.exec_())