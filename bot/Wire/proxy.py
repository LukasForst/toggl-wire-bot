import json

import requests

from Utils.systemUtils import getRomanURL


def sendMessage(token: str, message: any) -> str:
    url = getRomanURL()
    print(f"Sending to {url}")
    print(message)
    r = requests.post(f"{url}/conversation", data=json.dumps(message),
                      headers={"content-type": "application/json", "Authorization": f"Bearer {token}"})
    print(r.json())
    return r.json()
