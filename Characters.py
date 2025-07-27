import Dice_Functions as dice

class Character:
    def __init__(self, name, race, char_class, hit_points, stats, icon_path):
        self.name = name
        self.race = race
        self.char_class = char_class
        self.hit_points = hit_points
        self.stats = stats
        self.icon_path = icon_path

class Enemy:
    def __init__(self, name, race, stats, hit_points, attacks, icon_path):
        self.name = name
        self.race = race
        self.stats = stats
        self.hit_points = hit_points
        self.attacks = attacks
        self.icon_path = icon_path
    
