import requests




res = requests.post("http://localhost:3000/comments")
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
