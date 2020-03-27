'''
__author__      =       "Roberto Rocuant"
__version__     =       "3.0.0"
__created__     =       "03/27/2020 02:00"
'''


import json

with open('champions.json') as champions_file:
    champions_list = json.load(champions_file)
    
champions_dict = {}
for name in champions_list['data']: 
    champions_dict.update({
        champions_list['data'][name]['key']: name
    })

json_object = json.dumps(champions_dict, indent = 4)
with open("champions_dict.json", 'w') as json_write:
    json_write.write(json_object)

import requests as req
import shutil
#from tqdm.notebook import tqdm_notebook as tqdm

# for name in tqdm(champions_list['data']):
for name in champions_list['data']:
    
    try:
        ext = str(name) + '.png'
        a = 'http://ddragon.leagueoflegends.com/cdn/10.6.1/img/champion/' + ext
        path = 'champions/' + str(champions_list['data'][name]['key']) + ".png"
        r = req.get(a)
        if r.status_code == 200:
            with open(path, 'wb') as f:
                for chunk in r:
                    f.write(chunk)
    except Exception as e:
        print(str(e))