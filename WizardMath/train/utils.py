import json
def jload(path):
    fr = open(path, 'r')
    d = json.load(fr)
    return d
