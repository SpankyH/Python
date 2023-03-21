############ PYQT5 ############
#### МОДУЛИ
# QT - Обьединяет все модули
# QTcore - неграфические классы
# QTWidgets - Виджеты
# QT gui - компоненты графф интерф
# QTnetwork - сетевые классы
# QTmultimedia
# QT SQL - базы данных

#### ВИДЖЕТЫ
# QlineEdit - Поле ввода
# QradioButton - Кружочки
# Qcombobox - выпадающее меню
# QcheckBox - галочка
# QmenuBar - горизонтальная строка меню
# QtoolBar - горизонтальные паннели
# Qtab - разбивка страницы
# QscrolBar - прокрутка
# Qsplitter - разделители
# Qdock - подокна

# QboxLayout - Расположение (V H)
# QGridLayout




############ ПРИМЕРЫ ############
# import sys
# from PyQt5.QtWidgets import QApplication, QWidget
# if __name__ == "___main___":
#     app = QApplication(sys.argv)
#     w = QWidget()
#     w.resize(350, 350)
#     w.setWindowTitle("HELLO !!!!!!")
#     w.show()
#     sys.exit(app.exec_())
####
# import sys
# from PyQt5.QtWidgets import *
# if __name__ == "__main__":
#     app = QApplication([])
#     w = QWidget()
#     w.setWindowTitle("QboxLayout")
#     btn1 = QPushButton("AAAA")
#     btn2 = QPushButton("SSSS")
#     btn3 = QPushButton("DDDD")

#     hbox = QVBoxLayout(w)

#     hbox.addWidget(btn1)
#     hbox.addWidget(btn2)
#     hbox.addWidget(btn3)

#     w.show()
#     sys.exit(app.exec_())
####
# import sys
# from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import *
# from PyQt5.QtGui import QPalette
# if __name__ == "__main__":
#     app = QApplication([])
#     app.setStyle("Fusion")

#     qp = QPalette()
#     qp.setColor(QPalette.ButtonText, Qt.black)
#     qp.setColor(QPalette.Window, Qt.black)
#     app.setPalette(qp)

#     w = QWidget()
#     grid = QGridLayout(w)

#     for i in range(3):
#         for j in range(3):
#             grid.addWidget(QPushButton("Button"), i, j)
#     w.show()
#     sys.exit(app.exec_())
    
