import requests
import json


def dep_install(self):
    resp = requests.post('http://127.0.0.1:8088/api/v1/dep_install', data=json.dumps({'pkg': self}))
    print(resp)
