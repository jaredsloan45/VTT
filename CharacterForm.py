import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QListWidget, QFileDialog, QGraphicsView, QGraphicsScene, QLineEdit, QDialog
)
from PyQt5.QtGui import QIcon

class CharacterFormDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Character Form")
        self.setGeometry(100, 100, 300, 200)
        
        layout = QVBoxLayout()
        
        self.name_label = QLabel("Character Name:")
        self.name_input = QLineEdit()
        
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)
        
        # Add OK and Cancel buttons
        button_layout = QHBoxLayout()
        self.ok_button = QPushButton("OK")
        self.cancel_button = QPushButton("Cancel")
        self.ok_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)
        button_layout.addWidget(self.ok_button)
        button_layout.addWidget(self.cancel_button)
        layout.addLayout(button_layout)
        
        self.setLayout(layout)