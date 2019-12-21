import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QTableWidgetItem, QApplication, QMainWindow


class COFFEE(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.run()

    def run(self):
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()
        result = cur.execute("""SELECT * FROM coffee""").fetchall()
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(
            ['ID', 'название сорта', 'степень обжарки', 'молотый/в зернах', 'описание вкуса', 'цена', 'объем упаковки'])
        row_id = 0
        for good in result:
            self.table.insertRow(row_id)
            self.table.setItem(row_id, 0, QTableWidgetItem(str(good[0])))
            self.table.setItem(row_id, 1, QTableWidgetItem(str(good[1])))
            self.table.setItem(row_id, 2, QTableWidgetItem(str(good[2])))
            self.table.setItem(row_id, 3, QTableWidgetItem(str(good[3])))
            self.table.setItem(row_id, 4, QTableWidgetItem(str(good[4])))
            self.table.setItem(row_id, 5, QTableWidgetItem(str(good[5])))
            self.table.setItem(row_id, 6, QTableWidgetItem(str(good[6])))
            row_id += 1
        con.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = COFFEE()
    wnd.show()
    sys.exit(app.exec())