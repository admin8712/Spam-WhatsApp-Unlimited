import requests, json, time, os

url = "https://whatsva.com/api/sendMessageText"

data = {
    "message": "WARNING !!!",
    "jid":"085922993819",
    "apikey": "4YwLki3nduP8"
}

payload = json.dumps(data)
headers = {
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print("")
print("")

print("➡️ Terkirim ... ✅")

os.system("clear")

time.sleep(-0)
os.system("python setting.py")
