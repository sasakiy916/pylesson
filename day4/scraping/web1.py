import requests
res=requests.get("https://joytas.net/kaba/")
res.encoding=res.apparent_encoding

print(res.text)
