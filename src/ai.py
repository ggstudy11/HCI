
import requests
import json
from model import model
from parameters import API_KEY, SECRET_KEY, HEADERS

def get_access_token():
    """
    使用 API Key，Secret Key 获取access_token，替换下列示例中的应用API Key、应用Secret Key
    """
        
    url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=" + API_KEY + "&client_secret=" + SECRET_KEY
    
    payload = json.dumps("")
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json().get("access_token")


def main():   

    demo = model()

    demo.transcribe("output3.wav")

    demo.getText()

    print("User: ", demo.text)

    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/yi_34b_chat?access_token=" + get_access_token()
    
    payload = json.dumps({
        "messages": [
            {
                "role": "user",
                "content": demo.text
            }
        ]
    })

    headers = HEADERS
    
    response = requests.request("POST", url, headers=headers, data=payload)

    result = response.json()["result"]
    print("bot: ", result)
    ##print(response["result"])
    

if __name__ == '__main__':
    main()