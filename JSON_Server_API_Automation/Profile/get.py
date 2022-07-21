import requests

res=requests.get("http://localhost:3000/profile")
print(res)
print(dir(res))
print(res.json())
a=(res.json())
print(a["name"])