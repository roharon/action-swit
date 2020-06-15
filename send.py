import os
import requests

def main():
  WEBHOOKS_URL = os.environ["INPUT_WEBHOOKS_URL"]
  MESSAGE = os.environ["INPUT_MESSAGE"]

  data = {
    'text': MESSAGE
  }

  res = requests.post(WEBHOOKS_URL, json=data)

if __name__ == "__main__":
  main()
