#!/usr/bin/env python
import sys
import requests
from veracode_api_signing.plugin_requests import RequestsAuthPluginVeracodeHMAC
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-vid", required=True, help="Veracode API ID")
parser.add_argument("-vkey", required=True, help="Veracode API KEY")
parser.add_argument("-scan", required=True, help="DAST Scan Profile Name")
parser.add_argument("-create", action='store_true', help="Creates a New DAST Scan Profile")
args = parser.parse_args()

api_base = "https://api.veracode.com/was/configservice/v1"

headers = {"User-Agent": "Start DA Scan Example", 'Content-type': 'application/json'}

#Payload for updating schedule of existing DA job to start now
data =   { 
    "schedule": 
        {       
            "now": True,
            "duration": 
                {
                "length": 3,
                "unit": "DAY"
                }
        }
}

if __name__ == "__main__":
    print("Looking for Dynamic Analysis Job: " + args.scan )
    #lookup_query = "name=" + "$(SCAN_NAME)"
    res = requests.get(api_base + "/analyses", auth=RequestsAuthPluginVeracodeHMAC(api_key_id=args.vid, api_key_secret=args.vkey), params={ "name": args.scan }, headers=headers)
    response = res.json()
    try:
        job_id = response['_embedded']['analyses'][0]['analysis_id']
        print("found job_id: " + job_id)
    except: 
        print("Could not find Dynamic Analysis")
        sys.exit(1)
    try:
        res = requests.put(api_base + "/analyses/" + job_id + '?method=PATCH', auth=RequestsAuthPluginVeracodeHMAC(api_key_id=args.vid, api_key_secret=args.vkey), json=data, headers=headers)
        
        if res.status_code == 204:
            print("Scan Submitted Successfully: " + str(res.status_code) )
        else:
            response = res.json()
            print("Error encountered: " + response['_embedded']['errors'][0]['detail'])
    except:
        print("Error executing API Call")
        sys.exit(1)
