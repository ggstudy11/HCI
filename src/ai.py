
import requests
import json
from parameters import API_KEY, SECRET_KEY, HEADERS

def get_access_token():

    url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=" + API_KEY + "&client_secret=" + SECRET_KEY

    payload = json.dumps("")
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json().get("access_token")
def get_response(question):   

    print("User: ", question)
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/yi_34b_chat?access_token=" + get_access_token()
    payload = json.dumps({
        "messages": [
            {
                "role": "user",
                "content": question
            }
        ]
    })
    headers = HEADERS
    
    response = requests.request("POST", url, headers=headers, data=payload)
    
    if response:
        result = response.json()["result"]
        print("bot: ", result)

    return result
    
