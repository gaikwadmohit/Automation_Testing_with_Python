import requests

token = "Bearer BQCvNYk5yyw2yKeCMI5ZDDhke6a1QSe8896tQmitx9J0KBjgZWqy_rYLxmxuOxqsFg77mD5I1nqVX1E41UXxbfYCyWKAjuW-S8qr3vdsBO5dlW0f97viOXyDExvPyz7-x4JsBAR56GiA8n80pv98bJpwGx84k7pb6KILntYYEHe3SLzQN3KDDXZHmcCkQA8ia20"


def get_playlist():
    header = {
        'Authorization': token
    }
    resp = requests.get("https://api.spotify.com/v1/me/playlists", headers=header)
    print(resp)
    print(resp.text)

def create_playlist():

    header = {
        'Authorization': token
    }
    body='{"name":"Bridgelabz Playlist","description":"New playlist description","public":True}'
    resp = requests.get("https://api.spotify.com/v1/users/31phqvitquseox6y24sbjy7prlo4/playlists", headers=header,data=body)
    print(resp)
    print(resp.text)





# get_playlist()
create_playlist()