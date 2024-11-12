import tkinter as tk
from tkinter import ttk
from db_functions import delete_character, select_character, save_character

all_class = ['Barbarian', 'Cleric', 'Dwarf',
             'Elf', 'Halfling', 'Thief',
             'Warrior', 'Wizard']
root = tk.Tk()
root.title('4AD - Character Sheet Manager')

style = ttk.Style()


style.configure('TLabel', font=('Calibri', 13))
style.configure("TButton", font=("Helvetica", 11, "bold"),
                background='black', foreground='black', padding=10)


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
        ttk.Label(frm, text=text, style='TLabel').grid(
            column=col + ycol, row=row + xrow, sticky='E')


def make_entries(ycol, xrow, character_dict, character_dict_string_var):
    entries_items = [
        ('name', 1, 2, character_dict_string_var["name"]),
        ('level', 3, 2, character_dict_string_var["level"]),
        ('life', 3, 3, character_dict_string_var["life"]),
        ('attack', 1, 4, character_dict_string_var["attack"]),
        ('defense', 3, 4, character_dict_string_var["defense"]),
        ('clues', 1, 8, character_dict_string_var["clues"]),
        ('gold', 3, 8, character_dict_string_var["gold"])
    ]

    for key, col, row, var_string in entries_items:
        character_dict[key] = ttk.Entry(frm, textvariable=var_string)
        character_dict[key].grid(column=col + ycol, row=row + xrow, stick='W')


def make_combobox(ycol, xrow, character_dict, character_dict_string_var):
    combo_items = [
        ('class', 1, 3, character_dict_string_var['class'])
    ]
    for key, col, row, var_string in combo_items:
        character_dict[key] = ttk.Combobox(frm,
                                           textvariable=var_string,
                                           values=all_class)
        character_dict[key].grid(column=col + ycol,
                                 row=row + xrow, sticky='W')


def make_texts(ycol, xrow, character_dict):
    text_items = [
        ('special_abilities', 1, 5),
        ('equipament', 1, 7)
    ]

    for key, col, row in text_items:
        character_dict[key] = tk.Text(frm, width=55, height=3)
        character_dict[key].grid(column=col+ycol, sticky='W',
                                 row=row+xrow, columnspan=3)


def make_dict_string_var():
    return {
        "name": tk.StringVar(),
        "class": tk.StringVar(),
        "level": tk.StringVar(),
        "life": tk.StringVar(),
        "attack": tk.StringVar(),
        "defense": tk.StringVar(),
        "gold": tk.StringVar(),
        "special_abilities": tk.StringVar(),
        "clues": tk.StringVar(),
        "equipament": tk.StringVar()
    }


