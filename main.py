import tkinter as tk
from tkinter import ttk
from Character import Character
from db_functions import delete_character, select_character

all_class = ['Barbarian', 'Cleric', 'Dwarf',
             'Elf', 'Halfling', 'Thief',
             'Warrior', 'Wizard']
root = tk.Tk()
root.title('4AD - Character Sheet Manager')
root.option_add("*Font", "Helvetica 10")

style = ttk.Style()
style.configure("TButton", font=("Helvetica", 11, "bold"))

global frm
frm = ttk.Frame(root, padding=10)
frm.grid()


def clear_widgets():
    for widget in frm.winfo_children():
        widget.destroy()


def make_labels(ycol, xrow):
    labels_texts = [
        ("Name:", 0, 2),
        ("Level:", 2, 2),
        ("Class:", 0, 3),
        ("Life:", 2, 3),
        ("Attack Roll:", 0, 4),
        ("Defense Roll:", 2, 4),
        ("Abilities:", 0, 5),
        ("Equipament:", 0, 7),
        ("Clues:", 0, 8),
        ("Gold:", 2, 8)
    ]

    for text, col, row in labels_texts:
        ttk.Label(frm, text=text).grid(
            column=col + ycol, row=row + xrow, sticky='E')


def window_new_character():

    clear_widgets()

    ttk.Label(frm, text="New Character").grid(
        column=1, row=0, columnspan=4)
    make_labels(0, 0)

    global new_character
    new_character = {}
    new_character['name'] = ttk.Entry(frm)
    new_character['name'].grid(column=1, row=2, sticky='W')
    new_character['level'] = ttk.Entry(frm)
    new_character['level'].grid(column=3, row=2, sticky='W')
    new_character['class'] = ttk.Combobox(frm, values=all_class)
    new_character['class'].grid(column=1, row=3, sticky='W')
    new_character['life'] = ttk.Entry(frm)
    new_character['life'].grid(column=3, row=3, sticky='W')
    new_character['attack'] = ttk.Entry(frm)
    new_character['attack'].grid(column=1, row=4, sticky='W')
    new_character['defense'] = ttk.Entry(frm)
    new_character['defense'].grid(column=3, row=4, sticky='W')
    new_character['special_abilities'] = tk.Text(frm, width=55, height=3)
    new_character['special_abilities'].grid(
        column=1, row=5, sticky='W', columnspan=3)
    new_character['equipament'] = tk.Text(frm, width=55, height=3)
    new_character['equipament'].grid(
        column=1, row=7, sticky='W', columnspan=3)
    new_character['clues'] = ttk.Entry(frm)
    new_character['clues'].grid(column=1, row=8, sticky='W')
    new_character['gold'] = ttk.Entry(frm)
    new_character['gold'].grid(column=3, row=8, sticky='W')

    ttk.Button(frm, text="Save Character",
               command=save_character).grid(column=1, row=9, pady=10)
    ttk.Button(frm, text="Home",
               command=window_home).grid(column=3, row=99)


def window_delete_character():

    clear_widgets()
    ttk.Label(frm, text="Delete Character").grid(column=1, row=0)

    ttk.Label(frm, text='Character Name:').grid(column=0, row=1)
    global old_character
    old_character = ttk.Entry(frm)
    old_character.grid(column=1, row=1)

    ttk.Button(frm, text='Delete Character',
               command=delete_old_character).grid(column=1, row=2, pady=20)
    ttk.Button(frm, text="Home",
               command=window_home).grid(column=99, row=99)


