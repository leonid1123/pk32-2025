import sys
from PyQt6.QtWidgets import QApplication, \
    QWidget, QGridLayout, QLabel, QPushButton, QLineEdit, QListWidget, QMessageBox
from qt_material import apply_stylesheet
import pymysql.cursors


class Student:
    def __init__(self,_name,_fam,_otch,_dr,_tel,_id):
        self.name = _name
        self.fam = _fam
        self.otch = _otch
        self.dr = _dr
        self.tel = _tel
        self.id = _id


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.students = []
        self.setGeometry(100, 100, 500, 600)
        self.setWindowTitle('Студенческий отдел кадров')
        apply_stylesheet(app, theme='light_blue.xml')
        layout = QGridLayout()
        self.setLayout(layout)
        self.student_view = QListWidget()
        self.student_view.currentItemChanged.connect(self.list_item_change)
        self.fam_entry = QLineEdit()
        self.name_entry = QLineEdit()
        self.otchestvo_entry = QLineEdit()
        self.phone_entry = QLineEdit()
        self.data_rozhdeniya_entry = QLineEdit()
        self.add_button = QPushButton("Добавить")
        self.add_button.clicked.connect(self.add_student)
        self.edit_button = QPushButton("Изменить")
        self.edit_button.clicked.connect(self.change_student)

        layout.addWidget(self.student_view, 0, 0, 4, 0)
        layout.addWidget(self.fam_entry, 1, 1)
        layout.addWidget(self.name_entry, 1, 3)
        layout.addWidget(self.otchestvo_entry, 2, 1)
        layout.addWidget(self.data_rozhdeniya_entry, 2, 3)
        layout.addWidget(self.phone_entry, 3, 1)
        layout.addWidget(self.add_button, 3, 2, 1, 2)
        layout.addWidget(self.edit_button, 4, 0, 1, 2)

        layout.addWidget(QLabel("Фамилия"), 1, 0)
        layout.addWidget(QLabel("Имя"), 1, 2)
        layout.addWidget(QLabel("Отчество"), 2, 0)
        layout.addWidget(QLabel("Дата рождения"), 2, 2)
        layout.addWidget(QLabel("Телефон"), 3, 0)

        self.cnx = pymysql.connect(
            host="localhost",
            user="pk32",
            password="1234",
            database="stud_otdel")
        self.cur = self.cnx.cursor()
        self.get_all_students()
        # show the window
        self.show()

    def get_all_students(self):
        sql = "SELECT * FROM students"
        self.cur.execute(sql)
        ans = self.cur.fetchall()
        for item in ans:
            st = Student(item[1],item[2],item[3],item[4],item[5],item[0])
            self.students.append(st)
            self.student_view.addItem(
                f"{item[1]}, {item[2]}, {item[3]}, {item[4]}")

    def add_student(self):
        """добавление студентов в базу"""
        name = self.name_entry.text()
        fam = self.fam_entry.text()
        otch = self.otchestvo_entry.text()
        dr = self.data_rozhdeniya_entry.text()
        phone = self.phone_entry.text()
        self.student_view.clear()
        if name and fam and otch and dr and phone:
            sql = """INSERT INTO 
            students(imya, familiya, 
            otchestvo, data_rozhdeniya, telephone)
             VALUES(%s,%s,%s,%s,%s)"""
            params = (name, fam, otch, dr, phone)
            self.cur.execute(sql, params)
            self.cnx.commit()
            self.get_all_students()
        else:
            QMessageBox.warning(self, "Внимание!", "Поля должны быть заполнены!")

    def change_student(self):
        """метод для изменения информации о студенте"""
        x = self.student_view.currentRow()
        id = self.students[x].id
        #перенести в другой метод
        self.name_entry.clear()
        self.name_entry.insert(self.students[x].name)

    def list_item_change(self):
        """метод для определения выбранного студента.
        Вызывается при изменении пункта списка"""
        print("pup")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # create the main window
    window = MainWindow()
    # start the event loop
    sys.exit(app.exec())
