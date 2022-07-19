import requests

body =[
    {
        "posts": [
            {
                "id": 1,
                "title": "Mohit",
                "author": "typicode"
            }
        ],
        "comments": [
            {
                "id": 1,
                "body": "some comment",
                "postId": 1
            }
        ],
        "profile": {
            "name": "typicode"
        },
        "id": 1
    }
]

res = requests.put(" http://localhost:3000/comments/1", data=body)
print(res)

print(res.text)
print(
    "********************************************************************************************************************")

print(res.encoding)
print(
    "********************************************************************************************************************")

print(res.url)
print(
    "********************************************************************************************************************")

print(res.cookies)
print(
    "********************************************************************************************************************")

print(res.elapsed)
print(
    "********************************************************************************************************************")

print(res.headers)
print(
    "********************************************************************************************************************")

print(res.history)
print(
    "********************************************************************************************************************")

print(res.links)
print(
    "********************************************************************************************************************")

print(res.json())
print(
    "********************************************************************************************************************")

print(res.status_code)
print(
    "********************************************************************************************************************")