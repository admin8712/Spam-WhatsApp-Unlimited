import requests, json ,os ,time

try:
  url = "https://whatsva.com/api/sendMessageText"
  data = {
    "message": "WARNING !!!",
    "jid":"TARUK DI SINI NOMOR WHATSAPP KORBAN BRO",
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

except:
  eror = ("\033[0;31m \n[x] Troubled-network !")
  os.system("clear")
  print ("\033[0;31m \nHidupkan Data Seluler Dan Jalan Kan Lagi Tools\n")
