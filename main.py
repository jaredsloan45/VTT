import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QListWidget, QFileDialog, QGraphicsView, QGraphicsScene, QDialog
)
from PyQt5.QtGui import QIcon
from CharacterForm import CharacterFormDialog
from Characters import Character
from EnemyForm import EnemyFormDialog

class VTTMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Virtual Tabletop")
        self.setGeometry(100, 100, 1000, 700)
        self.init_ui()
        self.w = None
        self.characters = {}

    def init_ui(self):
        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layouts
        main_layout = QHBoxLayout()
        sidebar_layout = QVBoxLayout()
        map_layout = QVBoxLayout()

        # Sidebar: Character list and buttons
        self.char_list = QListWidget()
        add_char_btn = QPushButton("Add Character")
        add_char_btn.clicked.connect(self.add_character)

        add_enemy_btn = QPushButton("Add Enemy")
        add_enemy_btn.clicked.connect(self.add_enemy)

        sidebar_layout.addWidget(QLabel("Characters"))
        sidebar_layout.addWidget(self.char_list)
        sidebar_layout.addWidget(add_char_btn)
        sidebar_layout.addWidget(add_enemy_btn)
        sidebar_layout.addStretch()

        # Map area: Placeholder using QGraphicsView
        self.scene = QGraphicsScene()
        self.map_view = QGraphicsView(self.scene)
        self.map_view.setMinimumSize(600, 600)
        map_layout.addWidget(QLabel("Map Area"))
        map_layout.addWidget(self.map_view)

        # Combine layouts
        main_layout.addLayout(sidebar_layout, 1)
        main_layout.addLayout(map_layout, 3)
        central_widget.setLayout(main_layout)

    def add_character(self):
        # Simple placeholder for adding a character
        dialog = CharacterFormDialog(self)
        if dialog.exec_() == QDialog.Accepted:
            char_name = dialog.name_input.text()
            char_class = dialog.character_class_input.currentText()
            char_race = dialog.character_race_input.currentText()
            char_stats = dialog.get_stats_dict()
            if char_name:
                character = Character(char_name, char_race, char_class, char_stats)
                self.characters[char_name] = character
                display_text = f"{char_name} ({char_class})"
                self.char_list.addItem(display_text)
    
    def add_enemy(self):
        dialog = EnemyFormDialog(self)
        if dialog.exec() == QDialog.Accepted:
            enemy_name = dialog.name_input.text()
            enemy_race = dialog.enemy_race_input.text()
            enemy_stats = dialog.get_stats_dict()
            if enemy_name:
               pass 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VTTMainWindow()
    window.show()
    sys.exit(app.exec_())