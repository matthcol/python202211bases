import requests
# https://requests.readthedocs.io/en/latest/

# see also other module: json

url = 'https://data.toulouse-metropole.fr/api/records/1.0/search/?dataset=cafes-concerts&q=&rows=2'

response = requests.get(url)

# https://fr.wikipedia.org/wiki/Liste_des_codes_HTTP
print(response.status_code)
if 200 <= response.status_code < 300:
    print("OK")
    # content can be obtain with
    # - response.content (binary mode)
    # - response.text (text mode according to encoding)
    # - response.json() (decoding content in json/format)
    data = response.json()
    print(data)