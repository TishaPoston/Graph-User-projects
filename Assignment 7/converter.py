#converter.py
#Quatisha Poston
#Graph User Interface Dev. Sector
#Assignment 7 - Measurement Converter GUI
#April 1st, 2026

import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *


class ConverterApp(QMainWindow):
    """Simple measurement converter using PySide6"""

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Measurement Converter")
        self.resize(650, 500)

        #This creates the main container for the window
        self.mainWidget = QWidget()
        self.setCentralWidget(self.mainWidget)

        #This creates the title at the top
        self.titleLabel = QLabel("Converter App")
        self.titleLabel.setAlignment(Qt.AlignCenter)

        #This loads and displays the house image
        self.houseImage = QLabel()
        self.houseImage.setAlignment(Qt.AlignCenter)
        image = QPixmap("house.png")
        self.houseImage.setPixmap(image.scaled(180, 180))

        #This tells the user what to do
        self.infoText = QLabel("Enter a value and choose conversion")
        self.infoText.setAlignment(Qt.AlignCenter)

        #This is where the user types their number
        self.inputValue = QLineEdit()

        #This creates the radio button group
        self.convertGroup = QGroupBox("Conversion Type")
        self.inToMeters = QRadioButton("Inches to Meters")
        self.metersToIn = QRadioButton("Meters to Inches")

        #This sets Inches to Meters as the default option
        self.inToMeters.setChecked(True)

        groupLayout = QVBoxLayout()
        groupLayout.addWidget(self.inToMeters)
        groupLayout.addWidget(self.metersToIn)
        self.convertGroup.setLayout(groupLayout)

        #This label will display the result
        self.outputLabel = QLabel("")
        self.outputLabel.setAlignment(Qt.AlignCenter)

        #These are the main buttons for the app
        self.convertBtn = QPushButton("Convert")
        self.clearBtn = QPushButton("Clear")
        self.exitBtn = QPushButton("Exit")

        #This creates the main layout for the window
        mainLayout = QVBoxLayout()
        buttonLayout = QHBoxLayout()

        mainLayout.addWidget(self.titleLabel)
        mainLayout.addWidget(self.houseImage)
        mainLayout.addWidget(self.infoText)
        mainLayout.addWidget(self.inputValue)
        mainLayout.addWidget(self.convertGroup)
        mainLayout.addWidget(self.outputLabel)

        #This adds the buttons to a horizontal layout
        buttonLayout.addWidget(self.convertBtn)
        buttonLayout.addWidget(self.clearBtn)
        buttonLayout.addWidget(self.exitBtn)

        mainLayout.addLayout(buttonLayout)

        self.mainWidget.setLayout(mainLayout)

        #These connect each button to its function
        self.convertBtn.clicked.connect(self.convert_value)
        self.clearBtn.clicked.connect(self.clear_fields)
        self.exitBtn.clicked.connect(self.close)

    def convert_value(self):
        """Handles conversion and validation"""

        text = self.inputValue.text()

        #This checks if the input is empty
        if text == "":
            QMessageBox.critical(self, "Error", "Please enter a value.")
            return

        #This checks if the input is a number
        try:
            number = float(text)
        except ValueError:
            QMessageBox.critical(self, "Error", "Value entered is not numeric.")
            return

        #This makes sure the number is positive
        if number <= 0:
            QMessageBox.critical(self, "Error", "Value must be positive.")
            return

        # This performs the correct conversion based on selection
        if self.inToMeters.isChecked():
            meters = number * 0.0254
            self.outputLabel.setText(f"{number:.3f} inches = {meters:.3f} meters")

        elif self.metersToIn.isChecked():
            inches = number / 0.0254
            self.outputLabel.setText(f"{number:.3f} meters = {inches:.3f} inches")

    def clear_fields(self):
        """Clears input and resets UI"""

        #This clears the input box
        self.inputValue.clear()

        #This clears the result label
        self.outputLabel.setText("")

        #This resets the default radio button
        self.inToMeters.setChecked(True)

        #This puts the cursor back in the input box
        self.inputValue.setFocus()


#run the application
app = QApplication(sys.argv)
window = ConverterApp()
window.show()
sys.exit(app.exec())
