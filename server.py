import json

from datetime import datetime as dts
import datetime
import pandas as pd
from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse
from time import gmtime, strftime
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)

update_set = False
data_fre = 1
data_num = 2

def update_data():
    with open("data.txt", "r") as file1:
        lines = file1.readlines()

    time = []
    data = []

    time.append(lines[0].split(',')[0])
    data.append(float(lines[0].split(',')[-1].replace('\n','')))

    start_date=time[0]

    start_date = dts.strptime(start_date, '%Y-%m-%dT%H:%M:%S')
    
    for i in range(1,len(lines)):
        strs = lines[i].split(',')
        end_date = strs[0]
        end_date = dts.strptime(end_date, '%Y-%m-%dT%H:%M:%S')
        dt = (end_date-start_date).seconds
        for j in range(1,len(strs)):
            time.append((start_date).strftime("%Y-%m-%dT%H:%M:%S"))
            data.append(float(strs[j]))
            start_date = start_date + datetime.timedelta(seconds = float(dt)/(len(strs)-1))
    jsons = {}
    jsons['date'] = time
    jsons['value'] = data
    return jsons

class settings(Resource):
    '''Interface to get the operation information from FRP.''' 
    def get(self):
        u = request.get_json(force=True)
        global update_set
        update_set = u['update_set']
        global data_fre
        data_fre = u['data_fre']
        global data_num
        data_num = u['data_num']        
        return {'status':200, 'message':None, 'payload':None}

class building_data(Resource):
    '''Interface to get the operation information from FRP.''' 
    def get(self):
        u = request.get_json(force=True)
        global update_set
        global data_fre
        global data_num
        now = strftime("%Y-%m-%dT%H:%M:%S", gmtime())
        data = now + ',' + u['data'].replace(' ','')
        with open("data.txt", "a") as file1:
            file1.writelines(data+'\n')
        update_set_hold = update_set
        if update_set:
            update_set = False
        return {'status':200, 'message':None, 'payload':{'update_set':update_set_hold,'data_fre':data_fre,'data_num':data_num}}

class process_data(Resource):
    '''Interface to get the operation information from FRP.''' 
    def get(self):
        output = update_data()
        return {'status':200, 'message':None, 'payload':output}

api.add_resource(building_data, '/send_point')
api.add_resource(process_data, '/get_point')
api.add_resource(settings, '/settings')


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=False)
