import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QTableWidgetItem, QApplication, QMainWindow, QWidget


class COFFEE(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.run()

    def run(self):
        self.table.setColumnCount(0)
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


class COFFEE_add(QWidget):
    def __init__(self, wnd):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.wnd = wnd
        self.pb.clicked.connect(self.run)

    def run(self):
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()
        result = cur.execute("""SELECT * FROM coffee""").fetchall()
        print(result)
        ID = self.id.value()
        sort = self.sort.text()
        step = self.step.value()
        type_coffee = self.type.text()
        description = self.description.text()
        price = self.price.value()
        volume = self.volume.value()
        a = (ID, sort, step, type_coffee, description, price, volume)
        b = ('ID', 'variety', 'roasting_degree', 'type', 'description', 'price', 'volume_l')
        if ID == 0:
            cur.execute("""INSERT INTO coffee(variety, roasting_degree, type, description, price, volume_l) VALUES"""
                        + str(a[1:]))
        elif ID in map(lambda x: x[0], result):
            que = 'UPDATE coffee SET '
            for i in range(1, len(a[1:])):
                que += "{} = '{}',\n".format(b[i], a[i])
            cur.execute(que[:-2] + """ WHERE ID = """ + str(a[0]))
        else:
            cur.execute(
                """INSERT INTO coffee(ID, variety, roasting_degree, type, description, price, volume_l) VALUES"""
                + str(a))
        con.commit()
        self.wnd.run()
        con.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = COFFEE()
    wnd2 = COFFEE_add(wnd)
    wnd2.show()
    wnd.show()
    sys.exit(app.exec())
