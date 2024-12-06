import sqlite3
import sys
import sqlite3
from PyQt6 import uic
from random import randint
from PyQt6.QtGui import QColor, QStandardItem, QStandardItemModel
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMainWindow
con = sqlite3.connect('coffee.sqlite')
cur = con.cursor()
model = QStandardItemModel()

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.listView.setModel(model)
        self.write()

    def write(self):
        req = cur.execute('SELECT * FROM coffee ').fetchall()
        print(req)
        for i in req:
            item = QStandardItem(str(i))
            model.appendRow(item)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())

