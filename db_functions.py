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
        hit_points INTEGER NOT NULL,
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


def create_chracter(new_character):
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


# kassandra = (
#     'kassandra',
#     'warrior',
#     1,
#     7,
#     1,
#     2,
#     5,
#     'None',
#     0,
#     '[Hand Weapon] Shortsword; [Armor] Hide Armor'
# )

# print(len(kassandra))
# create_chracter(kassandra)
# create_table_character()
