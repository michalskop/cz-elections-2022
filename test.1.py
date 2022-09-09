"""Test."""

import requests

url = "https://api.ipify.org?format=json"

r = requests.get(url)

with open("test.1.txt", "a") as f:
  f.write(r.text + "\n")
