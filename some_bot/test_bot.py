import json

with open('tokens.json') as f:
    j = json.load(f)
    BOT_TOKEN = j['test_zeixes_bot token']

# Bot for converting color scheme of image
