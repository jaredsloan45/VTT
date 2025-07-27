from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QListWidget, QFileDialog, QGraphicsView, QGraphicsScene, QDialog, QListWidgetItem, QCheckBox, QComboBox
)
from PyQt5.QtGui import QIcon, QPixmap, QPen
from PyQt5.QtCore import Qt

def token_double_clicked(token_item, parent):
        dialog = QDialog(parent)
        dialog.setWindowTitle(f"Token: {token_item.toolTip()}")
        layout = QVBoxLayout()
        label = QLabel(f"You double-clicked on: {token_item.toolTip()}")
        layout.addWidget(label)
        dialog.setLayout(layout)
        dialog.exec_()