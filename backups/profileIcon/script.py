'''
__author__      =       "Roberto Rocuant"
__version__     =       "3.0.0"
__created__     =       "03/27/2020 02:00"
'''


import json

with open('profileIcon.json') as profileIcon_file:
    profileIcon_list = json.load(profileIcon_file)

profileIcon_dict = {}
for number in profileIcon_list['data']: 
    profileIcon_dict.update({
        number: str(number)
    })

json_object = json.dumps(profileIcon_dict, indent = 4)
with open("profileIcon_dict.json", 'w') as json_write:
    json_write.write(json_object)

import requests as req
import shutil
#from tqdm.notebook import tqdm_notebook as tqdm

# for number in tqdm(profileIcon_list['data']):
for number in tqdm(profileIcon_list['data']):
    try:
        a = 'http://ddragon.leagueoflegends.com/cdn/10.6.1/img/profileicon/' + profileIcon_list['data'][number]['image']['full']
        path = 'profileIcon/' + str(number) + ".png"
        r = req.get(a)
        if r.status_code == 200:
            with open(path, 'wb') as f:
                for chunk in r:
                    f.write(chunk)
    except Exception as e:
        print(str(e))