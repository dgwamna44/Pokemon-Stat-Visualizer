import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import tkinter as tk
import numpy as np
import tkinter.ttk as ttk
from tkinter import *
from PIL import Image, ImageTk

active_type = "None"
active_stat = "None"

types = ["Normal", "Grass", "Fire", "Water", "Electric", "Dark","Bug","Fairy","Fighting","Flying",
         "Steel","Poison","Rock","Ghost","Dragon","Ice","Ground","Psychic"]
stats = ["HP", "Attack", "Defense", "Speed","Sp. Defense", "Sp. Attack"]
types.sort()

df = pd.read_csv('pokemon.csv')
font_type = ("Calibri",24)
font_type_stat = ("Calibri", 20)


df = df.rename(columns={'hp':'HP',
                        'attack':'Attack',
                        'defense':'Defense',
                        'speed':'Speed',
                        'sp_attack':'Sp. Attack',
                        'sp_defense':'Sp. Defense'})

master_list = df['name'].values.tolist()
master_list.sort()

for stat in stats:
    df["pct_"+stat] = round((df[stat].rank(pct = True)) * 100,1)

def type_to_color(typ):  #generate a color based on selected type to change background of selection screen
    if typ == "Normal":
        return "beige"
    elif typ == "Grass":
        return "#00f000"
    elif typ == "Fire":
        return "orange"
    elif typ == "Water":
        return "blue"
    elif typ == "Electric":
        return "yellow"
    elif typ == "Dark":
        return "#606060"
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

def filter_names(typ): # filters list of names based on type.
    global master_list
    global active_type
    global active_stat
    active_type = typ.get()
    if active_stat != "None":
        master_list = df.sort_values(active_stat, ascending=False)['name'][(df.type_1 == active_type) | (df.type_2 == active_type)].values.tolist()
    else:
        master_list = df['name'][(df.type_1 == typ.get()) | (df.type_2 == typ.get())].values.tolist()
    master_list.sort()
    combobox["values"] = master_list
    combobox.current(0)
    dropdown.config(bg=type_to_color(typ.get())) # Generates list from either type_1 or type_2
    filter_type.config(bg=type_to_color(typ.get()))
    sort_by_stat.config(bg=type_to_color(typ.get()))

def sort_stat(stat):
    global active_type
    global active_stat
    active_stat = stat.get()
    if active_type != "None":
        master_list = df.sort_values(active_stat, ascending=False)['name'][(df.type_1 == active_type) | (df.type_2 == active_type)].values.tolist()
    else:
        master_list = df.sort_values(active_stat, ascending=False)['name'].values.tolist()
    combobox["values"] = master_list
    combobox.current(0)

def get_graph(var):
    plt.clf()
    plt.subplots_adjust(top=.8)
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

    def add_stat_rating(hp_stat, values): # applies a rating based on stat
        labels = []
        string = ""
        if hp_stat >= 130: # HP stat is slightly positively skewed compared to the other stats, hence
            # the different rating scale
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
    filename = 'plot.png'
    plt.savefig(filename)
    show_data()
    load = Image.open(filename)
    render = ImageTk.PhotoImage(load)
    plot = tk.Label(dropdown, image =  render, bg='white')
    plot.image = render
    plot.place(x=600, y=0, width=600, height=600)
    
root = Tk()
root.withdraw()
dropdown = Toplevel(root)
dropdown.geometry('1200x1000')
dropdown.config(bg='white')
s= ttk.Style()
s.theme_use('alt')
name = tk.StringVar(root)
show_stats = tk.BooleanVar(root)
show_types = tk.BooleanVar(root)
type_variable = tk.StringVar(root)
stat_variable = tk.StringVar(root)
type_variable.set("All")

combobox = ttk.Combobox(dropdown, state='readonly', values = master_list, width = 30, height = 10, font=font_type, textvariable = name)
combobox.current(0)
combobox.place(x=0, y=400)
combobox.pack(anchor=W)
root.option_add('*TCombobox*Listbox.font', font_type)

graph = tk.Button(dropdown, bg='red', text="Get Graph", font=font_type, width=27, command=lambda: get_graph(name)).pack(anchor=W)

typebox = ttk.Combobox(dropdown, state='readonly', values = types, width = 30, font=font_type, textvariable = type_variable)   
root.option_add('*TCombobox*Listbox.font', font_type)

filter_by_type = tk.Button(dropdown, bg='skyblue', text="Filter by Type", font=font_type, width=27, command=lambda: filter_names(type_variable))

def show_statbox():
    global active_stat
    global active_type
    if show_stats.get():
        statbox.pack(anchor=W)
        statbox.current(0)
        active_stat = stat_variable.get()
        statbox_button.pack(anchor=W)
    else:
        statbox.pack_forget()
        statbox_button.pack_forget()
        active_stat = "None"
        if active_type != 'None':
            master_list = df['name'][(df.type_1 == active_type) | (df.type_2 == active_type)] .values.tolist()
        else:
            master_list = df['name'].values.tolist()
        combobox['values'] = master_list

def show_typebox():
    global active_type
    global active_stat
    if show_types.get():
        typebox.pack(anchor=W)
        typebox.current(0)
        active_type = type_variable.get()
        filter_by_type.pack(anchor=W)
    else: #reset to unfiltered list
        typebox.pack_forget()
        filter_by_type.pack_forget()
        active_type = "None"
        if active_stat != "None":
            master_list = df.sort_values(active_stat, ascending=False)['name'].values.tolist()
        else:
            master_list = df['name'].values.tolist()
        master_list.sort()
        combobox["values"] = master_list
        combobox.current(0)
        filter_type.config(bg='white')
        sort_by_stat.config(bg='white')
        dropdown.config(bg='white')
        textbox.config(bg='white')

def show_data():
    textbox.delete('1.0', tk.END)
    name = combobox.get()
    textbox.insert(tk.END, name+"'s Stat Information:" + "\n" + "\n")
    for stat in stats:
       stat_pct = str("pct_"+stat)
       percentage = str(df[stat_pct][df.name == name].values)
       percentage = percentage.strip('[]')
       textbox.insert(tk.END, stat + " Percentile: \t ")
       textbox.insert(tk.END, percentage + "%" +"\n")
       

filter_type = tk.Checkbutton(dropdown, text="Filter By Types", font=font_type_stat, command=show_typebox, variable=show_types, onvalue=1, offvalue=0, bg='white')
filter_type.pack(anchor=W)

sort_by_stat = tk.Checkbutton(dropdown, text="Sort By Stats", font=font_type_stat, command=show_statbox, variable=show_stats, onvalue=1, offvalue=0, bg='white')
sort_by_stat.pack(anchor=W)

statbox = ttk.Combobox(dropdown, state='readonly', values = stats, width = 30, height = 10, font=font_type, textvariable = stat_variable)   
statbox.current(0)
root.option_add('*TCombobox*Listbox.font', font_type)
statbox_button = tk.Button(dropdown, bg='lightgreen', text="Sort", font=font_type, width=27, command=lambda: sort_stat(stat_variable))

textbox = tk.Text(dropdown, font=font_type_stat, bg='white')
textbox.place(x=0, y=600, width=1200, height=350)

get_graph(name)
show_data()
root.mainloop()
