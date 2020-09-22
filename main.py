#!/usr/bin/env python3.8
# Interesting information on how PyQT designer works https://stackoverflow.com/questions/52480526/pyqt-appropriate-function-for-back-button-for-previous-gui-frame
import random
import sys
import types

import pinyin.cedict
import pynlpir
pynlpir.open()
from ui import Ui_MainWindow

import PyQt5
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QTextEdit

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, *args, obj=None, **kwargs):
        # Initialize UI/UX
        super().__init__()
        self.setupUi(self)
        self.show()
        self.readerQuery.setPlaceholderText("Write or paste your Chinese text here")
        self.dictQuery.setPlaceholderText("Enter hanzi")
        self.dictQuery.setFocusPolicy(Qt.StrongFocus)
        self.dictQuery.setFocus()
        self.dictEntry.hide()

        # Connect
        self.dictQuery.returnPressed.connect(self.get_translation)
        self.goBackResultsButton.clicked.connect(self.show_results)
        self.textBrowserHanzi.selectionChanged.connect(self.get_selected_translation)
        self.dictResults.itemDoubleClicked.connect(self.show_dict_entry)


        # Change pages
        self.pushButtonDictionary.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.pushButtonReader.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))

    def _sort_translations(self, t):
        """Sort the translations based on the longest phrase."""
        if t:
            t = list(t)
            t.sort(key=lambda x: -len(x[0]))
        return t

    def show_dict_entry(self, item):
        """
        Populate the dictEntry widget with the clicked item's content.
        Show the widget and hide the dictResults.
        """
        self.dictEntry.show()
        self.dictResults.hide()
        print(item.text())
        self.phraseLabel.setText('This is an example text')

    def show_results(self):
        """Go back to the dictionary results."""
        self.dictEntry.hide()
        self.dictResults.show()

    def get_translation(self):
        """Gets the translation for the phrase entered in the dictionary query."""
        # Clear previous results
        self.dictResults.clear()
        query = self.dictQuery.text()

        translations = self._sort_translations(pinyin.cedict.all_phrase_translations(query))
        if translations == []:
            self.dictResults.addItem(QListWidgetItem("No translations found."))
        else:
            for i, phrase in enumerate(translations):
                line = f'{phrase[0]} ({phrase[1][1]}): '
                for t in phrase[1][0]:
                    line += f'{t}; '
                self.dictResults.addItem(QListWidgetItem(line))

    def get_selected_translation(self):
        """Gets the translation for the phrase highlighted in the readerTextBrowser."""
        # Clear previous results
        self.listWidgetReader.clear()

        # Get selected text
        selected_text = self.textBrowserHanzi.textCursor().selectedText()

        # Get translation for the segmented text
        for phrase, _ in pynlpir.segment(selected_text):
            translations = self._sort_translations(pinyin.cedict.all_phrase_translations(phrase))
            if translations is []:
                self.listWidgetReader.addItem(QListWidgetItem("No translations found."))
            else:
                for i, phrase in enumerate(translations):
                    line = f'{phrase[0]} ({phrase[1][1]}): '
                    for t in phrase[1][0]:
                        line += f'{t}; '
                    self.listWidgetReader.addItem(QListWidgetItem(line))

def hz2py_cedict(s):
    """
    Uses the cedict dictionary to translate characters to pinyin.
    Returns pinyin if s is a phrase in cedict. Otherwise return s.
    """
    try:
        py = pinyin.cedict.translate_word(s)[1]
        return py
    except TypeError:
        return s


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
pinyin.cedict.init()  # Initialize the pinyin cedict to load data
