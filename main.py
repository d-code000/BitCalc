import re
import sys

from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton

from backend import Calculator
from ui.mainwindow import Ui_MainWindow

DIGIT_BUTTONS = [str(i) for i in range(10)]


class CalculatorWindow(QMainWindow):
    def __init__(self):
        super(CalculatorWindow, self).__init__()

        self.calculator = Calculator()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.lineEdit = self.ui.lineEdit
        self.lineEdit.setText('0')
        self.lineEdit.setValidator(QIntValidator())
        self.backspaceButton = self.ui.backspaseButton
        self.clearButton = self.ui.clearButton
        self.clearAllButton = self.ui.clearAllButton

        self.ui.backspaseButton.clicked.connect(self.backspace_line)
        self.ui.clearButton.clicked.connect(self.clear_line)
        self.ui.clearAllButton.clicked.connect(self.clear_all_line)
        self.ui.mPlusButton.clicked.connect(self.memory_plus)
        self.ui.mMinusButton.clicked.connect(self.memory_minus)
        self.ui.mrButton.clicked.connect(self.memory_read)
        self.ui.msButton.clicked.connect(self.memory_save)
        self.ui.plusMinusButton.clicked.connect(self.change_sign)
        self.ui.plusButton.clicked.connect(self.set_operation)
        self.ui.minusButton.clicked.connect(self.set_operation)
        self.ui.multButton.clicked.connect(self.set_operation)
        self.ui.divButton.clicked.connect(self.set_operation)
        self.ui.expButton.clicked.connect(self.set_operation)
        self.ui.equalButton.clicked.connect(self.get_result)

        self.ui.valButton_0.clicked.connect(self.add_digit)
        self.ui.valButton_1.clicked.connect(self.add_digit)
        self.ui.valButton_2.clicked.connect(self.add_digit)
        self.ui.valButton_3.clicked.connect(self.add_digit)
        self.ui.valButton_4.clicked.connect(self.add_digit)
        self.ui.valButton_5.clicked.connect(self.add_digit)
        self.ui.valButton_6.clicked.connect(self.add_digit)
        self.ui.valButton_7.clicked.connect(self.add_digit)
        self.ui.valButton_8.clicked.connect(self.add_digit)
        self.ui.valButton_9.clicked.connect(self.add_digit)

    def get_result(self) -> None:
        try:
            self.calculator.second_num = int(self.lineEdit.text())
            result = self.calculator.get_result()
            self.calculator.clear()
            self.lineEdit.setText(str(result))
        except ZeroDivisionError:
            self.lineEdit.setText('Деление на ноль')
        except SyntaxError:
            self.calculator.second_num = None

    def set_operation(self) -> None:
        btn: QPushButton = self.sender()
        match btn:
            case self.ui.plusButton:
                self.calculator.operation = '+'
            case self.ui.minusButton:
                self.calculator.operation = '-'
            case self.ui.multButton:
                self.calculator.operation = '*'
            case self.ui.divButton:
                self.calculator.operation = '/'
            case self.ui.expButton:
                self.calculator.operation = '**'
        self.calculator.first_num = int(self.lineEdit.text())
        self.clear_line()

    def change_sign(self) -> None:
        num = int(self.lineEdit.text())
        self.lineEdit.setText(str(-num))

    def backspace_line(self) -> None:
        self.lineEdit.backspace()
        if self.lineEdit.text() == '':
            self.lineEdit.setText('0')

    def clear_line(self) -> None:
        self.lineEdit.clear()
        self.lineEdit.setText('0')

    def clear_all_line(self) -> None:
        self.calculator.clear()
        self.clear_line()

    def add_digit(self) -> None:
        btn: QPushButton = self.sender()
        digit = re.search(r"\d+", btn.objectName()).group()
        if digit in DIGIT_BUTTONS:
            if self.lineEdit.text() == '0':
                self.lineEdit.setText(btn.text())
            else:
                self.lineEdit.setText(self.lineEdit.text() + btn.text())

    def memory_plus(self) -> None:
        num = int(self.lineEdit.text())
        self.calculator.memory += num

    def memory_minus(self) -> None:
        num = int(self.lineEdit.text())
        self.calculator.memory -= num

    def memory_read(self) -> None:
        self.lineEdit.setText(str(self.calculator.memory))

    def memory_save(self) -> None:
        num = int(self.lineEdit.text())
        self.calculator.memory = num


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = CalculatorWindow()
    window.show()

    sys.exit(app.exec())
