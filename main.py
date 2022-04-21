import os
import json
from tkinter import *
from tkinter import filedialog, messagebox
from fn_file import *
from tooltip import *

setting = get_setting()

root = Tk()
# root.geometry("600x400")
root.title("fileNameChanger v1.0.0")
root.resizable(False, False)
# title_label = Label(root, text='[file name changer]')
# title_label = Label(root, text='[file name changer]', borderwidth=2, relief="groove")

entry_path_data = Entry(root, width=30)
entry_path_in = Entry(root, width=30)
entry_path_out = Entry(root, width=30)
label_ext = Label(root, text='[ext]')
entry_ext = Entry(root, width=4)
label_help_data = Label(root, text='[?]')
tooltip_help_data = CreateToolTip(label_help_data, str_help_data)


def get_path_in():
    init_dir = entry_path_in.get()
    get_dir = filedialog.askdirectory(initialdir=init_dir, title="select folder")
    if get_dir != "":
        entry_path_in.delete(0, END)
        entry_path_in.insert(0, get_dir)


def get_path_out():
    init_dir = entry_path_out.get()
    get_dir = filedialog.askdirectory(initialdir=init_dir, title="select folder")
    if get_dir != "":
        entry_path_out.delete(0, END)
        entry_path_out.insert(0, get_dir)


def get_path_data():
    init_dir = entry_path_data.get()
    get_file = filedialog.askopenfilename(initialdir=init_dir, title="select json file", filetypes=[("JSON files", ".json")])
    if get_file != "":
        entry_path_data.delete(0, END)
        entry_path_data.insert(0, get_file)


def save_setting():
    get_curr_setting()
    try:
        with open('setting.json', 'w') as settingFile:
            json.dump(setting, settingFile)
    except IOError as ioe:
        messagebox.showerror('error', ioe)
    else:
        messagebox.showinfo('inform', 'saved current setting')


def change_names():
    get_curr_setting()
    data = get_data(setting['path_data'])
    if data['result'] == 'success':
        in_names = data['data']
        extension = setting['extension']
        extension = '.' + extension if extension != "" else ""

        for before_name in in_names:
            after_name = in_names[before_name]
            os.rename(os.path.join(setting['path_in'], before_name + extension),
                      os.path.join(setting['path_out'], after_name + extension))
    elif data['result'] == 'error_json':
        messagebox.showerror('error', 'json format is not correct')
    elif data['result'] == 'error_io':
        messagebox.showerror('error', 'io error occurred')
    else:
        messagebox.showerror('error', 'unknown error occurred')


def get_curr_setting():
    setting['path_in'] = entry_path_in.get()
    setting['path_out'] = entry_path_out.get()
    setting['path_data'] = entry_path_data.get()
    setting['extension'] = entry_ext.get()


btn_path_data = Button(root, text='json data file', overrelief=SOLID, command=get_path_data)
btn_path_in = Button(root, text='input file path', overrelief=SOLID, command=get_path_in)
btn_path_out = Button(root, text='output file path', overrelief=SOLID, command=get_path_out)
btn_save = Button(root, text='setting save', overrelief=SOLID, command=save_setting)
btn_change = Button(root, text='change file\'s names', overrelief=SOLID, command=change_names)

# title_label.grid(row=0, column=0, padx=5, pady=5, columnspan=3, sticky=EW)
btn_path_data.grid(row=1, column=0, padx=5, pady=2, sticky=EW)
entry_path_data.grid(row=1, column=1, padx=5, pady=2)
btn_path_in.grid(row=2, column=0, padx=5, pady=2, sticky=EW)
entry_path_in.grid(row=2, column=1, padx=5, pady=2)
btn_path_out.grid(row=3, column=0, padx=5, pady=2, sticky=EW)
entry_path_out.grid(row=3, column=1, padx=5, pady=2)
label_help_data.grid(row=1, column=2, padx=5, pady=2, sticky=EW)
label_ext.grid(row=2, column=2, padx=5, pady=2, sticky=EW)
entry_ext.grid(row=3, column=2, padx=5, pady=2)
btn_save.grid(row=4, column=0, padx=5, pady=2, sticky=EW)
btn_change.grid(row=4, column=1, columnspan=2, padx=5, pady=2, sticky=EW)

entry_path_in.insert(0, setting['path_in'])
entry_path_out.insert(0, setting['path_out'])
entry_path_data.insert(0, setting['path_data'])
entry_ext.insert(0, setting['extension'])

root.mainloop()
