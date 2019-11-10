import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget, QApplication


class P1Main(QMainWindow):  # Меню - окно с выбором
    def __init__(self):
        super(P1Main, self).__init__()
        uic.loadUi('Интерфейсы\P1Main.ui', self)
        self.initUI()

    def initUI(self):  # Метод отвечающий за нажатие кнопок
        self.E1R.clicked.connect(self.run)
        self.E2R.clicked.connect(self.run2)

    def run(self):  # Открывает окно с переводчиком
        self.B1 = P1B1()
        self.B1.show()

    def run2(self):  # Открывает окно с калькулятором
        self.B2 = P1B2()
        self.B2.show()


class P1B1(QWidget):  # Окно с переводчиком С.С.
    def __init__(self):
        super(P1B1, self).__init__()
        uic.loadUi('Интерфейсы\P1B1.ui', self)
        self.initUI()

    def initUI(self):  # Метод отвечающий за нажатие кнопок
        self.pushButton.clicked.connect(self.shat)
        self.E1B.clicked.connect(self.run)

    def run(self):  # Открывает окно меню
        self.B0 = P1Main()
        self.B0.show()

    def shat(self):
        t0 = ['0', '1', 'Двоичная', '3', '4', '5', '6', '7', 'Восьмиричная', '9',
              'Десятиричная', '11', '12', '13', '14', '15', 'Шестнадцатиричная']
        t2 = ['0', '1']
        t8 = ['0', '1', '2', '3', '4', '5', '6', '7']
        t10 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        t16 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
        c1 = self.C1B.currentText()
        c2 = self.C2B.currentText()
        a1 = str(self.X1B.text())
        count = 0
        if count == 0:  # проверка на корректность условия
            if c1 == 'Двоичная':
                for i in str(a1):
                    if i not in t2:
                        count += 1
            if c1 == 'Восьмиричная':
                for i in a1:
                    if i not in t8:
                        count += 1
            if c1 == 'Десятиричная':
                for i in a1:
                    if i not in t10:
                        count += 1
            if c1 == 'Шестнадцатиричная':
                for i in a1:
                    if i not in t16:
                        count += 1
        if count != 0:
            self.kin1.setText(str('Некорректное условие'))
        else:
            b1 = t0.index(c1)
            b2 = int(t0.index(c2))
            a1 = str(a1)
            a2 = str(a1[::-1])
            ux1 = 0
            a3 = 0
            a4 = []
            if b1 == 16:  # перевод в десятичную С.С.
                for i in a2:
                    n = int(t16.index(i))
                    a3 += n * (b1 ** ux1)
                    ux1 += 1
            else:
                for i in a2:
                    a3 += int(i) * (b1 ** ux1)
                    ux1 += 1
            if c2 == 'Двоичная':  # Перевод кода СС по условию
                if a3 >= 2:
                    while a3 >= 2:
                        a4.append(str(a3 % 2))
                        a3 -= a3 % 2
                        a3 /= 2
                        a3 = int(a3)
                        if a3 < 2:
                            a4.append('1')
                else:
                    a4.append(str(a3))
                self.kin1.setText(str(''.join(a4[::-1])))
            if c2 == 'Восьмиричная':
                if a3 >= 8:
                    while a3 >= b2:
                        a4.append(str(a3 % b2))
                        a3 -= a3 % b2
                        a3 //= 8
                        if a3 < 8:
                            a4.append(str(a3))
                else:
                    a4.append(str(a3))
                self.kin1.setText(str(''.join(a4[::-1])))
            if c2 == 'Десятиричная':
                self.kin1.setText(str(a3))
            if c2 == 'Шестнадцатиричная':
                if a3 >= 16:
                    while a3 >= b2:
                        a4.append(str(t16[a3 % b2]))
                        a3 -= a3 % b2
                        a3 //= 16
                        if a3 < 16:
                            a4.append(str(a3))
                else:
                    a4.append(str(t16[a3]))
                self.kin1.setText(str(''.join(a4[::-1])))


