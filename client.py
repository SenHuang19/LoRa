import requests


url = 'http://127.0.0.1:5000'




result = requests.get('{0}/settings'.format(url),
                      headers={"Content-type":"application/json"},
                      json = {'update_set': True,'data_fre':3,'data_num':2}).json()