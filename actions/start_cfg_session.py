import requests
import warnings
import time
import json

from st2client.models import KeyValuePair
from st2client.client import Client

from st2actions.runners.pythonrunner import Action

class startCfgSession(Action):
    def run(self, deviceIP, login, password):
        
        headers = {
            "accept": "application/json",
            "content-length": "0"
        }
        
        url_base = "https://" + deviceIP
        url = url_base + "/rest/conf/"

        print("\n")
        print("Sending REST call: POST " + url)

        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            cmd_response = requests.post(url, auth=(login, password), headers=headers, verify=False)
            cmd_response_code = cmd_response.status_code
            cmd_response_code = str(cmd_response_code)
            print("Response code: " + cmd_response_code)
        
        if cmd_response.status_code == 201:
            cmd_path = cmd_response.headers["Location"]
            print("Configuration ID: " + cmd_path)
            client = Client(base_url='http://localhost')
            client.keys.update(KeyValuePair(name='cmd_path_key', value=cmd_path))
            print("Configuration ID set in datastore with key name: cmd_path_key")