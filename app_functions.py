from db_functions import save_character, select_character


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

    save_character(new_chracter_data)


def select_existing_character(character_name):
    """
    Sends a character's name to a database query,
    and adds its information to a dict.

    Args:
        character_name (string): name of an existing character in the database

    Return:
        character (dict): receives a tuple, transfers it to a dict, returns it
    """

    character_sheet = select_character(character_name)

    character = {
        "name": character_sheet[0],
        "class": character_sheet[1],
        "level": character_sheet[2],
        "life": character_sheet[3],
        "attack": character_sheet[4],
        "defense": character_sheet[5],
        "gold": character_sheet[6],
        "special_abilities": character_sheet[7],
        "clues": character_sheet[8],
        "equipament": character_sheet[9]
    }

    return character
