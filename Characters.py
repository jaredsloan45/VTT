import Dice_Functions as dice

class Character:
    def __init__(self, name, race, char_class, hit_points, armor_class, stats, attacks, icon_path):
        self.name = name
        self.race = race
        self.char_class = char_class
        self.hit_points = hit_points
        self.armor_class = armor_class
        self.stats = stats
        self.attacks = attacks
        self.icon_path = icon_path

class Enemy:
    def __init__(self, name, race, stats, hit_points, armor_class, attacks, icon_path):
        self.name = name
        self.race = race
        self.stats = stats
        self.hit_points = hit_points
        self.armor_class = armor_class
        self.attacks = attacks
        self.icon_path = icon_path
    
