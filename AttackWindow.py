from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QListWidget, QFileDialog, QGraphicsView, QGraphicsScene, QDialog, QListWidgetItem, QCheckBox, QComboBox
)
from PyQt5.QtGui import QIcon, QPixmap, QPen
from PyQt5.QtCore import Qt

def token_double_clicked(token_item, parent):
    dialog = QDialog(parent)
    dialog.setWindowTitle(f"Attack with: {token_item.name}")
    layout = QVBoxLayout()
    label = QLabel(f"You are attacking with: {token_item.name}")
    layout.addWidget(label)

    # Enemy selection
    enemy_label = QLabel("Choose target enemy:")
    enemy_combo = QComboBox()
    # Get enemies from parent (main window)
    enemy_names = list(getattr(parent, 'enemies', {}).keys())
    enemy_combo.addItems(enemy_names if enemy_names else ["No enemies"])
    layout.addWidget(enemy_label)
    layout.addWidget(enemy_combo)

    # Attack selection
    attack_label = QLabel("Choose attack:")
    attack_combo = QComboBox()
    # Get attacks from the character (token_item.name)
    char_obj = getattr(parent, 'characters', {}).get(token_item.name)
    if char_obj and hasattr(char_obj, 'attacks'):
        attack_names = [atk['name'] for atk in char_obj.attacks if atk.get('name')]
        attack_combo.addItems(attack_names if attack_names else ["No attacks"])
    else:
        attack_combo.addItem("No attacks")
    layout.addWidget(attack_label)
    layout.addWidget(attack_combo)

    # Attack button
    attack_button = QPushButton("Roll to attack")
    attack_button.clicked.connect(lambda: parent.attack(token_item.name, enemy_combo.currentText(), attack_combo.currentText()))
    layout.addWidget(attack_button)

    dialog.setLayout(layout)
    dialog.exec_()