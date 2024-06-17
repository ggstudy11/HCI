import requests
import random
import json
from parameters import API_KEY_2, SECRET_KEY_2

def get_access_token():

    url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=" + API_KEY_2 + "&client_secret=" + SECRET_KEY_2

    payload = json.dumps("")
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json().get("access_token")
    


def get_translatiton(q, lan):
    token = get_access_token()
    url = 'https://aip.baidubce.com/rpc/2.0/mt/texttrans/v1?access_token=' + token

    from_lang = 'zh' # example: en
    to_lang = lan # example: zh
    term_ids = '' # 术语库id，多个逗号隔开


    # Build request
    headers = {'Content-Type': 'application/json'}
    payload = {'q': q, 'from': from_lang, 'to': to_lang, 'termIds' : term_ids}
    r = requests.post(url, params=payload, headers=headers)
    result = r.json()
    dst_value = result["result"]["trans_result"][0]["dst"]
    print(result)
    return dst_value

