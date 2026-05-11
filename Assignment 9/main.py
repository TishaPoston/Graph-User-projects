import sys
from PySide6.QtWidgets import QApplication
from controller import RemixController


# Starts the application
app = QApplication(sys.argv)

window = RemixController()
window.show()

sys.exit(app.exec())
