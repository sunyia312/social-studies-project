from random import randint
import tkinter as tk
import tkinter.font as font
import json
import os

num_to_role = {1: "Citizen", 2: "Woman", 3: "Slave"}
counter = 0


def on_entry_click(event):
    if event.widget.get() == "Type here...":
        event.widget.delete(0, "end") 
        event.widget.config(fg='black')

def get_entry(the_entry, root, button):
    canvas.delete(bb)
    canvas.config(width=0, height=0)
    canvas.pack_forget()
    label = tk.Label(root, text="", font=fontbasic, wraplength=450, bg="#90D1CA", fg="teal")
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
    proceed = tk.Button(root, text="OK!", command=lambda: next_scenario(label, proceed, root, role), bd=5, bg="green", fg="white")
    proceed.grid(row=1, column=0, columnspan=2)

def clear_fors2(c1, c2, label, data, sc, root, role):
    c1.destroy()
    c2.destroy()
    label.config(text=data[sc]["choices"][1][1])
    proceed = tk.Button(root, text="OK!", command=lambda: next_scenario(label, proceed, root, role), bd=5, bg="green", fg="white")
    proceed.grid(row=1, column=0, columnspan=2)

def next_scenario(label, proceed, root, role):
    proceed.destroy()
    game_loop(label, root, role)

def tkinter_death():
    system.destroy()
    exit()

def end_game(label, root, role):
    global canvas
    for widget in root.winfo_children():
        if widget != canvas:
            widget.destroy()
    canvas.config(width=img.width(), height=img.height())
    bb = canvas.create_image(0, 0, image=img, anchor="nw")

    # Keep a reference to avoid garbage collection
    canvas.bg = img

    # Optionally, add widgets over the image
    canvas.create_text(500, 130, text=f"You completed your journey as {num_to_role[role]}!", font=("Papyrus", 20), fill="white")
    exit_button = tk.Button(text="Exit Game", command=tkinter_death, relief="raised", bg="yellow", fg="black", bd=5)
    canvas.create_window(500, 500, window=exit_button)


def game_loop(label, root, role):
    global counter
    scenario = counter
    counter += 1
    if role == 1:
        if counter == 11:
            end_game(label, root, role)
            return -1
        script_dir = os.path.dirname(os.path.abspath(__file__))  # Folder of the script
        file_path = os.path.join(script_dir, "citizen.json")
        with open(file_path) as abc:
            data = json.load(abc)
    elif role == 2:
        if counter == 7:
            end_game(label, root, role)
            return -1
        script_dir = os.path.dirname(os.path.abspath(__file__))  # Folder of the script
        file_path = os.path.join(script_dir, "metic.json")
        with open(file_path) as xyz:
            data = json.load(xyz)
    elif role == 3:
        if counter == 11:
            end_game(label, root, role)
            return -1
        script_dir = os.path.dirname(os.path.abspath(__file__))  # Folder of the script
        file_path = os.path.join(script_dir, "slave.json")
        with open(file_path) as efg:
            data = json.load(efg)
    label.grid(row=0, column=0, columnspan=2, sticky="n")
    label.config(text=f"Current role: {num_to_role[role]}\n \n{data[scenario]["text"]}")
    print(data[scenario]["choices"][0][0])
    choice1 = tk.Button(root, text=data[scenario]["choices"][0][0], bg="red", fg="black", font=fontbasic2, bd=5, relief="raised")
    choice2 = tk.Button(root, text=data[scenario]["choices"][1][0], bg="navy", fg="white", font=fontbasic2, bd=5, relief="raised")
    choice1.config(command=lambda: clear_fors1(choice1, choice2, label, data, scenario, root, role))
    choice2.config(command=lambda: clear_fors2(choice1, choice2, label, data, scenario, root, role))
    choice1.grid(row=1, column=0, pady=5)
    choice2.grid(row=1, column=1, pady=5)




def ask_type(root):
    entry_1 = tk.Entry(root, bd=10, relief="raised")
    submit_button = tk.Button(root, text="Confirm", command=lambda: get_entry(entry_1, root, submit_button), bd=5, font=("Futura", 12))
    # choice.grid(row=0, column=0, columnspan=2)
    # entry_1.grid(row=1, column=0)
    # submit_button.grid(row=1, column=1)
    entry_1.insert(0, "Type here...")
    entry_1.bind('<FocusIn>', on_entry_click)
    canvas.create_window(400, 400, window=entry_1)
    canvas.create_window(700, 400, window=submit_button)

    

system = tk.Tk()
opacity = 0
def fade_in():
    global opacity
    opacity += 0.1
    system.attributes('-alpha', opacity)
    system.after(75, fade_in)  # Schedule next fade step
if opacity < 1:
    fade_in()

fontbasic = font.Font(family="Helvetica", size=12, weight="bold")
fontbasic2 = font.Font(family="Arial", size=10, weight="bold")
script_dir = os.path.dirname(os.path.abspath(__file__))  # Folder of the script
file_path = os.path.join(script_dir, "project_image.png")
img = tk.PhotoImage(file=file_path)

canvas = tk.Canvas(system, width=img.width(), height=img.height())
canvas.grid(row=0, column=0, columnspan=2)

# Add image to canvas
bb = canvas.create_image(0, 0, image=img, anchor="nw")

# Keep a reference to avoid garbage collection
canvas.bg = img

# Optionally, add widgets over the image
canvas.create_text(500, 160, text="Choose your role by typing its number: \n1 • Citizen  \n2 • Woman  \n3 • Slave\n", font=("Papyrus", 20), fill="white")



system.title("Project")
ask_type(system)

system.mainloop()