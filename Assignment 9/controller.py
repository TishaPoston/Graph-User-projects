from PySide6.QtWidgets import QMainWindow
from view import Ui_MainWindow
from model import RemixModel


class RemixController(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.model = RemixModel()

        #Connecting buttons to functions
        self.ui.magicButton.clicked.connect(self.capitalize_text)
        self.ui.reverseButton.clicked.connect(self.reverse_text)
        self.ui.lowerButton.clicked.connect(self.lowercase_text)
        self.ui.countButton.clicked.connect(self.count_text)
        self.ui.clearButton.clicked.connect(self.clear_everything)

    #Gets the text from the input box
    def get_input_text(self):
        text = self.ui.nameInput.text()
        self.model.set_text(text)

    def capitalize_text(self):
        self.get_input_text()

        result = self.model.make_uppercase()
        self.ui.resultLabel.setText(result)

    def reverse_text(self):
        self.get_input_text()

        result = self.model.reverse_text()
        self.ui.resultLabel.setText(result)

    def lowercase_text(self):
        self.get_input_text()

        result = self.model.make_lowercase()
        self.ui.resultLabel.setText(result)

    def count_text(self):
        self.get_input_text()

        total = self.model.count_letters()
        self.ui.resultLabel.setText(f"Character Count: {total}")

    def clear_everything(self):
        self.ui.nameInput.clear()
        self.ui.resultLabel.setText("Your transformed text appears here")
