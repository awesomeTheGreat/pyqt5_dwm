from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
import os
import urllib.request as req

from PyQt5.uic import loadUiType

ui, _ = loadUiType('main.ui')


class MainApp(QMainWindow, ui):
    def __init__(self, parent=None) -> None:
        super(MainApp, self).__init__(parent=parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.init_ui()
        self.handle_button()

    def init_ui(self):
        pass

    def handle_button(self):
        self.pushButton.clicked.connect(lambda: self.download(
            url=self.lineEdit.text(),
            path=self.lineEdit_2.text()
        ))
        self.pushButton_2.clicked.connect(lambda: self.handle_browse())

    def handle_progress(self, block_num, block_size, total_size):
        read_data = block_num*block_size

        if total_size > 0:
            download_percentage = (read_data * 100) / total_size
            self.progressBar.setValue(download_percentage)
            QApplication.processEvents()

    def handle_browse(self):
        save_location = QFileDialog.getSaveFileName(
            self, caption="Save as", directory=".", filter="All Files(*.*)")
        self.lineEdit_2.setText(str(save_location[0]))

    def download(self, url, path):
        req.urlretrieve(url, path, self.handle_progress)


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
