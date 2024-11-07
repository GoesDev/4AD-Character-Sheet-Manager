from Character import Character


kassandra = {
    'name': 'Kassandra',
    'class': 'Cleric',
    'level': 1,
    'life': 7,
    'attack': 1,
    'defense': 0,
    'gold': 3,
    'special_abilities': 'No Abilities',
    'special_abilities_uses': 0,
    'clues': 0,
    'equipament': '[Hand Weapon] Shortsword -- [Armor] Hide Armor'
}


new_character = Character(kassandra)

if new_character:
    choice = input("Confirm?")
    if choice == '1':
        new_character.save_new_character()
    else:
        print("Failed")
