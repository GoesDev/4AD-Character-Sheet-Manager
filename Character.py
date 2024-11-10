from db_functions import save_character, update_character


class Character:

    def __init__(self, character):
        """
        Creates a new character object

        Args (character (dict)) - dict with character information.
        """

        self.name = character["name"]
        self.character_class = character["class"]
        self.level = character["level"]
        self.life = character["life"]
        self.attack = character["attack"]
        self.defense = character["defense"]
        self.gold = character["gold"]
        self.special_abilities = character["special_abilities"]
        self.clues = character["clues"]
        self.equipament = character["equipament"]

    def save_new_character(self):
        """
        Stores a new character's information in the database
        """

        # Creates a tuple that will be passed to the database
        # in a SQL execution.
        new_character = (
            self.name,
            self.character_class,
            self.level,
            self.life,
            self.attack,
            self.defense,
            self.gold,
            self.special_abilities,
            self.clues,
            self.equipament
        )
        save_character(new_character)

    def update_current_character(self, update_character_status):
        """
        Changes the character information, and calls the function to perform an
        UPDATE on the database.
        """

        self.level = update_character_status["level"]
        self.life = update_character_status["life"]
        self.attack = update_character_status["attack"]
        self.defense = update_character_status["defense"]
        self.gold = update_character_status["gold"]
        self.special_abilities = update_character_status["special_abilities"]
        self.clues = update_character_status["clues"]
        self.equipament = update_character_status["equipament"]

        character_new_status = (
            self.level,
            self.life,
            self.attack,
            self.defense,
            self.gold,
            self.special_abilities,
            self.clues,
            self.equipament,
            self.name
        )

        # Calling the function that updates the information in the Database,
        # sent a tuple as a parameter.
        update_character(character_new_status)
