import os
import json
from tkinter import *

try:
    with open('setting.json', 'r') as settingFile:
        setting = json.load(settingFile)
except:
    setting = dict()
    setting['path_in'] = 'in'
    setting['path_out'] = 'out'
    setting['extension'] = 'txt'


path_in = setting['path_in']
path_out = setting['path_out']
ext = setting['extension']

root = Tk()
# root.geometry("600x400")
root.title("fileNameChanger")
root.resizable(False, False)
title_label = Label(root, text='[file name changer]')
# title_label = Label(root, text='[file name changer]', borderwidth=2, relief="groove")

btn_path_in = Button(root, text='input file path')
entry_path_in = Entry(root, width=30)
entry_path_in.insert(0, path_in)

btn_path_out = Button(root, text='output file path')
entry_path_out = Entry(root, width=30)
entry_path_out.insert(0, path_out)

btn_path_data = Button(root, text='json data file')
entry_path_data = Entry(root, width=30)
entry_path_data.insert(0, path_out)

label_ext = Label(root, text='[ext]')
entry_ext = Entry(root, width=4)
entry_ext.insert(0, ext)

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

root.mainloop()