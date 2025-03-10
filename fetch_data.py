import requests, json
from datetime import datetime, timezone
import uuid

headers = {"content-type": "application/json"}
baseUrl = "http://127.0.0.1:8000"


def addKey(key):
    url = f"{baseUrl}/api/add/"
    payload = {"key": key}
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    data = json.loads(response.content.decode("utf-8"))
    return data


def getKeys():
    url = f"{baseUrl}/api/keys/"

    response = requests.get(url)
    data = json.loads(response.content.decode("utf-8"))
    return data


def activateKey(key, account):
    url = f"{baseUrl}/api/update/{key}/"

    date = datetime.now(timezone.utc).isoformat()
    payload = {"account": account, "date": date}
    response = requests.put(url, data=json.dumps(payload), headers=headers)
    data = json.loads(response.content.decode("utf-8"))
    return data


def deleteKey(key):

    url = f"{baseUrl}/api/delete/{key}/"
    response = requests.delete(url)
    data = json.loads(response.content.decode("utf-8"))
    return data


def generate_activation_keys(n):
    for _ in range(n):
        key = str(uuid.uuid4())
        addKey(key)

    print(f"{n} activation keys generated and uploaded to database")


# print(activateKey("58c49f30-76b8-4b89-bd08-d2775ce62fa6", 6666))
# keys = getKeys()
# d = keys["keys"][1]["created"]

# diff = datetime.now(timezone.utc) - datetime.fromisoformat(d)
# print(diff.total_seconds() / 3600)

# generate_activation_keys(20)
# print(getKeys()["keys"])
keys = getKeys()
for key in keys:
    deleteKey(key["activation_key"])
