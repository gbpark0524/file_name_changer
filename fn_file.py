import json


def get_setting():
    try:
        with open('setting.json', 'r') as settingFile:
            setting = json.load(settingFile)
    except IOError:
        setting = dict()
        setting['path_in'] = 'in'
        setting['path_out'] = 'out'
        setting['extension'] = 'txt'

    return setting

