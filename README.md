# Name Remix Studio

## Description

Name Remix Studio is a simple desktop GUI application created with Python and PySide6.
The app allows users to enter text and transform it in different ways using a modern interface.

Users can:
- Convert text to uppercase
- Convert text to lowercase
- Reverse text
- Count characters
- Clear the screen

This project demonstrates the MVC (Model View Controller) design pattern.

---

### MVC Overview

#### Model
The model handles all text processing logic like reversing text,
counting characters, and changing letter cases.

### View
The view is responsible for the graphical user interface.
It contains buttons, labels, and text boxes created with PySide6.

### Controller
The controller connects the view and the model together.
It listens for button clicks and updates the interface with results.

---

#How to Run

1. Install PySide6

```bash
pip install PySide6
```

2. Run the application

```bash
python main.py
```