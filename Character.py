from db_functions import save_character, update_character


class Character:

    def __init__(self, character):
        """
        Cria o objeto de um novo personagem

        Args (character (dict)) - dicionário com as informações do personagem.
        """

        self.name = character["name"]
        self.character_class = character["class"]
        self.level = character["level"]
        self.life = character["life"]
        self.attack = character["attack"]
        self.defense = character["defense"]
        self.gold = character["gold"]
        self.special_abilities = character["special_abilities"]
        self.special_abilities_uses = character["special_abilities_uses"]
        self.clues = character["clues"]
        self.equipament = character["equipament"]

    def save_new_character(self):
        """
        Armazena as informações de um novo personagem no banco de dados
        """

        # Cria a tupla que será passada para o banco em uma execução sql
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
        Altera as informações do personagem, e chama a função para dar um
        UPDATE no banco de dados.
        """

        self.level = update_character_status["level"],
        self.life = update_character_status["life"],
        self.attack = update_character_status["attack"],
        self.defense = update_character_status["defense"],
        self.gold = update_character_status["gold"],
        self.special_abilities = update_character_status["special_abilities"],
        self.clues = update_character_status["clues"],
        self.equipament = update_character_status["equipament"],

        # Chamando a função que atualiza as informações no banco,
        # enviado a tupla como parâmetro
        update_character(update_character_status)
