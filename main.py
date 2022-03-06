import os
import json
from tkinter import *

try:
    with open('setting.json', 'r') as settingFile:
        setting = json.load(settingFile)
except:
    setting = dict()
    setting['inPath'] = 'in'
    setting['outPath'] = 'out'
    setting['extension'] = 'txt'


inPath = setting['inPath']
outPath = setting['outPath']
ext = setting['extension']

root = Tk()
# root.geometry("600x400")
root.title("fileNameChanger")
root.resizable(False, False)
titleLabel = Label(root, text='[file name changer]')
# titleLabel = Label(root, text='[file name changer]', borderwidth=2, relief="groove")

inPathButton = Button(root, text='input file path')
inPathEntry = Entry(root, width=30)
inPathEntry.insert(0, inPath)

outPathButton = Button(root, text='output file path')
outPathEntry = Entry(root, width=30)
outPathEntry.insert(0, outPath)

dataPathButton = Button(root, text='json data file')
dataPathEntry = Entry(root, width=30)
dataPathEntry.insert(0, outPath)

extPathLabel = Label(root, text='[ext]')
extPathEntry = Entry(root, width=4)
extPathEntry.insert(0, ext)

saveButton = Button(root, text='setting save')
changeButton = Button(root, text='file name change')

titleLabel.grid(row=0, column=0, padx=5, pady=5, columnspan=3, sticky="ew")
inPathButton.grid(row=1, column=0, padx=5, pady=2, sticky="ew")
inPathEntry.grid(row=1, column=1, padx=5, pady=2)
outPathButton.grid(row=2, column=0, padx=5, pady=2, sticky="ew")
outPathEntry.grid(row=2, column=1, padx=5, pady=2)
dataPathButton.grid(row=3, column=0, padx=5, pady=2, sticky="ew")
dataPathEntry.grid(row=3, column=1, padx=5, pady=2)
extPathLabel.grid(row=2, column=2, padx=5, pady=2, sticky="ew")
extPathEntry.grid(row=3, column=2, padx=5, pady=2)
saveButton.grid(row=4, column=0, padx=5, pady=2, sticky="ew")
changeButton.grid(row=4, column=1, columnspan=2, padx=5, pady=2, sticky="ew")

root.mainloop()
# data = {"inPath":"C:\Temp\in","outPath":"C:\Temp\out"}

# with open('setting.json', 'w') as fp:
#     json.dump(data, fp)


# for name in inNames:
#     fName = name[:-4]
#     if data.get(fName) != None :
#         chName = data.get(fName) + '.hwp'
#         print(fName + ' => change => ' + chName)
#         os.rename(inPath + '\\' + name , outPath + '\\' + chName)