def window_show_party():
    clear_widgets()
    ttk.Label(frm, text="Party").grid(
        column=1, row=0, columnspan=4)
    make_labels(0, 0)

    global test_dict, char_name, char_class, char_level, char_life
    global char_gold, char_attack, char_defense, char_equipament, char_clues
    global char_special_abilities, char_one

    char_name = tk.StringVar()
    char_class = tk.StringVar()
    char_level = tk.StringVar()
    char_life = tk.StringVar()
    char_attack = tk.StringVar()
    char_defense = tk.StringVar()
    char_gold = tk.StringVar()
    char_special_abilities = tk.StringVar()
    char_clues = tk.StringVar()
    char_equipament = tk.StringVar()

    ttk.Label(frm, text="#1 Character").grid(column=0, row=98)
    ttk.Label(frm, text="#2 Character").grid(column=2, row=98)
    ttk.Label(frm, text="#3 Character").grid(column=0, row=99)
    ttk.Label(frm, text="#4 Character").grid(column=2, row=99)

    test_dict = {}
    char_one = ttk.Entry(frm)
    char_one.grid(column=1, row=98)
    char_two = ttk.Entry(frm)
    char_two.grid(column=3, row=98)
    char_three = ttk.Entry(frm)
    char_three.grid(column=1, row=99)
    char_four = ttk.Entry(frm)
    char_four.grid(column=3, row=99)

    test_dict['name'] = ttk.Entry(frm, textvariable=char_name)
    test_dict['name'].grid(column=1, row=2, sticky='W')
    test_dict['level'] = ttk.Entry(frm, textvariable=char_level)
    test_dict['level'].grid(column=3, row=2, sticky='W')
    test_dict['class'] = ttk.Combobox(
        frm, textvariable=char_class, values=all_class)
    test_dict['class'].grid(column=1, row=3, sticky='W')
    test_dict['life'] = ttk.Entry(frm, textvariable=char_life)
    test_dict['life'].grid(column=3, row=3, sticky='W')
    test_dict['attack'] = ttk.Entry(frm, textvariable=char_attack)
    test_dict['attack'].grid(column=1, row=4, sticky='W')
    test_dict['defense'] = ttk.Entry(frm, textvariable=char_defense)
    test_dict['defense'].grid(column=3, row=4, sticky='W')
    test_dict['special_abilities'] = tk.Text(frm, width=55, height=3)
    test_dict['special_abilities'].grid(
        column=1, row=5, sticky='W', columnspan=3)
    test_dict['equipament'] = tk.Text(frm, width=55, height=3)
    test_dict['equipament'].grid(
        column=1, row=7, sticky='W', columnspan=3)
    test_dict['clues'] = ttk.Entry(frm, textvariable=char_clues)
    test_dict['clues'].grid(column=1, row=8, sticky='W')
    test_dict['gold'] = ttk.Entry(frm, textvariable=char_gold)
    test_dict['gold'].grid(column=3, row=8, sticky='W')

    ttk.Button(frm, text='Select Characters', command=atualizar_entry).grid(
        column=99, row=99)


def window_home():

    clear_widgets()

    ttk.Button(frm, text="Create Character",
               command=window_new_character).grid(column=0, row=0)
    ttk.Button(frm, text="Delete Character",
               command=window_delete_character).grid(column=0, row=2)
    ttk.Button(frm, text="Select Character",
               command=window_show_party).grid(column=0, row=1)
    ttk.Button(frm, text="Quit",
               command=root.destroy).grid(column=0, row=99)


def save_character():
    definitive_character = {}

    definitive_character['name'] = new_character["name"].get()
    definitive_character['class'] = new_character["class"].get()
    definitive_character['level'] = new_character["level"].get()
    definitive_character['life'] = new_character["life"].get()
    definitive_character['attack'] = new_character["attack"].get()
    definitive_character['defense'] = new_character["defense"].get()
    definitive_character['gold'] = new_character["gold"].get()
    definitive_character['special_abilities'] = new_character[
        "special_abilities"].get("1.0", tk.END).strip()
    definitive_character['clues'] = new_character["clues"].get()
    definitive_character['equipament'] = new_character[
        "equipament"].get("1.0", tk.END).strip()

    my_character = Character(definitive_character)
    my_character.save_new_character()


def delete_old_character():
    character = old_character.get()
    delete_character(character)


def atualizar_entry():

    character = select_character(char_one.get().title())
    char_name.set(character[0])
    char_class.set(character[1])
    char_level.set(character[2])
    char_life.set(character[3])
    char_attack.set(character[4])
    char_defense.set(character[5])
    char_gold.set(character[6])
    test_dict['special_abilities'].delete("1.0", tk.END)
    test_dict['special_abilities'].insert(tk.END, character[7])
    char_clues.set(character[8])
    test_dict['equipament'].delete("1.0", tk.END)
    test_dict['equipament'].insert(tk.END, character[9])


window_home()
root.mainloop()
