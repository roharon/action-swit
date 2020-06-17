import json
import os
import requests

def main():
  WEBHOOKS_URL = os.environ.get("INPUT_WEBHOOKS_URL")
  MESSAGE = os.environ.get("INPUT_MESSAGE")

  if WEBHOOKS_URL == None or MESSAGE == None:
    return -1
  headers = {'Content-Type': 'application/json; charset=utf-8'}
  data = {
    'text': MESSAGE
  }

  res = requests.post(WEBHOOKS_URL, headers=headers, data=json.dumps(data))

if __name__ == "__main__":
  main()
