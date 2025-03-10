import requests, json
from datetime import datetime, timezone

headers = {"content-type": "application/json"}

baseUrl = "http://127.0.0.1:8000"  # "https://173.225.101.183"  #


def validate_and_register_key(key, account):

    # check if the key exist and unused
    keys = getKeys()
    for k in keys:
        if key == k["activation_key"] and k["account"] == None:
            # assign key
            return activateKey(key, account)

        if key == k["activation_key"] and k["account"] != None:
            # has been asigned
            return f"key has been assigned to account: {k['account']}"

    # invalid key
    return "Invalid Key"


def check_existing_key(account):
    # load keys
    account = str(account)
    keys = getKeys()
    for k in keys:
        if account == k["account"] and is_active(k):
            # active
            return "active"
        if account == k["account"] and not is_active(k):
            # expired
            return "Your Key has expired"

    # no key
    return "No key found for this account. Please provide a valid activation key."


def getKeys():
    # url = "http://127.0.0.1:5000/api/keys"
    url = f"{baseUrl}/api/keys/"

    response = requests.get(url)
    data = json.loads(response.content.decode("utf-8"))
    return data


def activateKey(key, account):
    # url = f"http://127.0.0.1:5000/api/update/{key}"
    url = f"{baseUrl}/api/update/{key}/"

    date = datetime.now(timezone.utc).isoformat()
    payload = {"account": account, "created": date}
    response = requests.put(url, data=json.dumps(payload), headers=headers)
    data = json.loads(response.content.decode("utf-8"))
    return data


def is_active(key):

    expiration_time = 1  # days

    # Check if the current time is past the expiration time
    created_time = datetime.fromisoformat(key["created"])
    time_elapsed = (datetime.now(timezone.utc) - created_time).total_seconds() / 86400
    return time_elapsed < expiration_time


# msg = check_existing_key(19106117)
# msg = validate_and_register_key("0b0804e8-425f-47ec-aab3-fa1d85701e59", 787867)
# print(msg)
