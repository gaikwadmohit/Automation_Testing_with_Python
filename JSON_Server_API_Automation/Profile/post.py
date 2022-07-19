import requests

body={
  "posts": [
    { "id": 1, "title": "json-server", "author": "typicode" }
  ],
  "comments": [
    { "id": 1, "body": "some comment", "postId": 1 }
  ],
  "profile": { "name": "typicode" }
}

res=requests.post("http://localhost:3000/profile",data=body)
print(res)
print(dir(res))
print(res.json())