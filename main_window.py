import sys
from PyQt5 import QtWidgets, QtGui, QtCore


def window():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    l1 = QtWidgets.QLabel(w)
    l1.setText('Option 1')
    l1.move(300, 100)
    l2 = QtWidgets.QLabel(w)
    l2.setText('keychain')
    pixmap = QtGui.QPixmap('./images/key.png')
    pixmap_scaled = pixmap.scaled(128, 128, QtCore.Qt.KeepAspectRatio)
    l2.setPixmap(pixmap_scaled)
    l2.move(600, 20)
    b = QtWidgets.QPushButton(w)
    b.setText('add records')
    b.move(20, 560)
    # h_box = QtWidgets.QHBoxLayout()
    # h_box.addStretch()
    # h_box.addWidget(l1)
    # h_box.addStretch()
    v_box = QtWidgets.QVBoxLayout()
    v_box.addWidget(b)
    # v_box.addWidget(h_box)
    w.setLayout(v_box)
    w.show()
    w.setWindowTitle('pass app')
    w.setGeometry(1600, 200, 800, 600)
    sys.exit(app.exec_())


window()
