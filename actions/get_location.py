import requests
import warnings
import time
from st2client.client import Client
from st2client.models import KeyValuePair

from st2actions.runners.pythonrunner import Action

class getLocation(Action):
    def run(self, deviceIP, login, password, path):
        
        headers = {
            "accept": "application/json",
            "content-length": "0"
        }
              
        url_base = "https://" + deviceIP
        url = url_base + path

        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            cmd_response = requests.get(url, auth=(login, password), headers=headers, verify=False)
            cmd_response_code = cmd_response.status_code
            cmd_response_code = str(cmd_response_code)
            print("Response code: " + cmd_response_code)

        try:
            data = json.loads(cmd_response.text)
            print("Response body: ")
            print json.dumps(data, sort_keys=True, indent=4)
        except:
            print ("Response body is empty")