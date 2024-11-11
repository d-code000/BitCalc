import sys

from PySide6.QtWidgets import QMainWindow, QApplication
from ui.mainwindow import Ui_MainWindow


class Calculator(QMainWindow):
    def __init__(self):
        super(Calculator, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.lineEdit = self.ui.lineEdit
        self.backspaceButton = self.ui.backspaseButton
        self.clearButton = self.ui.clearButton
        self.clearAllButton = self.ui.clearAllButton

        self.ui.backspaseButton.clicked.connect(self.backspace_line)
        self.ui.clearButton.clicked.connect(self.clear_line)
        self.ui.clearAllButton.clicked.connect(self.clear_all_line)

    def backspace_line(self) -> None:
        self.lineEdit.backspace()

    def clear_line(self) -> None:
        self.lineEdit.clear()

    def clear_all_line(self) -> None:
        self.clear_line()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Calculator()
    window.show()

    sys.exit(app.exec())
