import sys
from PyQt5 import QtWidgets


def window():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    l1 = QtWidgets.QLabel(w)
    l1.setText('Option 1')
    l1.move(300, 100)
    w.show()
    w.setWindowTitle('pass app')
    w.setGeometry(1600, 200, 800, 600)
    sys.exit(app.exec_())


window()
