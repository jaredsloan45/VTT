import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QListWidget, QFileDialog, QGraphicsView, QGraphicsScene, QLineEdit
)
from PyQt5.QtGui import QIcon

class CharacterFormDialog(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Character Form")
        self.setGeometry(100, 100, 300, 200)
        
        layout = QVBoxLayout()
        
        self.name_label = QLabel("Character Name:")
        self.name_input = QLineEdit()
        
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)
        
        self.setLayout(layout)