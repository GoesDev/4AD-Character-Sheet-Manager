import tkinter as tk
from tkinter import ttk
from Character import Character
from db_functions import delete_character


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
    ttk.Label(frm, text="Name:").grid(column=1, row=2, sticky='E')
    ttk.Label(frm, text="Level:").grid(column=3, row=2, sticky='E')
    ttk.Label(frm, text="Class:").grid(column=1, row=3, sticky='E')
    ttk.Label(frm, text="Life:").grid(column=3, row=3, sticky='E')
    ttk.Label(frm, text="Attack Roll:").grid(column=1, row=4, sticky='E')
    ttk.Label(frm, text="Defense Roll:").grid(column=3, row=4, sticky='E')
    ttk.Label(frm, text="Abilities:").grid(column=1, row=5)
    ttk.Label(frm, text="Equipament:").grid(column=1, row=7)
    ttk.Label(frm, text="Clues:").grid(column=1, row=8)
    ttk.Label(frm, text="Gold:").grid(column=3, row=8)

    global new_character
    new_character = {}
    new_character['name'] = ttk.Entry(frm)
    new_character['name'].grid(column=2, row=2)
    new_character['level'] = ttk.Entry(frm)
    new_character['level'].grid(column=4, row=2)
    new_character['class'] = ttk.Entry(frm)
    new_character['class'].grid(column=2, row=3)
    new_character['life'] = ttk.Entry(frm)
    new_character['life'].grid(column=4, row=3)
    new_character['attack'] = ttk.Entry(frm)
    new_character['attack'].grid(column=2, row=4)
    new_character['defense'] = ttk.Entry(frm)
    new_character['defense'].grid(column=4, row=4)
    new_character['special_abilities'] = ttk.Entry(frm)
    new_character['special_abilities'].grid(column=2, row=5, columnspan=3,
                                            ipadx=300, padx=10, pady=10,
                                            ipady=20)
    new_character['equipament'] = ttk.Entry(frm)
    new_character['equipament'].grid(column=2, row=7, padx=10,
                                     pady=10, ipadx=300, ipady=50,
                                     columnspan=3)
    new_character['clues'] = ttk.Entry(frm)
    new_character['clues'].grid(column=2, row=8)
    new_character['gold'] = ttk.Entry(frm)
    new_character['gold'].grid(column=4, row=8)

    ttk.Button(frm, text="Save Character",
               command=save_character).grid(column=1, row=9)
    ttk.Button(frm, text="Home",
               command=window_home).grid(column=99, row=99)


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


def window_home():

    clear_widgets()

    ttk.Button(frm, text="Create Character",
               command=window_new_character).grid(column=0, row=0)
    ttk.Button(frm, text="Delete Character",
               command=window_delete_character).grid(column=0, row=1)


def save_character():
    character = Character(new_character)
    character.save_new_character()


def delete_old_character():
    character = old_character.get()
    delete_character(character)


window_home()
root.mainloop()
