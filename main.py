import sys
from PyQt6.QtWidgets import QApplication, \
    QWidget, QGridLayout, QLabel, QPushButton, QLineEdit
from qt_material import apply_stylesheet


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setGeometry(100, 100, 500, 300)
        self.setWindowTitle('Hello World')
        apply_stylesheet(app, theme='light_blue.xml')
        layout = QGridLayout()
        self.setLayout(layout)
        self.lbl = QLabel("пуп")
        layout.addWidget(self.lbl, 0, 0)
        btn = QPushButton("ПУП!!!", )
        btn.clicked.connect(self.my_slot)
        layout.addWidget(btn, 1, 1)
        self.edit1 = QLineEdit()
        layout.addWidget(self.edit1, 0, 1)
        self.edit2 = QLineEdit()
        layout.addWidget(self.edit2, 0, 2)
        # show the window
        self.show()

    def my_slot(self):
        print("ОЙ!!!")
        str1 = self.edit1.text()
        str2 = self.edit2.text()
        self.lbl.setText(str1 + str2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # create the main window
    window = MainWindow()
    # start the event loop
    sys.exit(app.exec())
