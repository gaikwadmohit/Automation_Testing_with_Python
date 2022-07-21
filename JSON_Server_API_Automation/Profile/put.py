import requests

body={

 "name": "mohit123"
}

res=requests.put("http://localhost:3000/profile",data=body)
print(res)
print(dir(res))
print(res.json())
print(res.text)
