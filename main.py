import tkinter as tk
from tkinter import ttk
from Character import Character
from db_functions import delete_character

all_class = ['Barbarian', 'Cleric', 'Dwarf',
             'Elf', 'Halfling', 'Thief',
             'Warrior', 'Wizard']
root = tk.Tk()
root.title('4AD - Character Sheet Manager')
root.option_add("*Font", "Helvetica 10")

style = ttk.Style()
style.configure("TButton", font=("Helvetica", 11, "bold"))

frm = ttk.Frame(root, padding=10)
frm.grid()


def clear_widgets():
    for widget in frm.winfo_children():
        widget.destroy()


def window_new_character():

    clear_widgets()

    ttk.Label(frm, text="New Character").grid(
        column=1, row=0, columnspan=4)
    ttk.Label(frm, text="Name:").grid(column=0, row=2, sticky='E')
    ttk.Label(frm, text="Level:").grid(column=2, row=2, sticky='E')
    ttk.Label(frm, text="Class:").grid(column=0, row=3, sticky='E')
    ttk.Label(frm, text="Life:").grid(column=2, row=3, sticky='E')
    ttk.Label(frm, text="Attack Roll:").grid(column=0, row=4, sticky='E')
    ttk.Label(frm, text="Defense Roll:").grid(column=2, row=4, sticky='E')
    ttk.Label(frm, text="Abilities:").grid(column=0, row=5, sticky='E')
    ttk.Label(frm, text="Equipament:").grid(column=0, row=7, sticky='E')
    ttk.Label(frm, text="Clues:").grid(column=0, row=8, sticky='E')
    ttk.Label(frm, text="Gold:").grid(column=2, row=8, sticky='E')

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


def window_select_character():
    clear_widgets()

    ttk.Label(frm, text="Select Characters").grid(column=1, row=0)

    ttk.Label(frm, text='#1 Name:').grid(column=0, row=1)
    ttk.Label(frm, text='#2 Name:').grid(column=0, row=2)
    ttk.Label(frm, text='#3 Name:').grid(column=0, row=3)
    ttk.Label(frm, text='#4 Name:').grid(column=0, row=4)
    global char_one, char_two, char_three, char_four
    char_one = ttk.Entry(frm)
    char_one.grid(column=1, row=1)
    char_two = ttk.Entry(frm)
    char_two.grid(column=1, row=2)
    char_three = ttk.Entry(frm)
    char_three.grid(column=1, row=3)
    char_four = ttk.Entry(frm)
    char_four.grid(column=1, row=4)

    ttk.Button(frm, text='Select Character',
               command=select_existing_character).grid(column=1,
                                                       row=99, pady=20)

    ttk.Button(frm, text="Home",
               command=window_home).grid(column=99, row=99)


def window_home():

    clear_widgets()

    ttk.Button(frm, text="Create Character",
               command=window_new_character).grid(column=0, row=0)
    ttk.Button(frm, text="Delete Character",
               command=window_delete_character).grid(column=0, row=2)
    ttk.Button(frm, text="Select Character",
               command=window_select_character).grid(column=0, row=1)


def save_character():
    character = Character(new_character)
    character.save_new_character()


def delete_old_character():
    character = old_character.get()
    delete_character(character)


def select_existing_character():
    print(char_one.get(), char_two, char_three, char_four)


window_home()
root.mainloop()