class P1B2(QWidget):  # Открывает окно с калькулятором С.С.
    def __init__(self):
        super(P1B2, self).__init__()
        uic.loadUi('Интерфейсы\P1B2.ui', self)
        self.initUI()

    def initUI(self):  # Метод отвечающий за нажатие кнопок
        self.pushButton.clicked.connect(self.shat)
        self.E1B.clicked.connect(self.run)

    def run(self):  # Открывает окно меню
        self.B0 = P1Main()
        self.B0.show()

    def shat(self):
        t0 = ['0', '1', 'Двоичная', '3', '4', '5', '6', '7', 'Восьмиричная', '9',
              'Десятиричная', '11', '12', '13', '14', '15', 'Шестнадцатиричная']
        t2 = ['0', '1']
        t8 = ['0', '1', '2', '3', '4', '5', '6', '7']
        t10 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        t16 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
        c1 = self.C1B.currentText()
        c2 = self.C2B.currentText()
        c12 = self.C3B.currentText()
        a1 = str(self.X1B.text())
        az = str(self.X3B.text())
        count = 0
        if count == 0:  # проверка на корректность условия
            if c1 == 'Двоичная':
                for i in str(a1):
                    if i not in t2:
                        count += 1
            if c1 == 'Восьмиричная':
                for i in a1:
                    if i not in t8:
                        count += 1
            if c1 == 'Десятиричная':
                for i in a1:
                    if i not in t10:
                        count += 1
            if c1 == 'Шестнадцатиричная':
                for i in a1:
                    if i not in t16:
                        count += 1
            if c12 == 'Двоичная':
                for i in str(az):
                    if i not in t2:
                        count += 1
            if c12 == 'Восьмиричная':
                for i in az:
                    if i not in t8:
                        count += 1
            if c12 == 'Десятиричная':
                for i in az:
                    if i not in t10:
                        count += 1
            if c12 == 'Шестнадцатиричная':
                for i in az:
                    if i not in t16:
                        count += 1
        if count != 0:
            self.X2B.setText(str('Некорректное условие'))
        else:  # перевод в десятичную С.С.
            b1 = t0.index(c1)
            b2 = int(t0.index(c2))
            a1 = str(a1)
            a2 = a1[::-1]
            ux1 = 0
            a3 = 0
            a4 = []
            if b1 == 16:
                for i in a2:
                    n = int(t16.index(str(i)))
                    a3 += n * (b1 ** ux1)
                    ux1 += 1
            else:
                for i in a2:
                    a3 += int(i) * (b1 ** ux1)
                    ux1 += 1
            b3 = t0.index(c12)
            az = str(az)
            az2 = az[::-1]
            ux2 = 0
            az3 = 0
            if b3 == 16:
                for i in az2:
                    n = int(t16.index(str(i)))
                    az3 += n * (b3 ** ux2)
                    ux2 += 1
            else:
                for i in az2:
                    az3 += int(i) * (b3 ** ux2)
                    ux2 += 1
            Z1 = self.Z1B.currentText()
            if Z1 == '+':  # Сумма двух кодов С.С.
                a3 += az3
            if Z1 == '-':  # Разность двух кодов С.С.
                a3 -= az3
            if Z1 == 'x':  # Произведение двух кодов С.С.
                a3 *= az3
            if Z1 == ':':  # Частное двух кодов С.С.
                a3 /= az3
            if c2 == 'Двоичная':  # Перевод кода СС по условию
                if a3 >= 2:
                    while a3 >= 2:
                        a4.append(str(a3 % 2))
                        a3 -= a3 % 2
                        a3 /= 2
                        a3 = int(a3)
                        if a3 < 2:
                            a4.append('1')
                else:
                    a4.append(str(a3))
                self.X2B.setText(str(''.join(a4[::-1])))
            if c2 == 'Восьмиричная':
                if a3 >= 8:
                    while a3 >= b2:
                        a4.append(str(a3 % b2))
                        a3 -= a3 % b2
                        a3 //= 8
                        if a3 < 8:
                            a4.append(str(a3))
                else:
                    a4.append(str(a3))
                self.X2B.setText(str(''.join(a4[::-1])))
            if c2 == 'Десятиричная':
                self.X2B.setText(str(a3))
            if c2 == 'Шестнадцатиричная':
                if a3 >= 16:
                    while a3 >= b2:
                        a4.append(str(t16[a3 % b2]))
                        a3 -= a3 % b2
                        a3 //= 16
                        if a3 < 16:
                            a4.append(str(a3))
                else:
                    a4.append(str(t16[a3]))
                self.X2B.setText(str(''.join(a4[::-1])))


app = QApplication(sys.argv)
ex = P1Main()
ex.show()
sys.exit(app.exec_())
