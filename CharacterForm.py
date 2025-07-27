import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QListWidget, QFileDialog, QGraphicsView, QGraphicsScene, QLineEdit, QDialog, QComboBox, QSpinBox
)
from PyQt5.QtGui import QIcon
from Dice_Functions import roll_stat, roll_stats

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

        self.character_class_label = QLabel("Character Class:")
        self.character_class_input = QComboBox()
        self.character_class_input.addItems(["Barbarian", "Wizard", "Rogue", "Cleric", "Sorcerer", "Paladin", "Druid", "Bard"])
        
        layout.addWidget(self.character_class_label)
        layout.addWidget(self.character_class_input)

        self.character_race_label = QLabel("Character Race:")
        self.character_race_input = QComboBox()
        self.character_race_input.addItems(["Human", "Elf", "Dwarf", "Halfling", "Orc", "Tiefling", "Dragonborn"])
        
        layout.addWidget(self.character_race_label)
        layout.addWidget(self.character_race_input)

        self.hit_points_label = QLabel("Hit Points:")
        self.hit_points_input = QSpinBox()

        hitpoints_layout = QHBoxLayout()
        hitpoints_layout.addWidget(self.hit_points_label)
        hitpoints_layout.addWidget(self.hit_points_input)
        layout.addLayout(hitpoints_layout)

        self.character_stats_choice_label = QLabel("How would you like to choose your stats?")
        self.character_stats_input = QComboBox()
        self.character_stats_input.addItems(["Select", "Roll Stats", "Point Buy", "Standard Array"])
        self.character_stats_input.currentIndexChanged.connect(self.update_stats_display)
        self.char_stats = []
        self.character_stats_list = QLabel(f"Here is your list of stats, choose how to allocate them: {self.char_stats}")

        layout.addWidget(self.character_stats_choice_label)
        layout.addWidget(self.character_stats_input)
        layout.addWidget(self.character_stats_list)

        self.strength_label = QLabel("Strength:")
        self.strength_input = QSpinBox()
        self.dexterity_label = QLabel("Dexterity:")
        self.dexterity_input = QSpinBox()
        self.constitution_label = QLabel("Constitution:")
        self.constitution_input = QSpinBox()
        self.intelligence_label = QLabel("Intelligence:")
        self.intelligence_input = QSpinBox()
        self.wisdom_label = QLabel("Wisdom:")
        self.wisdom_input = QSpinBox()
        self.charisma_label = QLabel("Charisma:")
        self.charisma_input = QSpinBox()

        self.stat_fields = [
            ("Strength", self.strength_label, self.strength_input),
            ("Dexterity", self.dexterity_label, self.dexterity_input),
            ("Constitution", self.constitution_label, self.constitution_input),
            ("Intelligence", self.intelligence_label, self.intelligence_input),
            ("Wisdom", self.wisdom_label, self.wisdom_input),
            ("Charisma", self.charisma_label, self.charisma_input),
        ]

        for name, label, spinbox in self.stat_fields:
            hbox = QHBoxLayout()
            hbox.addWidget(label)
            hbox.addWidget(spinbox)
            layout.addLayout(hbox)

        self.icon_path = None
        self.icon_btn = QPushButton("Choose Icon")
        self.icon_btn.clicked.connect(self.choose_icon)
        layout.addWidget(self.icon_btn)

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
    def update_stats_display(self):
        choice = self.character_stats_input.currentText()
        if choice == "Roll Stats":
            self.char_stats = roll_stats()
            self.character_stats_list.setText(f"Here is your list of stats, choose how to allocate them: {self.char_stats}")
        elif choice == "Standard Array":
            self.char_stats = [15, 14, 13, 12, 10, 8]
            self.character_stats_list.setText(f"Here is your list of stats, choose how to allocate them: {self.char_stats}")
        elif choice == "Point Buy":
            self.character_stats_list.setText('Choose your stats through the point buy system:')
        else:
            self.char_stats = []

    def get_stats_dict(self):
        return {name: spinbox.value() for name, label, spinbox in self.stat_fields}

    def choose_icon(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Choose Icon", "", "Images (*.png *.jpg *.jpeg *.bmp)")
        if file_path:
            self.icon_path = file_path
            self.icon_btn.setText(f"Icon: {file_path.split('/')[-1]}")