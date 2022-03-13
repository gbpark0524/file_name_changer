import json
import os


def get_setting():
    try:
        with open('setting.json', 'r') as settingFile:
            setting = json.load(settingFile)
    except IOError:
        dir_in = os.path.join(os.curdir, 'in')
        dir_out = os.path.join(os.curdir, 'out')

        setting = dict()
        setting['path_in'] = dir_in
        setting['path_out'] = dir_out
        setting['path_data'] = os.curdir
        setting['extension'] = 'txt'

    return setting
