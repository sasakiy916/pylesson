import requests

res = requests.post("https://joytas.net/php/calc.php",data={"x":10,"y":7})

res.encoding=res.apparent_encoding

print(res.text)
