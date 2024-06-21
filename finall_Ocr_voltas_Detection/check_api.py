import requests

url = 'http://localhost:5001/extract_text_info'
files = {'files': open(r'images\1.bmp', 'rb')}

response = requests.post(url, files=files)

print(response.json())
