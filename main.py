#author : Nguyễn Vũ Xuân Kiên | 17/02/2004 | Email : nguyenvxkien@gmail.com | github.com/xkien2k4
import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QGridLayout, QPushButton,
    QVBoxLayout, QLineEdit, QLabel
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Máy tính tay")
        self.setFixedSize(360, 560)

        self.expression = ""

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # ===== HEADER =====
        self.title = QLabel("Chuẩn")
        self.title.setFont(QFont("Segoe UI", 16))
        self.title.setStyleSheet("color: white; margin-left:10px;")
        layout.addWidget(self.title)

        # ===== DISPLAY =====
        self.display = QLineEdit()
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setFont(QFont("Segoe UI", 32))
        self.display.setFixedHeight(80)

        self.display.setStyleSheet("""
            QLineEdit {
                background-color: #1f1f1f;
                border: 2px solid #3a3a3a;
                border-radius: 10px;
                color: white;
                padding-right: 10px;
            }
        """)

        layout.addWidget(self.display)

        # ===== GRID BUTTON =====
        grid = QGridLayout()
        grid.setSpacing(8)

        buttons = [
            ["%", "CE", "C", "⌫"],
            ["1/x", "x²", "√x", "÷"],
            ["7", "8", "9", "×"],
            ["4", "5", "6", "−"],
            ["1", "2", "3", "+"],
            ["+/-", "0", ".", "="]
        ]

        for r, row in enumerate(buttons):
            for c, text in enumerate(row):
                btn = QPushButton(text)
                btn.setFont(QFont("Segoe UI", 14))
                btn.setFixedSize(75, 60)

                # STYLE
                if text == "=":
                    btn.setStyleSheet("""
                        QPushButton {
                            background-color: #4cc2ff;
                            border-radius: 8px;
                            color: black;
                        }
                        QPushButton:hover {
                            background-color: #2fa4e7;
                        }
                    """)
                else:
                    btn.setStyleSheet("""
                        QPushButton {
                            background-color: #2d2d2d;
                            border-radius: 8px;
                            color: white;
                        }
                        QPushButton:hover {
                            background-color: #3a3a3a;
                        }
                    """)

                btn.clicked.connect(lambda _, t=text: self.on_click(t))
                grid.addWidget(btn, r, c)

        layout.addLayout(grid)

        # BACKGROUND
        self.setStyleSheet("background-color: #1f1f1f;")

        self.setLayout(layout)

    def on_click(self, char):
        try:
            if char == "C":
                self.expression = ""
            elif char == "CE":
                self.expression = ""
            elif char == "⌫":
                self.expression = self.expression[:-1]
            elif char == "=":
                self.expression = str(eval(self.expression))
            elif char == "×":
                self.expression += "*"
            elif char == "÷":
                self.expression += "/"
            elif char == "−":
                self.expression += "-"
            elif char == "x²":
                self.expression = str(eval(self.expression) ** 2)
            elif char == "√x":
                self.expression = str(eval(self.expression) ** 0.5)
            elif char == "1/x":
                self.expression = str(1 / eval(self.expression))
            elif char == "+/-":
                if self.expression.startswith("-"):
                    self.expression = self.expression[1:]
                else:
                    self.expression = "-" + self.expression
            else:
                self.expression += char

        except:
            self.expression = "Error"

        self.display.setText(self.expression)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec())