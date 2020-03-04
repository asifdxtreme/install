import sys
from asyncio import subprocess

import requests
import json


def dep_install(self):
    # token = subprocess.check_output([sys.executable, 'cat', '/run/secrets/kubernetes.io/serviceaccount/token'])
    # read token of serviceaccount from the file
    f = open("/run/secrets/kubernetes.io/serviceaccount/token", "r")
    token = f.read()

    # get information of cluster and pods based on labels
    session = requests.Session()
    session.verify = False
    header = {'Authorization': 'Bearer ' + token}
    url = 'https://kubernetes/api/v1/namespaces/default/pods?labelSelector=app%3Dspark-exec'
    response = session.get(url, headers=header)

    # extract podIP from json file
    data = json.loads(response.text)
    for item in data['items']:
        key = item['status']['podIP']
        url = 'http://'+key+':8088/api/v1/dep_install'
        resp = requests.post(url=url, data=json.dumps({'pkg': self}))
        print(resp)
