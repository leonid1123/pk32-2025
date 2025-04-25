import sys
from PyQt6.QtWidgets import QApplication, QWidget, \
    QGridLayout, QListWidget, QLineEdit, \
    QPushButton, QMessageBox, QVBoxLayout, QLabel
from PyQt6.QtCore import QTimer
import pymysql.cursors


class LogIn(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('Авторизация')
        layout = QVBoxLayout()
        self.setLayout(layout)
        layout.addWidget(QLabel("Логин"))
        self.login_entry = QLineEdit()
        layout.addWidget(self.login_entry)
        layout.addWidget(QLabel("Пароль"))
        self.pass_entry = QLineEdit()
        layout.addWidget(self.pass_entry)
        self.login_btn = QPushButton("ВХОД")
        layout.addWidget(self.login_btn)
        self.reg_button = QPushButton("регистрация")
        layout.addWidget(self.reg_button)
        self.show()


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('Убийца телеги')
        layout = QGridLayout()
        self.setLayout(layout)
        self.msg_view = QListWidget()
        self.msg_entry = QLineEdit()
        send_btn = QPushButton("Отправить")
        send_btn.clicked.connect(self.send_msg)

        layout.addWidget(self.msg_view, 0, 0, 1, 2)
        layout.addWidget(self.msg_entry, 1, 0)
        layout.addWidget(send_btn, 1, 1)

        self.db_connect()
        self.get_msg()
        self.show()

    def db_connect(self):
        try:
            self.cnx = pymysql.connect(host="192.168.1.61",
                                       user="pk32",
                                       password="1234",
                                       database="pk32msg",
                                       cursorclass=pymysql.cursors.DictCursor)
            self.cur = self.cnx.cursor()
        except pymysql.Error as e:
            QMessageBox.critical(self,
                                 "Ошибка БД",
                                 f"Ошибка:{e}")
            self.cnx = None
            self.cur = None

    def send_msg(self):
        msg = self.msg_entry.text().strip()
        if msg and self.cnx:
            sql = """INSERT INTO msg(text) VALUES(%s)"""
            self.cur.execute(sql, (msg,))
            self.cnx.commit()
            self.msg_entry.clear()

    def get_msg(self):
        if self.cnx:
            self.msg_view.clear()
            self.cur.execute("SELECT text FROM msg")
            self.cnx.commit()
            ans = self.cur.fetchall()
            for item in ans:
                self.msg_view.addItem(item['text'])
            self.msg_view.scrollToBottom()
            QTimer.singleShot(500, self.get_msg)

    def keyPressEvent(self, event):
        # Check if the Enter key is pressed
        if event.key() == 16777220:  # Qt.Key_Return
            self.send_msg()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LogIn()
    sys.exit(app.exec())
