import requests


def test_user_post():
    body = {
        "id": 0,
        "username": "sonu",
        "firstName": "string",
        "lastName": "string",
        "email": "string",
        "password": "string",
        "phone": "string",
        "userStatus": 0
    }

    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

    resp = requests.post("https://petstore.swagger.io/v2/user", headers=headers, data=body)
    print(resp.text)
    # validation
    status = resp.status_code
    assert status == 200, "status code invalid"
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
