import random 

def dice_roll(n = 6):
    """Simulate rolling an n-sided die."""
    return random.randint(1, n)

def dice_rolls(m, n = 6):
    #roll an n-sided die m times
    output = 0
    for i in range(m):
        output += dice_roll(n)
    return output

def roll_stat():
    #rolls 4d6 and drops lowest
    stat_rolls = []
    for i in range(4):
        stat_rolls.append(dice_roll())
    stat = sum(stat_rolls)-min(stat_rolls)
    return stat



print(roll_stat())