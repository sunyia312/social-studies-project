from random import randint
import tkinter as tk
import tkinter.font as font
import json
import os


num_to_role = {1: "Citizen", 2: "Woman", 3: "Slave"}
counter = 0

def get_entry(the_entry, root, label, button):
    val = the_entry.get()
    label.config(text=f"You chose: {num_to_role[int(val)]}!", padx=100, pady=100)
    the_entry.destroy()
    button.destroy()
    root.update()
    root.after(2000)
    # label.config(text=f"Put scenario here", padx=100, pady=20)
    game_loop(label, root, int(val))

def clear_fors1(c1, c2, label, data, sc, root, role):
    c1.destroy()
    c2.destroy()
    label.config(text=data[sc]["choices"][0][1])
    proceed = tk.Button(root, text="OK", command=lambda: next_scenario(label, proceed, root, role))
    proceed.grid(row=1, column=0, columnspan=2)

def clear_fors2(c1, c2, label, data, sc, root, role):
    c1.destroy()
    c2.destroy()
    label.config(text=data[sc]["choices"][1][1])
    proceed = tk.Button(root, text="OK", command=lambda: next_scenario(label, proceed, root, role))
    proceed.grid(row=1, column=0, columnspan=2)

def next_scenario(label, proceed, root, role):
    proceed.destroy()
    game_loop(label, root, role)


    


def game_loop(label, root, role):
    global counter
    scenario = counter
    counter += 1
    if role == 1:
        script_dir = os.path.dirname(os.path.abspath(__file__))  # Folder of the script
        file_path = os.path.join(script_dir, "citizen.json")
        with open(file_path) as abc:
            data = json.load(abc)
    elif role == 2:
        script_dir = os.path.dirname(os.path.abspath(__file__))  # Folder of the script
        file_path = os.path.join(script_dir, "metic.json")
        with open("metic.json") as xyz:
            data = json.load(xyz)
    elif role == 3:
        script_dir = os.path.dirname(os.path.abspath(__file__))  # Folder of the script
        file_path = os.path.join(script_dir, "slave.json")
        with open("slave.json") as efg:
            data = json.load(efg)
    label.grid(row=0, column=0, columnspan=2, sticky="n")
    label.config(text=data[scenario]["text"])
    print(data[scenario]["choices"][0][0])
    choice1 = tk.Button(root, text=data[scenario]["choices"][0][0])
    choice2 = tk.Button(root, text=data[scenario]["choices"][1][0])
    choice1.config(command=lambda: clear_fors1(choice1, choice2, label, data, scenario, root, role))
    choice2.config(command=lambda: clear_fors2(choice1, choice2, label, data, scenario, root, role))
    choice1.grid(row=1, column=0)
    choice2.grid(row=1, column=1)




def ask_type(root):
    choice = tk.Label(root, text="Choose your role by typing its number: \n1 - Citizen  \n2 - Woman  \n3 - Slave\n ---\n", font=fontbasic, wraplength=450, image=img)
    entry_1 = tk.Entry(root)
    submit_button = tk.Button(root, text="Confirm", command=lambda: get_entry(entry_1, root, choice, submit_button))
    choice.grid(row=0, column=0)
    entry_1.grid(row=1, column=0)
    submit_button.grid(row=1, column=1)

    

system = tk.Tk()
fontbasic = font.Font(family="Helvetica", size=12, weight="bold")
script_dir = os.path.dirname(os.path.abspath(__file__))  # Folder of the script
file_path = os.path.join(script_dir, "project_image.png")
img = tk.PhotoImage(file=file_path)
system.title("Project")
ask_type(system)

system.mainloop()