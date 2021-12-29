import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import tkinter as tk
import numpy as np
import tkinter.ttk as ttk
from tkinter import *

types = ["All","Normal", "Grass", "Fire", "Water", "Electric", "Dark","Bug","Fairy","Fighting","Flying",
         "Steel","Poison","Rock","Ghost","Dragon","Ice","Ground","Psychic"]
types.sort()

def type_to_color(typ):
    if typ == "Normal":
        return "beige"
    elif typ == "Grass":
        return "green"
    elif typ == "Fire":
        return "orange"
    elif typ == "Water":
        return "blue"
    elif typ == "Electric":
        return "yellow"
    elif typ == "Dark":
        return "black"
    elif typ == "Bug":
        return "lightgreen"
    elif typ == "Fairy":
        return "#f0f8ff"
    elif typ == "Fighting":
        return "crimson"
    elif typ == "Flying":
        return "lavender"
    elif typ == "Steel":
        return "#aaaaaa"
    elif typ == "Poison":
        return "purple"
    elif typ == "Rock":
        return "tan"
    elif typ == "Ghost":
        return "#0070a0"
    elif typ == "Dragon":
        return "teal"
    elif typ == "Ground":
        return "brown"
    elif typ == "Ice":
        return "cyan"
    elif typ == "Psychic":
        return "fuchsia"

def filter_names(typ):
    if typ.get() == 'All':
        names = df['name'].values.tolist()
    else:
        names = df['name'][(df.type_1 == typ.get()) | (df.type_2 == typ.get())].values.tolist()
        dropdown.config(bg=type_to_color(typ.get()))
    names.sort()
    combobox["values"] = names
    combobox.current(0)

def get_graph(var):
    plt.clf()
    angles = [n / float(6) * 2 * 3.14159 for n in range(6)]
    angles += angles[:1]
    ax = plt.subplot(1,1,1, polar = True)
    ax.set_theta_offset(3.14159 / 2)
    ax.set_theta_direction(-1)
    ax.set_rlabel_position(30)
    plt.yticks([])
    plt.ylim(0,150)
    values = df.loc[df.name == var.get()][stats].values.tolist()
    typ = df.loc[df.name == var.get()]['type_1'].values.tolist()
    temp = values[0]
    temp2 = typ[0]
    temp.append(values[0][0])
    values = temp
    capped_values = values.copy()
    capped_values = [d if d < 150 else 150 for d in capped_values]
    clr = type_to_color(temp2)

    def add_stat_rating(hp_stat, values):
        labels = []
        string = ""
        if hp_stat >= 130:
            string = 'S+ '
        elif hp_stat < 130 and hp_stat >= 120:
            string = 'S '
        elif hp_stat < 120 and hp_stat >= 113:
            sting = 'A+ '
        elif hp_stat < 113 and hp_stat >= 106:
            string = 'A '
        elif hp_stat < 106 and hp_stat >= 100:
            string = 'A- '
        elif hp_stat < 100 and hp_stat >= 93:
            string = 'B+ '
        elif hp_stat < 93 and hp_stat >= 86:
            string = 'B '
        elif hp_stat < 86 and hp_stat >= 80:
            string = 'B- '
        elif hp_stat < 80 and hp_stat >= 73:
            string = 'C+ '
        elif hp_stat < 73 and hp_stat >= 66:
            string = 'C '
        elif hp_stat < 66 and hp_stat >= 60:
            string = 'C- '
        elif hp_stat < 60 and hp_stat >= 53:
            string = 'D+ '
        elif hp_stat < 53 and hp_stat >= 46:
            string = 'D '
        elif hp_stat < 46 and hp_stat >= 40:
            string = 'D- '
        else:
            string='F '
        string += str(hp_stat)
        labels.append(string)
        for value in values:
            if value >= 150:
                string = 'S+ '
            elif value < 150 and value >= 135:
                string  = 'S '
            elif value < 135 and value >= 128:
                string = 'A+ '
            elif value < 128 and value >= 119:
                string = 'A '
            elif value < 119 and value >= 111:
                string  = 'A- '
            elif value < 111 and value >= 103:
                string = 'B+ '
            elif value < 103 and value >= 94:
                string = 'B '
            elif value < 94 and value >= 86:
                string = 'B- '
            elif value < 86 and value >= 78:
                string = 'C+ '
            elif value < 78 and value >= 69:
                string  = 'C '
            elif value < 69 and value >= 61:
                string = 'C- '
            elif value < 61 and value >= 53:
                string = 'D+ '
            elif value < 53 and value >= 44:
                string = 'D '
            elif value < 44 and value >= 36:
                string = 'D- '
            else:
                string = 'F '
            string += str(value)
            labels.append(string)
        return labels
    
    hp_stat = values[0]
    labels = add_stat_rating(hp_stat, values[1:])
    for s in range(len(stats)):
        plt.text(angles[s],90, labels[s], size='large')

    plt.xticks(angles[:-1], stats, color='black', size=14)
    ax.tick_params(axis='x')

    for label, angle in zip(ax.get_xticklabels(), angles):
        if angle in (0, np.pi):
            label.set_horizontalalignment('center')
        elif 0 < angle < np.pi:
            label.set_horizontalalignment('left')
        else:
            label.set_horizontalalignment('right')

    ax.plot(angles, capped_values, linewidth=1, color='lightgreen', alpha=.5, linestyle='solid')
    ax.fill(angles, capped_values, color='lightgreen', alpha = .6)
    plt.title(var.get(), fontsize=20)

    plt.show()
    
root = Tk()
root.withdraw()
dropdown = Toplevel(root)
dropdown.geometry('600x600')
s= ttk.Style()
s.theme_use('alt')
variable = tk.StringVar(root)
type_variable = tk.StringVar(root)
type_variable.set("All")

df = pd.read_csv('pokemon.csv')
font_type = ("Sylfaen",24,"bold")

df = df.rename(columns={'hp':'HP',
                        'attack':'Attack',
                        'defense':'Defense',
                        'speed':'Speed',
                        'sp_attack':'Sp. Attack',
                        'sp_defense':'Sp. Defense'})

names = df['name'].values.tolist()
names.sort()

combobox = ttk.Combobox(dropdown, state='readonly', values = names, width = 30, height = 10, font=font_type, textvariable = variable)
combobox.current(0)
combobox.pack()
root.option_add('*TCombobox*Listbox.font', font_type)

graph = tk.Button(dropdown, bg='red', text="Get Graph", font=font_type, width=30, command=lambda: get_graph(variable)).pack()
stats = ["HP", "Attack", "Defense", "Speed","Sp. Defense", "Sp. Attack"]

typebox = ttk.Combobox(dropdown, state='readonly', values = types, width = 30, height = 10, font=font_type, textvariable = type_variable)   
typebox.current(0)
typebox.pack()
root.option_add('*TCombobox*Listbox.font', font_type)

filter_by_type = tk.Button(dropdown, bg='skyblue', text="Filter by Type", font=font_type, width=30, command=lambda: filter_names(type_variable)).pack()

get_graph(variable)
root.mainloop()








