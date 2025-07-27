import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QListWidget, QFileDialog, QGraphicsView, QGraphicsScene, QDialog, QListWidgetItem, QCheckBox, QComboBox
)
from PyQt5.QtGui import QIcon, QPixmap, QPen
from PyQt5.QtCore import Qt
from CharacterForm import CharacterFormDialog
from Characters import Character, Enemy
from EnemyForm import EnemyFormDialog
from MapGrid import TokenItem
import Dice_Functions as dice

class VTTMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Virtual Tabletop")
        self.setGeometry(100, 100, 1000, 700)
        self.init_ui()
        self.w = None
        self.characters = {}
        self.enemies = {}
        self.bg_item = None
        self.grid_lines = []

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

        self.enemy_list = QListWidget()
        add_enemy_btn = QPushButton("Add Enemy")
        add_enemy_btn.clicked.connect(self.add_enemy)

        self.dice = QLabel("Roll Dice:")
        self.dice_roll_input = QComboBox()
        self.dice_roll_input.addItems(["d4", "d6", "d8", "d10", "d12", "d20"])
        dice_roll_btn = QPushButton("Roll")
        dice_roll_btn.clicked.connect(self.roll_dice)
        self.dice_result = QLabel("Result: ")
        self.clear_dice_result = QPushButton("Clear")
        self.clear_dice_result.clicked.connect(lambda: self.dice_result_value.setText("0"))
        self.dice_result_value = QLabel(self.result if hasattr(self, 'result') else "0")

        sidebar_layout.addWidget(QLabel("Characters"))
        sidebar_layout.addWidget(self.char_list)
        sidebar_layout.addWidget(QLabel("Enemies"))
        sidebar_layout.addWidget(self.enemy_list)
        sidebar_layout.addWidget(add_char_btn)
        sidebar_layout.addWidget(add_enemy_btn)

        dice_layout = QHBoxLayout()
        dice_layout.addWidget(self.dice)
        dice_layout.addWidget(self.dice_roll_input)
        dice_layout.addWidget(dice_roll_btn)

        dice_result_layout = QHBoxLayout()
        dice_result_layout.addWidget(self.dice_result)
        dice_result_layout.addWidget(self.dice_result_value)
        dice_result_layout.addWidget(self.clear_dice_result)
        sidebar_layout.addLayout(dice_layout)
        sidebar_layout.addLayout(dice_result_layout)
        sidebar_layout.addStretch()

        # Map area: Placeholder using QGraphicsView
        self.scene = QGraphicsScene()
        self.map_view = QGraphicsView(self.scene)
        self.map_view.setMinimumSize(600, 600)
        self.use_gridlines = QCheckBox("Use Gridlines")
        self.use_gridlines.setChecked(False)
        self.use_gridlines.stateChanged.connect(self.draw_grid)
        map_layout.addWidget(QLabel("Map Area"))
        map_layout.addWidget(self.map_view)
        set_bg_btn = QPushButton("Set Map Background")
        set_bg_btn.clicked.connect(self.set_map_background)
        map_layout.addWidget(set_bg_btn)
        map_layout.addWidget(self.use_gridlines)

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
            char_hp = dialog.hit_points_input.value()
            char_stats = dialog.get_stats_dict()
            icon_path = dialog.icon_path
            if char_name:
                character = Character(char_name, char_race, char_class, char_hp, char_stats, icon_path)
                self.characters[char_name] = character
                display_text = f"{char_name} ({char_class})"
                item = QListWidgetItem(display_text)
                if icon_path:
                    item.setIcon(QIcon(icon_path))
                    self.add_icon_to_map(icon_path, char_name)
                self.char_list.addItem(item)
    
    def add_enemy(self):
        dialog = EnemyFormDialog(self)
        if dialog.exec() == QDialog.Accepted:
            enemy_name = dialog.name_input.text()
            enemy_race = dialog.enemy_race_input.text()
            enemy_stats = dialog.get_stats_dict()
            enemy_hp = dialog.hit_points_input.value()
            enemy_attacks = dialog.get_attacks()
            icon_path = dialog.icon_path
            if enemy_name:
                enemy = Enemy(enemy_name, enemy_race, enemy_stats, enemy_hp, enemy_attacks, icon_path)
                self.enemies[enemy_name] = enemy
                display_text = enemy_name
                item = QListWidgetItem(display_text)
                if icon_path:
                    item.setIcon(QIcon(icon_path))
                    self.add_icon_to_map(icon_path, enemy_name, x=60, y=0)
                self.enemy_list.addItem(item)

    def add_icon_to_map(self, icon_path, name, x=0, y=0):
        if icon_path:
            pixmap = QPixmap(icon_path).scaled(48, 48)  # Adjust size as needed
            token = TokenItem(pixmap, name, grid_size=48)
            token.setPos(x, y)
            self.scene.addItem(token)
    
    def draw_grid(self, state = None, grid_size=48, width=600, height=600):
        for line in getattr(self, "grid_lines", []):
            self.scene.removeItem(line)
        self.grid_lines = []

        if self.use_gridlines.isChecked():
            pen = QPen(Qt.gray)
            pen.setWidth(1)
            for x in range(0, width, grid_size):
                line = self.scene.addLine(x, 0, x, height, pen)
                line.setZValue(-50)
                self.grid_lines.append(line)
            for y in range(0, height, grid_size):
                line = self.scene.addLine(0, y, width, y, pen)
                line.setZValue(-50)
                self.grid_lines.append(line)
        

    def set_map_background(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Choose Map Background", "", "Images (*.png *.jpg *.bmp)")
        if file_path:
            pixmap = QPixmap(file_path).scaled(600, 600, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
            # Remove previous background if any
            if hasattr(self, 'bg_item') and self.bg_item:
                self.scene.removeItem(self.bg_item)
            self.bg_item = self.scene.addPixmap(pixmap)
            self.bg_item.setZValue(-100)
            self.bg_item.setPos(0, 0)
            self.draw_grid()  # Redraw grid on top of the background

    def roll_dice(self):
        result = int(self.dice_result_value.text())
        dice_type = self.dice_roll_input.currentText()
        dice_type_int = int(dice_type[1:]) if dice_type.startswith('d') else None
        if dice_type_int:
            self.result = result + dice.dice_roll(dice_type_int)
            self.dice_result_value.setText(str(self.result))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VTTMainWindow()
    window.show()
    sys.exit(app.exec_())