import requests

body = {

     "name": "swapnil"
}
res = requests.post("http://localhost:3000/profile", data=body)

print(res)
print(dir(res))
