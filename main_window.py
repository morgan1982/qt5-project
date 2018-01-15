import sys
from PyQt5.QtWidgets import (
    QLineEdit, QSlider, QPushButton, QVBoxLayout, QApplication, QWidget, QLabel, QHBoxLayout
)
from PyQt5.QtCore import Qt
from PyQt5 import QtGui


class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.b = QPushButton('add records')
        self.l = QLabel('Keychain')
        self.l2 = QLabel('logo')
        self.pixmap = QtGui.QPixmap('./images/key.png')
        pix_map_scaled = self.pixmap.scaled(128, 128, Qt.KeepAspectRatio)
        self.l2.setPixmap(pix_map_scaled)

        # input
        self.line_edit = QLineEdit()

        # buttons
        self.btn_print = QPushButton('print')
        self.btn_clear = QPushButton('clear')

        # slider
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(1)
        self.slider.setMaximum(99)
        self.slider.setValue(25)
        self.slider.setTickInterval(5)
        self.slider.setTickPosition(QSlider.TicksBelow)

        h_box3 = QHBoxLayout()
        h_box3.addSpacing(400)
        h_box3.addWidget(self.b)

        h_box2 = QHBoxLayout()
        h_box2.addSpacing(150)
        h_box2.addWidget(self.btn_print)
        h_box2.addSpacing(30)
        h_box2.addWidget(self.btn_clear)
        h_box2.addSpacing(10)

        h_box = QHBoxLayout()
        h_box.addStretch()
        h_box.addWidget(self.l)
        h_box.addStretch()
        h_box.addWidget(self.line_edit)

        v_box = QVBoxLayout()
        v_box.addLayout(h_box3)
        v_box.addWidget(self.slider)
        v_box.addWidget(self.l2)
        v_box.addLayout(h_box)
        v_box.addLayout(h_box2)

        self.setLayout(v_box)
        self.setWindowTitle('keychain')

        self.b.clicked.connect(self.add_record)
        self.btn_print.clicked.connect(self.btn_clicked)
        self.btn_clear.clicked.connect(self.btn_clicked)
        self.setWindowTitle('keychain')
        self.setGeometry(1600, 700, 600, 500)

        self.show()

    def add_record(self):
        self.l.setText('record added')
        print('oooo')

    def btn_clicked(self):
        sender = self.sender()
        if sender.text() == 'print':
            print(self.line_edit.text())
        else:
            self.line_edit.clear()


app = QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())
