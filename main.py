import os
import json
from tkinter import *
from tkinter import filedialog, messagebox
from fn_file import *

setting = get_setting()

root = Tk()
# root.geometry("600x400")
root.title("fileNameChanger")
root.resizable(False, False)
title_label = Label(root, text='[file name changer]')
# title_label = Label(root, text='[file name changer]', borderwidth=2, relief="groove")

entry_path_data = Entry(root, width=30)
entry_path_in = Entry(root, width=30)
entry_path_out = Entry(root, width=30)
label_ext = Label(root, text='[ext]')
entry_ext = Entry(root, width=4)


# TODO - call initial dir from entry
def get_path_in():
    entry_path_in.delete(0, END)
    entry_path_in.insert(0, filedialog.askdirectory(initialdir=setting['path_in'], title="select folder"))

def get_path_out():
    entry_path_out.delete(0, END)
    entry_path_out.insert(0, filedialog.askdirectory(initialdir=setting['path_out'], title="select folder"))

def get_path_data():
    entry_path_data.delete(0, END)
    entry_path_data.insert(0, filedialog.askopenfilename(initialdir=setting['path_data'],
                                                         title="select json file", filetypes=[("JSON files", ".json")]))

def save_setting():
    setting['path_in'] = entry_path_in.get()
    setting['path_out'] = entry_path_out.get()
    setting['path_data'] = entry_path_data.get()
    setting['extension'] = entry_ext.get()
    try:
        with open('setting.json', 'w') as settingFile:
            json.dump(setting, settingFile)
    except IOError as ioe:
        messagebox.showerror(ioe)
    else:
        messagebox.showinfo('saved current setting')


btn_help_data = Button(root, text='[?]', overrelief=SOLID)
btn_path_data = Button(root, text='json data file', overrelief=SOLID, command=get_path_data)
btn_path_in = Button(root, text='input file path', overrelief=SOLID, command=get_path_in)
btn_path_out = Button(root, text='output file path', overrelief=SOLID, command=get_path_out)
btn_save = Button(root, text='setting save', overrelief=SOLID, command=save_setting)
btn_change = Button(root, text='file name change', overrelief=SOLID)

title_label.grid(row=0, column=0, padx=5, pady=5, columnspan=3, sticky=EW)
btn_path_data.grid(row=1, column=0, padx=5, pady=2, sticky=EW)
entry_path_data.grid(row=1, column=1, padx=5, pady=2)
btn_path_in.grid(row=2, column=0, padx=5, pady=2, sticky=EW)
entry_path_in.grid(row=2, column=1, padx=5, pady=2)
btn_path_out.grid(row=3, column=0, padx=5, pady=2, sticky=EW)
entry_path_out.grid(row=3, column=1, padx=5, pady=2)
btn_help_data.grid(row=1, column=2, padx=5, pady=2, sticky=EW)
label_ext.grid(row=2, column=2, padx=5, pady=2, sticky=EW)
entry_ext.grid(row=3, column=2, padx=5, pady=2)
btn_save.grid(row=4, column=0, padx=5, pady=2, sticky=EW)
btn_change.grid(row=4, column=1, columnspan=2, padx=5, pady=2, sticky=EW)

entry_path_in.insert(0, setting['path_in'])
entry_path_out.insert(0, setting['path_out'])
entry_path_data.insert(0, setting['path_data'])
entry_ext.insert(0, setting['extension'])

root.mainloop()
