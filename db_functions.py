import sqlite3


def connect_database():
    """
    Creates the connection to the Database
    """
    conn = sqlite3.connect("app.db")
    return conn


def create_table_character():
    """
    Creates the Character table if it not exists
    """

    con = connect_database()
    cur = con.cursor()

    sql_create_character_table = """
        CREATE TABLE IF NOT EXISTS character (
        name TEXT NOT NULL,
        class TEXT NOT NULL,
        level INTEGER NOT NULL,
        life INTEGER NOT NULL,
        attack INTEGER NOT NULL,
        defense INTEGER NOT NULL,
        gold INTEGER NOT NULL,
        special_abilities TEXT NOT NULL,
        clues INTEGER NOT NULL,
        equipament TEXT NOT NULL
        )
    """

    cur.execute(sql_create_character_table)
    con.commit()
    con.close()


def save_character(new_character):
    """
    Adds a new character to the Database

    Args:
        new_character (tuple): character's name, stats, etc
    """

    con = connect_database()
    cur = con.cursor()

    sql_insert_character = """
        INSERT INTO character
        VALUES (?,
        ?,
        ?,
        ?,
        ?,
        ?,
        ?,
        ?,
        ?,
        ?)
    """

    cur.execute(sql_insert_character, new_character)
    con.commit()
    con.close()

    print(f"Saving {new_character[0]}")


def update_character(att_character):
    """
    Receives a tuple with the character's new information and
    updates it in the database using the name as a reference.

    Args:
        att_character (tuple): character new stats
    """

    con = connect_database()
    cur = con.cursor()

    sql_update_character = """
        UPDATE character
        SET level = ?,
            life = ?,
            attack = ?,
            defense = ?,
            gold = ?,
            special_abilities = ?,
            clues = ?,
            equipament = ?
        WHERE name = ?
    """

    cur.execute(sql_update_character, att_character)
    con.commit()
    con.close()


def select_character(character_name):
    """
    Select a character from the Database and returns a tuple with its stats

    Args:
        character_name (string): name of an existing character in the database

    Return:
        character_sheet (tuple): character stats
    """

    conn = connect_database()
    cur = conn.cursor()

    sql_select_character = """
        SELECT *
        FROM character
        WHERE name = ?
    """

    cur.execute(sql_select_character, (character_name,))
    character_sheet = cur.fetchone()
    conn.close()
    return character_sheet


def delete_character(character_name):
    """
    Select a character from the Database and delete its

    Args:
        character_name (string): name of an existing character in the database
    """

    con = connect_database()
    cur = con.cursor()

    sql_delete_character = """
        DELETE FROM character
        WHERE name = ?
    """

    cur.execute(sql_delete_character, (character_name,))
    con.commit()
    con.close()
