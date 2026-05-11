from PySide6.QtCore import QRect, Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QLineEdit,
    QMainWindow
)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setWindowTitle("Name Remix Studio")
        MainWindow.resize(700, 500)

        self.centralwidget = QWidget(MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)

        #Main title
        self.titleLabel = QLabel("Name Remix Studio", self.centralwidget)
        self.titleLabel.setGeometry(QRect(180, 30, 350, 50))

        title_font = QFont()
        title_font.setPointSize(22)
        title_font.setBold(True)

        self.titleLabel.setFont(title_font)
        self.titleLabel.setAlignment(Qt.AlignCenter)

        #Input box
        self.nameInput = QLineEdit(self.centralwidget)
        self.nameInput.setGeometry(QRect(150, 120, 400, 50))
        self.nameInput.setPlaceholderText("Type your text here...")

        #Result label
        self.resultLabel = QLabel(
            "Your transformed text appears here",
            self.centralwidget
        )
        self.resultLabel.setGeometry(QRect(120, 210, 460, 60))

        result_font = QFont()
        result_font.setPointSize(14)

        self.resultLabel.setFont(result_font)
        self.resultLabel.setAlignment(Qt.AlignCenter)

        #Uppercase button
        self.magicButton = QPushButton(
            "UPPERCASE MAGIC",
            self.centralwidget
        )
        self.magicButton.setGeometry(QRect(80, 320, 170, 50))

        #Reverse button
        self.reverseButton = QPushButton(
            "REVERSE IT",
            self.centralwidget
        )
        self.reverseButton.setGeometry(QRect(270, 320, 170, 50))

        #Lowercase button
        self.lowerButton = QPushButton(
            "lowercase vibe",
            self.centralwidget
        )
        self.lowerButton.setGeometry(QRect(460, 320, 170, 50))

        #Count button
        self.countButton = QPushButton(
            "COUNT LETTERS",
            self.centralwidget
        )
        self.countButton.setGeometry(QRect(170, 390, 170, 50))

        #Clear button
        self.clearButton = QPushButton(
            "CLEAR",
            self.centralwidget
        )
        self.clearButton.setGeometry(QRect(360, 390, 170, 50))

        #Modern styling
        MainWindow.setStyleSheet("""
            QMainWindow {
                background-color: #1e1f29;
            }

            QLabel {
                color: #f5f5f5;
            }

            QLineEdit {
                background-color: #2d2f3d;
                color: white;
                border: 2px solid #7b68ee;
                border-radius: 12px;
                padding: 10px;
                font-size: 16px;
            }

            QPushButton {
                background-color: #7b68ee;
                color: white;
                border-radius: 14px;
                font-size: 14px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #937dff;
            }

            QPushButton:pressed {
                background-color: #5f4cd6;
            }
        """)
