'''
__author__      =       "Roberto Rocuant"
__version__     =       "3.0.0"
__created__     =       "03/27/2020 02:00"
'''


import json

with open('items_list.json') as items_file:
    items_list = json.load(items_file)
    
items_dict = {}
for number in items_list['data']: 
    items_dict.update({
        number: items_list['data'][number]['name']
    })

json_object = json.dumps(items_dict, indent = 4)
with open("items_dict.json", 'w') as json_write:
    json_write.write(json_object)

import requests as req
import shutil
#from tqdm.notebook import tqdm_notebook as tqdm

# for item in tqdm(items_list['data']):
for item in items_list['data']:
    try:
        ext = str(i) + '.png'
        a = 'http://ddragon.leagueoflegends.com/cdn/10.6.1/img/item/' + ext
        path = 'items/' + ext
        r = req.get(a)
        if r.status_code == 200:
            with open(path, 'wb') as f:
                for chunk in r:
                    f.write(chunk)
    except Exception as e:
        print(str(e))