def window_new_character():

    clear_widgets()

    ttk.Label(frm, text="New Character").grid(
        column=1, row=0, columnspan=4)
    make_labels(0, 0)

    global new_character, new_character_string_var
    new_character = {}
    new_character_string_var = make_dict_string_var()

    make_entries(0, 0, new_character, new_character_string_var)
    make_texts(0, 0, new_character)
    make_combobox(0, 0, new_character, new_character_string_var)

    ttk.Button(frm, text="Save Character",
               command=prep_save_character).grid(column=1, row=9, pady=10)
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
        column=2, row=0, columnspan=4)
    make_labels(0, 0)
    make_labels(4, 0)
    make_labels(0, 10)
    make_labels(4, 10)

    global char_one, char_one_dict, char_one_dict_string_var
    global char_two, char_two_dict, char_two_dict_string_var
    global char_three, char_three_dict, char_three_dict_string_var
    global char_four, char_four_dict, char_four_dict_string_var

    char_one_dict_string_var = make_dict_string_var()
    char_two_dict_string_var = make_dict_string_var()
    char_three_dict_string_var = make_dict_string_var()
    char_four_dict_string_var = make_dict_string_var()
    char_one_dict = {}
    char_two_dict = {}
    char_three_dict = {}
    char_four_dict = {}

    ttk.Label(frm, text="#1 Character").grid(column=0, row=98)
    ttk.Label(frm, text="#2 Character").grid(column=2, row=98)
    ttk.Label(frm, text="#3 Character").grid(column=0, row=99)
    ttk.Label(frm, text="#4 Character").grid(column=2, row=99)

    ttk.Label(frm).grid(column=0, row=9)
    ttk.Label(frm).grid(column=0, row=10)
    ttk.Label(frm).grid(column=0, row=20)
    ttk.Label(frm).grid(column=0, row=21)
    char_one = ttk.Entry(frm)
    char_one.grid(column=1, row=98, pady=15)
    char_two = ttk.Entry(frm)
    char_two.grid(column=3, row=98, pady=15)
    char_three = ttk.Entry(frm)
    char_three.grid(column=1, row=99, pady=15)
    char_four = ttk.Entry(frm)
    char_four.grid(column=3, row=99, pady=15)

    make_entries(0, 0, char_one_dict, char_one_dict_string_var)
    make_combobox(0, 0, char_one_dict, char_one_dict_string_var)
    make_texts(0, 0, char_one_dict)

    make_entries(4, 0, char_two_dict, char_two_dict_string_var)
    make_combobox(4, 0, char_two_dict, char_two_dict_string_var)
    make_texts(4, 0, char_two_dict)

    make_entries(0, 9, char_three_dict, char_three_dict_string_var)
    make_combobox(0, 9, char_three_dict, char_three_dict_string_var)
    make_texts(0, 9, char_three_dict)

    make_entries(4, 9, char_four_dict, char_four_dict_string_var)
    make_combobox(4, 9, char_four_dict, char_four_dict_string_var)
    make_texts(4, 9, char_four_dict)

    ttk.Button(frm, text='Select Characters', command=update_party_entry).grid(
        column=7, row=99)
    ttk.Button(frm, text="Home",
               command=window_home).grid(column=7, row=100)
    ttk.Button(frm, text="Quit",
               command=root.destroy).grid(column=7, row=101)


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


def prep_save_character():
    new_character_infos = []

    new_character_infos.append(new_character["name"].get().title())
    new_character_infos.append(new_character["class"].get())
    new_character_infos.append(new_character["level"].get())
    new_character_infos.append(new_character["life"].get())
    new_character_infos.append(new_character["attack"].get())
    new_character_infos.append(new_character["defense"].get())
    new_character_infos.append(new_character["gold"].get())
    new_character_infos.append(new_character[
        "special_abilities"].get("1.0", tk.END).strip())
    new_character_infos.append(new_character["clues"].get())
    new_character_infos.append(new_character[
        "equipament"].get("1.0", tk.END).strip())

    save_character(new_character_infos)


def delete_old_character():
    character = old_character.get().title()
    delete_character(character)


def update_character_entry(character_dict, character_number_dict, character):

    character_dict['name'].set(character[0])
    character_dict['class'].set(character[1])
    character_dict['level'].set(character[2])
    character_dict['life'].set(character[3])
    character_dict['attack'].set(character[4])
    character_dict['defense'].set(character[5])
    character_dict['gold'].set(character[6])
    character_number_dict['special_abilities'].delete("1.0", tk.END)
    character_number_dict['special_abilities'].insert(tk.END, character[7])
    character_dict['clues'].set(character[8])
    character_number_dict['equipament'].delete("1.0", tk.END)
    character_number_dict['equipament'].insert(tk.END, character[9])


def update_party_entry():

    character_one = select_character(char_one.get().title())
    update_character_entry(char_one_dict_string_var,
                           char_one_dict, character_one)

    character_two = select_character(char_two.get().title())
    update_character_entry(char_two_dict_string_var,
                           char_two_dict, character_two)

    character_three = select_character(char_three.get().title())
    update_character_entry(char_three_dict_string_var,
                           char_three_dict, character_three)

    character_four = select_character(char_four.get().title())
    update_character_entry(char_four_dict_string_var,
                           char_four_dict, character_four)


window_home()
root.mainloop()
