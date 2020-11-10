import sys
from PyQt5.Qt import *
from PyQt5 import QtWidgets
app = QApplication(sys.argv)

window2 = QtWidgets.QMainWindow()
window2.resize(1000,800)
window2.setCursor(QCursor(QPixmap('./icon/up.png')))

c2_label = QLabel(window2)
c2_label.setText('标签控件')
c2_label.resize(100, 100)
c2_label.setStyleSheet('background-color:red;')
my_cursor = QCursor(QPixmap('./icon/down.png'))
c2_label.setCursor(my_cursor)


window2.show()
sys.exit(app.exec_())
