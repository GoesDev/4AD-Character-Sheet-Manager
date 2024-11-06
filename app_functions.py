from db_functions import create_chracter


def new_character():
    """
    Receives user information to create a new character
    """
    print("Let's create a character in 4AD")
    character_name = input("Name: ")
    character_class = input("Class: ")
    character_level = input("Level: ")
    new_chracter_data = (
        character_name.lower(),
        character_class.lower(),
        character_level.lower(),
        7,
        1,
        2,
        5,
        'None',
        0,
        '[Hand Weapon] Shortsword; [Armor] Hide Armor'
        )

    create_chracter(new_chracter_data)


new_character()
