import os
import json
from tkinter import *

try:
    with open('setting.json', 'r') as settingFile:
        setting = json.load(settingFile)
except:
    setting = dict()
    setting['inPath'] = ''
    setting['outPath'] = ''
    setting['extension'] = '.hwp'


inPath = setting['inPath']
outPath = setting['outPath']

root = Tk()
# root.geometry("600x400")
root.title("fileNameChanger")
root.resizable(False, False)
titleLabel = Label(root, text='[file name changer]')

inPathLabel = Label(root, text='input file path :')
inPathEntry = Entry(root, width=30)
inPathEntry.insert(0, inPath)

outPathLabel = Label(root, text='output file path :')
outPathEntry = Entry(root, width=30)
outPathEntry.insert(0, outPath)

dataPathLabel = Label(root, text='json data file :')
dataPathEntry = Entry(root, width=30)
dataPathEntry.insert(0, outPath)

titleLabel.grid(row=0, column=0, padx=5, pady=5, columnspan=3)
inPathLabel.grid(row=1, column=0, padx=5, pady=2)
inPathLabel.grid(sticky="e")
inPathEntry.grid(row=1, column=1, padx=5, pady=2, columnspan=2)
outPathLabel.grid(row=2, column=0, padx=5, pady=2)
outPathLabel.grid(sticky="e")
outPathEntry.grid(row=2, column=1, padx=5, pady=2, columnspan=2)
dataPathLabel.grid(row=3, column=0, padx=5, pady=2)
dataPathLabel.grid(sticky="e")
dataPathEntry.grid(row=3, column=1, padx=5, pady=2, columnspan=2)

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