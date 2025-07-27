import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QListWidget, QFileDialog, QGraphicsView, QGraphicsScene, QLineEdit, QDialog, QComboBox, QSpinBox
)
from PyQt5.QtGui import QIcon
from Dice_Functions import roll_stat, roll_stats

class EnemyFormDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Enemy Form")
        self.setGeometry(100, 100, 300, 200)
        
        layout = QVBoxLayout()
        
        self.name_label = QLabel("Enemy Name:")
        self.name_input = QLineEdit()
        
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)

        self.enemy_race_label = QLabel("Enemy Race:")
        self.enemy_race_input = QLineEdit()
        
        layout.addWidget(self.enemy_race_label)
        layout.addWidget(self.enemy_race_input)

        hitpoints_layout = QHBoxLayout()
        hitpoints_layout.addWidget(self.hit_points_label)
        hitpoints_layout.addWidget(self.hit_points_input)
        layout.addLayout(hitpoints_layout)

        self.character_stats_choice_label = QLabel("Please enter the stats list:")

        layout.addWidget(self.character_stats_choice_label)

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

        #Attacks
        self.attacks = []
        for i in range(1, 4):
            self.attacks_label = QLabel(f"Attack {i}:")
            self.attack_label = QLabel("Attack Name:")
            self.attack_input = QLineEdit()
            self.attack_damage_label = QLabel("Damage:")
            self.attack_damage_input = QSpinBox()
            self.attack_damage_dice = QComboBox()
            self.attack_damage_dice.addItems(["d4", "d6", "d8", "d10", "d12"])

            layout.addWidget(self.attacks_label)
            attack_layout = QHBoxLayout()
            attack_layout.addWidget(self.attack_label)
            attack_layout.addWidget(self.attack_input)
            attack_layout.addWidget(self.attack_damage_label)
            attack_layout.addWidget(self.attack_damage_input)
            attack_layout.addWidget(self.attack_damage_dice)
            layout.addLayout(attack_layout)

            self.attacks.append({
                "name_input": self.attack_input,
                "damage_input": self.attack_damage_input,
                "damage_dice": self.attack_damage_dice
            })

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

    def get_stats_dict(self):
        return {name: spinbox.value() for name, label, spinbox in self.stat_fields}

    def get_attacks(self):
        attacks = []
        for attack in self.attacks:
            name = attack["name_input"].text()
            damage = attack["damage_input"].value()
            dice = attack["damage_dice"].currentText()
            if name:  # Only include attacks with a name
                attacks.append({"name": name, "damage": damage, "dice": dice})
        return attacks