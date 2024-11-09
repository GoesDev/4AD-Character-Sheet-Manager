from db_functions import select_character


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
