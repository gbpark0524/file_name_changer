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

def get_data(path_data):
    json_data = []
    try:
        with open(path_data, 'r') as file_json_data:
            json_data['data'] = json.load(file_json_data)
    except IOError:
        json_data['result'] = 'error'
    else:
        json_data['result'] = 'success'
    finally:
        return json_data
