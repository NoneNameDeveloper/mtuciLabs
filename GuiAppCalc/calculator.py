import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton
import time


class Calculator(QWidget):
    def __init__(self):
        '''
        ТУТ ЛЕЖАТ ЭКЗЕМПЛЯРЫ
        '''
        super().__init__() # получаем доступ к унаследованным методам

        self.vbox = QVBoxLayout(self)

        self.hbox_input = QHBoxLayout()

        self.hbox_zero = QHBoxLayout() # AC C % del
        self.hbox_first = QHBoxLayout() # 1 2 3 *
        self.hbox_second = QHBoxLayout() # 4 5 6 -
        self.hbox_third = QHBoxLayout() # 7 8 9 /
        self.hbox_forth = QHBoxLayout() # 0 00 , +
        self.hbox_fifth = QHBoxLayout() # =

        self.vbox.addLayout(self.hbox_input)
        
        self.vbox.addLayout(self.hbox_zero)
        self.vbox.addLayout(self.hbox_first)
        self.vbox.addLayout(self.hbox_second)
        self.vbox.addLayout(self.hbox_third)
        self.vbox.addLayout(self.hbox_forth)
        self.vbox.addLayout(self.hbox_fifth)


        self.input = QLineEdit(self)
        self.hbox_input.addWidget(self.input)

        self.b_ac = QPushButton("AC", self)
        self.hbox_zero.addWidget(self.b_ac)
        self.b_clear = QPushButton("C (no work)", self)
        self.hbox_zero.addWidget(self.b_clear)
        self.b_perc = QPushButton("%", self)
        self.hbox_zero.addWidget(self.b_perc)
        self.b_del = QPushButton("del", self)
        self.hbox_zero.addWidget(self.b_del)


        self.b_1 = QPushButton("1", self)
        self.hbox_first.addWidget(self.b_1)
        self.b_2 = QPushButton("2", self)
        self.hbox_first.addWidget(self.b_2)
        self.b_3 = QPushButton("3", self)
        self.hbox_first.addWidget(self.b_3)
        self.b_umn = QPushButton("*", self)
        self.hbox_first.addWidget(self.b_umn)
        
        self.b_4 = QPushButton("4", self)
        self.hbox_second.addWidget(self.b_4)
        self.b_5 = QPushButton("5", self)
        self.hbox_second.addWidget(self.b_5)
        self.b_6 = QPushButton("6", self)
        self.hbox_second.addWidget(self.b_6)
        self.b_minus = QPushButton("-", self)
        self.hbox_second.addWidget(self.b_minus)

        
        self.b_7 = QPushButton("7", self)
        self.hbox_third.addWidget(self.b_7)
        self.b_8 = QPushButton("8", self)
        self.hbox_third.addWidget(self.b_8)
        self.b_9 = QPushButton("9", self)
        self.hbox_third.addWidget(self.b_9)
        self.b_div = QPushButton("/", self)
        self.hbox_third.addWidget(self.b_div)
        
        self.b_0 = QPushButton("0", self)
        self.hbox_forth.addWidget(self.b_0)
        self.b_00 = QPushButton("00", self)
        self.hbox_forth.addWidget(self.b_00)
        self.b_zap = QPushButton(".", self)
        self.hbox_forth.addWidget(self.b_zap)
        self.b_plus = QPushButton("+", self)
        self.hbox_forth.addWidget(self.b_plus)



        self.b_result = QPushButton("=", self)
        self.hbox_fifth.addWidget(self.b_result)




            
        self.b_1.clicked.connect(lambda: self._button("1"))
        self.b_2.clicked.connect(lambda: self._button("2"))
        self.b_3.clicked.connect(lambda: self._button("3"))
        self.b_4.clicked.connect(lambda: self._button("4"))
        self.b_5.clicked.connect(lambda: self._button("5"))
        self.b_6.clicked.connect(lambda: self._button("6"))
        self.b_7.clicked.connect(lambda: self._button("7"))
        self.b_8.clicked.connect(lambda: self._button("8"))
        self.b_9.clicked.connect(lambda: self._button("9"))
        self.b_0.clicked.connect(lambda: self._button("0"))
        self.b_00.clicked.connect(lambda: self._button("00"))

        self.b_plus.clicked.connect(lambda: self._operation("+"))
        self.b_minus.clicked.connect(lambda: self._operation("-"))
        self.b_umn.clicked.connect(lambda: self._operation("*"))
        self.b_div.clicked.connect(lambda: self._operation("/"))
        
        
        self.b_del.clicked.connect(self._delete)
        self.b_ac.clicked.connect(self._reset)
        self.b_result.clicked.connect(self._result)
        self.b_perc.clicked.connect(lambda: self._button("%"))
        self.b_zap.clicked.connect(lambda: self._button("."))

    def _reset(self):
        self.input.setText("")

    
    def _is_number(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    def _delete(self):
        line = self.input.text()
        if line:
            self.input.setText(line[0 : len(line) - 1])
    
   
    def _button(self, param):
        line = self.input.text()

        if param == "%":
            if not self._is_number(self.input.text()): 
                return self.input.setText("String is not available")
            return self.input.setText(str(float(line) / 100))

        elif param == ".":
            if line:
                return self.input.setText(line + param)
            else:
                return self.input.setText("0.")

        elif param == ",":
            if line:
                return self.input.setText(line + param)
            else:
                return self.input.setText("0.")

        line = self.input.text()
        self.input.setText(line + param)



    def _operation(self, op):
        if not self._is_number(self.input.text()): 
            return self.input.setText("String not available")
        elif self.input.text():
            self.num_1 = float(self.input.text())
            self.op = op
            self.input.setText("")

    def _result(self):
        if not self._is_number(self.input.text()): 
            return self.input.setText("String not available")       
        if self.input.text() and self.op:

            self.num_2 = float(self.input.text())
            if self.op == "+":
                self.input.setText(str(self.num_1 + self.num_2))
            elif self.op == "-":
                self.input.setText(str(self.num_1 - self.num_2))
            elif self.op == "/":
                if self.num_2 != 0:
                    self.input.setText(str(self.num_1 / self.num_2))
                else:
                    self.input.setText("Can't divide by 0")
            if self.op == "*":
                self.input.setText(str(self.num_1 * self.num_2))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Calculator()
    win.show()
    sys.exit(app.exec_())