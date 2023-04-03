import random

def roll_dice(num_dice, num_sides, modifier=0):
    """Simulates rolling multiple dice with different numbers of sides and a modifier.
    Args:
        num_dice (int): The number of dice to roll.
        num_sides (int): The number of sides each die has.
        modifier (int, optional): A modifier to add to the roll. Defaults to 0.
    Returns:
        tuple: A tuple containing the individual rolls and the total sum of the rolls with the modifier.
    """
    rolls = []
    for i in range(num_dice):
        roll = random.randint(1, num_sides)
        rolls.append(roll)
    total = sum(rolls) + modifier
    return (rolls, total)

if __name__ == '__main__':
    num_dice, num_sides = input("Enter the number of dice and the number of sides, separated by a space: ").split()
    num_dice = int(num_dice)
    num_sides = int(num_sides)

    modifier = 0
    add_modifier = input("Do you want to add a modifier? (y/n) ")
    if add_modifier.lower() == 'y':
        modifier = int(input("Enter the modifier value: "))

    print(f"Rolling {num_dice} dice with {num_sides} sides each, with a {modifier:+} modifier...")
    rolls, total = roll_dice(num_dice, num_sides, modifier)
    for i, roll in enumerate(rolls):
        print(f"Roll {i+1}: {roll}")
    print(f"Total: {total}")
