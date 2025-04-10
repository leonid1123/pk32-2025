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
        lbl = QLabel("пуп")
        layout.addWidget(lbl, 0, 0)
        btn = QPushButton("ПУП!!!")
        layout.addWidget(btn, 1, 1)
        edit1 = QLineEdit()
        layout.addWidget(edit1,0,1)
        edit2 = QLineEdit()
        layout.addWidget(edit2,0,2)
        # show the window
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # create the main window
    window = MainWindow()
    # start the event loop
    sys.exit(app.exec())
