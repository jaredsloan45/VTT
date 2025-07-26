import Dice_Functions as dice

class Character:
    def __init__(self, name, race, char_class, stats = None):
        self.name = name
        self.race = race
        self.char_class = char_class
        if stats:
            self.stats = stats
        else:
            self.stats = self.roll_stats()

    def roll_stats(self):
        # Rolls stats using the Dice_Functions module
        return {
            'Strength': dice.roll_stat(),
            'Dexterity': dice.roll_stat(),
            'Constitution': dice.roll_stat(),
            'Intelligence': dice.roll_stat(),
            'Wisdom': dice.roll_stat(),
            'Charisma': dice.roll_stat()
        }
    
