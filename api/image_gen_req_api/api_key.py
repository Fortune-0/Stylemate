# Example posting a text URL:

import requests
r = requests.post(
    "https://api.deepai.org/api/text2img",
    data={
        'text': 'RED SHIRT',
    },
    headers={'api-key': 'a34d4a77-155b-4836-bec1-99aadd3c78b4'}
)
print(r.json())


# Example posting a local text file:

import requests
r = requests.post(
    "https://api.deepai.org/api/text2img",
    files={
        'text': open('/path/to/your/file.txt', 'rb'),
    },
    headers={'api-key': 'a34d4a77-155b-4836-bec1-99aadd3c78b4'}
)
print(r.json())


# Example directly sending a text string:

import requests
r = requests.post(
    "https://api.deepai.org/api/text2img",
    data={
        'text': 'RED SHIRT',
    },
    headers={'api-key': 'a34d4a77-155b-4836-bec1-99aadd3c78b4'}
)
print(r.json())