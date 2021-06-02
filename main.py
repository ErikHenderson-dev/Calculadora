import sys
from PyQt5.QtWidgets import QApplication, QGridLayout, QMainWindow, QWidget
from PyQt5.QtWidgets import QPushButton, QLineEdit, QSizePolicy

class Calculadora(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Calculadora')
        self.setFixedSize(350, 400)
        self.cw = QWidget()
        self.cw.setStyleSheet(
            '* {background: #A9A9A9;}'
        )

        self.grid = QGridLayout(self.cw)

        self.display = QLineEdit()
        self.grid.addWidget(self.display, 0, 0, 1, 5)
        self.display.setDisabled(True)
        self.display.setStyleSheet(
            '* {background: white; font-size: 30px;}'
        )
        self.display.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        self.add_btn(QPushButton('7'), 1, 0, 1, 1,
            None,
            self.style_numeros()
        )
        self.add_btn(QPushButton('8'), 1, 1, 1, 1,
            None,
            self.style_numeros()  
        )
        self.add_btn(QPushButton('9'), 1, 2, 1, 1,
            None,
            self.style_numeros()
        )
        self.add_btn(
            QPushButton('<-'), 1, 3, 1, 1,
            lambda: self.display.setText(
                self.display.text()[:-1]
            ),
            self.style_operadores()
        )
        self.add_btn(
            QPushButton('C'), 1, 4, 1, 1,
            lambda: self.display.setText(''),
            self.style_operadores()
        )

        self.add_btn(QPushButton('4'), 2, 0, 1, 1,
            None,
            self.style_numeros()
        )
        self.add_btn(QPushButton('5'), 2, 1, 1, 1,
            None,
            self.style_numeros()
        )
        self.add_btn(QPushButton('6'), 2, 2, 1, 1,
            None,
            self.style_numeros()
        )
        self.add_btn(QPushButton('+'), 2, 3, 1, 1,
            None,
            self.style_operadores()
        )
        self.add_btn(QPushButton('-'), 2, 4, 1, 1,
            None,
            self.style_operadores()
        )

        self.add_btn(QPushButton('1'), 3, 0, 1, 1,
            None,
            self.style_numeros()
        )
        self.add_btn(QPushButton('2'), 3, 1, 1, 1,
            None,
            self.style_numeros()
        )
        self.add_btn(QPushButton('3'), 3, 2, 1, 1,
            None,
            self.style_numeros()
        )
        self.add_btn(QPushButton('*'), 3, 3, 1, 1,
            None,
            self.style_operadores()
        )
        self.add_btn(QPushButton('/'), 3, 4, 1, 1,
            None,
            self.style_operadores()
        )

        self.add_btn(QPushButton('.'), 4, 0, 1, 1,
            None,
            self.style_numeros()
        )
        self.add_btn(QPushButton('0'), 4, 1, 1, 1,
            None,
            self.style_numeros()
        )
        self.add_btn(QPushButton(''), 4, 2, 1, 1,
            None,
            self.style_numeros()
        )
        self.add_btn(
            QPushButton('='), 4, 3, 1, 2,
            self.eval_igual,
            'background: #4682B4;'
        )
        

        self.setCentralWidget(self.cw)

    def add_btn(self, btn, row, col, rowspan, coolsapn, funcao=None, style=None):
        self.grid.addWidget(btn, row, col, rowspan, coolsapn)
        if not funcao:
            btn.clicked.connect(
                lambda: self.display.setText(
                    self.display.text() + btn.text()
                )
            )
        else:
            btn.clicked.connect(funcao)

        if style:
            btn.setStyleSheet(style)

        btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

    def eval_igual(self):
        try:
            self.display.setText(
                str(eval(self.display.text()))
            )
        except Exception as e:
            self.display.setText('Error')

    def style_numeros(self):
        return 'background: #1C1C1C; color: white;'

    def style_operadores(self):
        return 'background: #4F4F4F; color: white;'

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    calc = Calculadora()
    calc.show()
    qt.exec_()