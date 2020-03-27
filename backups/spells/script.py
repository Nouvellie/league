'''
__author__      =       "Roberto Rocuant"
__version__     =       "3.0.0"
__created__     =       "03/27/2020 02:00"
'''


import json

with open('spells.json') as spells_file:
    spells_list = json.load(spells_file)

spells_dict = {}
for name in spells_list['data']: 
    spells_dict.update({
        spells_list['data'][name]['key']: spells_list['data'][name]['name']
    })

json_object = json.dumps(spells_dict, indent = 4)
with open("spells_dict.json", 'w') as json_write:
    json_write.write(json_object)

import requests as req
import shutil
#from tqdm.notebook import tqdm_notebook as tqdm
#for name in tqdm(spells_list['data']):
for name in spells_list['data']:
    
    try:
        ext = str(name) + '.png'
        a = 'http://ddragon.leagueoflegends.com/cdn/10.6.1/img/spell/' + ext
        path = 'spells/' + str(spells_list['data'][name]['key']) + ".png"
        r = req.get(a)
        if r.status_code == 200:
            with open(path, 'wb') as f:
                for chunk in r:
                    f.write(chunk)
    except Exception as e:
        print(str(e))