import sys
from PyQt6.QtWidgets import QApplication, QWidget, QListWidget, QVBoxLayout, QListWidgetItem, QLabel, QComboBox, \
    QLineEdit, QPushButton
import pymysql.cursors

#https://ctxt.io/2/AAB4kwukFg
class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print("Подключение к БД...")
        self.cnx = pymysql.connect(host="localhost",
                         user="pk32",
                         password="1234",
                         database='water_shop')
        print("Подключение успешно.")
        # set the window title
        self.setWindowTitle('Магазин Ромашка')
        self.tovari_view = QListWidget()
        pos_label = QLabel("Позиция:")
        self.pos_entry = QComboBox()
        self.get_table_fields()
        #SHOW COLUMNS FROM my_table;
        znak_label = QLabel("Знак:")
        self.znak_entry = QComboBox()
        self.znak_entry.addItems([">","<","="])
        chiselka_label = QLabel("чиселка/буковка:")
        self.chiselka_entry = QLineEdit()
        self.btn = QPushButton("ТЫК!")

        layout = QVBoxLayout()
        layout.addWidget(self.tovari_view)
        layout.addWidget(pos_label)
        layout.addWidget(self.pos_entry)
        layout.addWidget(znak_label)
        layout.addWidget(self.znak_entry)
        layout.addWidget(chiselka_label)
        layout.addWidget(self.chiselka_entry)
        layout.addWidget(self.btn)
        self.setLayout(layout)
        # show the window
        self.select_sklad()
        self.show()

    def select_sklad(self):
        cursor = self.cnx.cursor()
        cursor.execute("SELECT * from sklad WHERE quantity < 5")
        ans = cursor.fetchall()
        for item in ans:
            tmp = f"{item[1]}, {item[2]}, {item[3]}, {item[4]}"
            qtmp = QListWidgetItem(tmp)
            self.tovari_view.addItem(qtmp)

    def get_table_fields(self):
        cursor = self.cnx.cursor()
        cursor.execute("SHOW COLUMNS FROM sklad")
        ans = cursor.fetchall()
        print(ans)
        for item in ans:
            print(item[0])
            self.pos_entry.addItem(item[0])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
