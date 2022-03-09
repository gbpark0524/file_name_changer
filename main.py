import os
import json
from tkinter import *
from tkinter import filedialog
from fn_file import *


root = Tk()
# root.geometry("600x400")
root.title("fileNameChanger")
root.resizable(False, False)
title_label = Label(root, text='[file name changer]')
# title_label = Label(root, text='[file name changer]', borderwidth=2, relief="groove")

btn_path_in = Button(root, text='input file path')
entry_path_in = Entry(root, width=30)
btn_path_out = Button(root, text='output file path')
entry_path_out = Entry(root, width=30)
btn_path_data = Button(root, text='json data file')
entry_path_data = Entry(root, width=30)
label_ext = Label(root, text='[ext]')
entry_ext = Entry(root, width=4)
btn_save = Button(root, text='setting save')
btn_change = Button(root, text='file name change')

title_label.grid(row=0, column=0, padx=5, pady=5, columnspan=3, sticky="ew")
btn_path_in.grid(row=1, column=0, padx=5, pady=2, sticky="ew")
entry_path_in.grid(row=1, column=1, padx=5, pady=2)
btn_path_out.grid(row=2, column=0, padx=5, pady=2, sticky="ew")
entry_path_out.grid(row=2, column=1, padx=5, pady=2)
btn_path_data.grid(row=3, column=0, padx=5, pady=2, sticky="ew")
entry_path_data.grid(row=3, column=1, padx=5, pady=2)
label_ext.grid(row=2, column=2, padx=5, pady=2, sticky="ew")
entry_ext.grid(row=3, column=2, padx=5, pady=2)
btn_save.grid(row=4, column=0, padx=5, pady=2, sticky="ew")
btn_change.grid(row=4, column=1, columnspan=2, padx=5, pady=2, sticky="ew")

setting = get_setting()
entry_path_in.insert(0, setting['path_in'])
entry_path_out.insert(0, setting['path_out'])
entry_ext.insert(0, setting['extension'])

def get_path_in(event):
    entry_path_in.delete(0, END)
    entry_path_in.insert(0, filedialog.askdirectory(initialdir="/", title="select folder"))

def get_path_out(event):
    entry_path_out.delete(0, END)
    entry_path_out.insert(0, filedialog.askdirectory(initialdir="/", title="select folder"))

def get_path_data(event):
    entry_path_data.delete(0, END)
    entry_path_data.insert(0, filedialog.askopenfilename(initialdir="/",
                                                         title="select json file", filetypes=[("JSON files", ".json")]))


btn_path_in.bind('<Button-1>', get_path_in)
btn_path_out.bind('<Button-1>', get_path_out)
btn_path_data.bind('<Button-1>', get_path_data)

root.mainloop()
