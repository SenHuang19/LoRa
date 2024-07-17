import serial
import time
import datetime
import requests


url = 'http://127.0.0.1:5000'
def find_between(sub1,sub2,test_str):
    idx1 = test_str.index(sub1)
    idx2 = test_str.index(sub2)
 
    res = ''
    # getting elements in between
    for idx in range(idx1 + len(sub1), idx2):
        res = res + test_str[idx]
    return res

serialPort = serial.Serial(
    port="COM4", baudrate=115200
)
serialString = ""  # Used to hold data coming over UART
s = 0
while 1:
    if serialPort.in_waiting > 0:
        serialString = serialPort.readline()
        strs = serialString.decode("Ascii")
        if strs.find('T=')!=-1:
            msg = find_between('T=','H',strs)
            result = requests.get('{0}/send_point'.format(url),headers={"Content-type":"application/json"},json = {'data': msg}).json()
            print(result)
            if result['payload']['update_set']:
                serialPort.write(bytes('AT+SEND=74,3,{},{}\r\n'.format(result['payload']['data_fre'],result['payload']['data_num']),encoding='utf8'))
        