import requests
#response=requests.get("http://www.python.org/downloads/")
response=requests.get("http://joytas.net/kaba")
response.encoding=response.apparent_encoding
text=response.text
print(text)
