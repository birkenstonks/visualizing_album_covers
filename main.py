import os
import requests
import base64


CLIENT_ID_PATH = os.path.expanduser("~/.spotify/client_id")
CLIENT_SECRET_PATH = os.path.expanduser("~/.spotify/client_secret")

with open(CLIENT_ID_PATH, "r") as f:
    client_id = f.read()

with open(CLIENT_SECRET_PATH, "r") as f:
    client_secret = f.read()

print(client_id, client_secret)

# 1. get current song

# 2. look online for album cover

# 3. transfer that information to webpage that'll display the image
