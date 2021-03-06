# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dict.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(912, 750)
        MainWindow.setStyleSheet(".QWidget {\n"
"    background: white;\n"
"}\n"
"#centralwidget {\n"
"    background: rgb(248, 248, 248);\n"
"}\n"
"\n"
"* {\n"
"    font-size: 18px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButtonReader = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonReader.setGeometry(QtCore.QRect(150, 10, 111, 31))
        self.pushButtonReader.setObjectName("pushButtonReader")
        self.pushButtonDictionary = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonDictionary.setGeometry(QtCore.QRect(20, 10, 111, 31))
        self.pushButtonDictionary.setObjectName("pushButtonDictionary")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(20, 60, 871, 671))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.dictionary = QtWidgets.QWidget(self.page)
        self.dictionary.setGeometry(QtCore.QRect(0, 0, 871, 681))
        self.dictionary.setObjectName("dictionary")
        self.dictQuery = QtWidgets.QLineEdit(self.dictionary)
        self.dictQuery.setGeometry(QtCore.QRect(30, 30, 811, 31))
        self.dictQuery.setText("")
        self.dictQuery.setObjectName("dictQuery")
        self.dictResults = QtWidgets.QListWidget(self.dictionary)
        self.dictResults.setGeometry(QtCore.QRect(30, 120, 811, 521))
        self.dictResults.setStyleSheet("::item {\n"
"}")
        self.dictResults.setObjectName("dictResults")
        self.dictEntry = QtWidgets.QWidget(self.dictionary)
        self.dictEntry.setGeometry(QtCore.QRect(30, 80, 811, 581))
        self.dictEntry.setObjectName("dictEntry")
        self.phraseLabel = QtWidgets.QLabel(self.dictEntry)
        self.phraseLabel.setGeometry(QtCore.QRect(0, 0, 341, 21))
        self.phraseLabel.setObjectName("phraseLabel")
        self.examplesLabel = QtWidgets.QLabel(self.dictEntry)
        self.examplesLabel.setGeometry(QtCore.QRect(0, 290, 91, 21))
        self.examplesLabel.setObjectName("examplesLabel")
        self.examplesBrowser = QtWidgets.QTextBrowser(self.dictEntry)
        self.examplesBrowser.setGeometry(QtCore.QRect(0, 320, 811, 261))
        self.examplesBrowser.setObjectName("examplesBrowser")
        self.phraseBrowser = QtWidgets.QTextBrowser(self.dictEntry)
        self.phraseBrowser.setGeometry(QtCore.QRect(0, 40, 811, 231))
        self.phraseBrowser.setObjectName("phraseBrowser")
        self.goBackResultsButton = QtWidgets.QPushButton(self.dictEntry)
        self.goBackResultsButton.setGeometry(QtCore.QRect(620, 0, 191, 31))
        self.goBackResultsButton.setObjectName("goBackResultsButton")
        self.dictResultsLabel = QtWidgets.QLabel(self.dictionary)
        self.dictResultsLabel.setGeometry(QtCore.QRect(30, 80, 121, 23))
        self.dictResultsLabel.setObjectName("dictResultsLabel")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.reader = QtWidgets.QWidget(self.page_2)
        self.reader.setGeometry(QtCore.QRect(0, 0, 871, 681))
        self.reader.setObjectName("reader")
        self.readerQuery = QtWidgets.QLineEdit(self.reader)
        self.readerQuery.setGeometry(QtCore.QRect(30, 30, 811, 31))
        self.readerQuery.setText("")
        self.readerQuery.setObjectName("readerQuery")
        self.textBrowserHanzi = QtWidgets.QTextBrowser(self.reader)
        self.textBrowserHanzi.setGeometry(QtCore.QRect(30, 120, 811, 351))
        self.textBrowserHanzi.setObjectName("textBrowserHanzi")
        self.listWidgetReader = QtWidgets.QListWidget(self.reader)
        self.listWidgetReader.setGeometry(QtCore.QRect(30, 520, 811, 141))
        self.listWidgetReader.setObjectName("listWidgetReader")
        self.label = QtWidgets.QLabel(self.reader)
        self.label.setGeometry(QtCore.QRect(30, 80, 481, 23))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.reader)
        self.label_2.setGeometry(QtCore.QRect(30, 490, 481, 23))
        self.label_2.setObjectName("label_2")
        self.stackedWidget.addWidget(self.page_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButtonReader.setText(_translate("MainWindow", "Reader"))
        self.pushButtonDictionary.setText(_translate("MainWindow", "Dictionary"))
        self.phraseLabel.setText(_translate("MainWindow", "Phrase"))
        self.examplesLabel.setText(_translate("MainWindow", "Examples"))
        self.goBackResultsButton.setText(_translate("MainWindow", "Go back to results"))
        self.dictResultsLabel.setText(_translate("MainWindow", "Search results"))
        self.label.setText(_translate("MainWindow", "Text Browser (highlight to show translations and pinyin)"))
        self.label_2.setText(_translate("MainWindow", "Highlight results"))
