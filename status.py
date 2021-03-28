import requests
import time
import json

url = "https://discord.com/api/v8/users/@me/settings"

try:
    delay = float(input("delay per each time changed? =>\t"))
except ValueError:
    print("put a number in lol")
else:

    with open('token.json') as f:
        config = json.load(f)

    token = config.get('token')

    if config.get('token') == "token-here":
            print("did you put your token in the token.json file")
    else:

        tokenv = {"Authorization": token}
        valid = requests.get("https://discord.com/api/v8/users/@me/settings", headers=tokenv)
        if valid.status_code == 401:
            print("invalid token!")
        else:

            headers = {
                'Authorization': token,
                'Content-Type': 'application/json'
            }

            def main():
                print("{+} Changing Status! {+}")
                while True:
                    with open("status.txt", "r") as s:
                        for stat in s:
                            status = stat.strip()
                            status_data = ({'custom_status': {'text': status}})
                            requests.patch(url, headers=headers, json=status_data)
                            time.sleep(delay)


            if __name__== "__main__": 
                main()
