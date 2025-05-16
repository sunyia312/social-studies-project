from time import sleep
from random import randint
import tkinter as tk
import json


start_game = 0
num_to_role = {1: "Citizen", 2: "Metic", 3: "Slave"}



def get_entry(the_entry, root, label, button):
    global start_game
    val = the_entry.get()
    label.config(text=f"You chose: {num_to_role[int(val)]}!", padx=100, pady=100)
    the_entry.destroy()
    button.destroy()
    root.update()
    root.after(2000)
    label.config(text=f"Put scenario here", padx=100, pady=20)
    game_loop(label, root)
    


def game_loop(label, root):
    scenario = randint(0, 1)
    with open("huh.json") as abc:
        data = json.load(abc)
    label.grid(row=0, column=0, columnspan=2, sticky="n")
    label.config(text=data[scenario]["text"])
    print(data[scenario]["choices"][0][0])
    choice1 = tk.Button(root, text=data[scenario]["choices"][0][0])
    choice2 = tk.Button(root, text=data[scenario]["choices"][1][0])
    choice1.grid(row=1, column=0)
    choice2.grid(row=1, column=1)




def ask_type(root):
    choice = tk.Label(root, text="Choose your role by typing its number: \n1 - Citizen  \n2 - Metic (Middle Class)  \n3 - Slave  \n4 - Woman\n ---\n")
    entry_1 = tk.Entry(root)
    submit_button = tk.Button(root, text="Confirm", command=lambda: get_entry(entry_1, root, choice, submit_button))
    choice.grid(row=0, column=0)
    entry_1.grid(row=1, column=0)
    submit_button.grid(row=1, column=1)

    

system = tk.Tk()
system.title("Project")
ask_type(system)

system.mainloop()