import requests
import warnings
import time
import json

from st2actions.runners.pythonrunner import Action

class commit(Action):
    def run(self, deviceIP, login, password, cmd_path):
        
        headers = {
            "accept": "application/json",
            "content-length": "0"
        }
             
        url_base = "https://" + deviceIP + "/" + cmd_path
        url = url_base + "/commit"

        print("\n")
        print("Sending REST call: POST " + url)

        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            cmd_response = requests.post(url, auth=(login, password), headers=headers, verify=False)
            cmd_response_code = cmd_response.status_code
            cmd_response_code = str(cmd_response_code)
            print("Response code: " + cmd_response_code)

        try:
            data = json.loads(cmd_response.text)
            print("Response body: ")
            print json.dumps(data, sort_keys=True, indent=4)
        except:
            print ("Response body is empty")

        #if cmd_response.status_code == 200:
        #    cmd_response_length = cmd_response.headers['content-length']
        #    cmd_response_length = int(cmd_response_length)
        #    if cmd_response_length != 0
        #        data = json.loads(cmd_response.text)
        #        print("Response body: ")
        #        print json.dumps(data, sort_keys=True, indent=4)