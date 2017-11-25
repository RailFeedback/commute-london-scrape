import requests

url = 'http://commutelondon.com/CommuteLondon/CommuteLondon?getrequest=wordlistrelated&gettocname=VT+EAST+COAST'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
    # 'From': 'youremail@domain.com'  # This is another valid field
}

response = requests.get(url, headers=headers)
print(response.text)
