import pytest
import requests
import random

token = "Bearer BQCUbT1IK4PluELhclx1bSs" \
        "-4MeIhhndKc7oE3yLQVoGovY2tLYSL4LXqYWTYigDMCfm9zKnHhqDKu9sNfx6GCynUSHTv1StmIAW" \
        "9o4nJqg5H6er5kJYvtjf80Bx6pJKujHRr1n5dzVtQKU4UtjpPO9HOFZ88jaXU8Ddor2NH1NCiR7J0pwI6wKnn73w-J79iao "

user_id = '31phqvitquseox6y24sbjy7prlo4'

playlist_id = '29Kh2hfsA6Koha1qXBGALe'

track_id = '61JrslREXq98hurYL2hYoc'


# --------------------------------profile----------------------------------------------------
def test_Get_Current_Profile():
    header = {
        'Authorization': token
    }
    resp = requests.get("https://api.spotify.com/v1/me", headers=header)
    print(resp.text)
    print(">>>>>>>>>>>>>>>>>test_Get_Current_Profile>>>>>>>>>>>>>>>>>>>>>>>>")

    a = resp.json()
    country = a['country']
    uri = a['uri']
    type = a["type"]
    prod = a["product"]
    id = a["id"]
    display_name = a["display_name"]
    print('', uri, '', type, '', prod, '', id)

    # validation
    status = resp.status_code
    assert status == 200, "status code invalid"
    assert user_id == '31phqvitquseox6y24sbjy7prlo4', "invalid id"
    assert country == 'IN', "Invalid country"
    assert uri == "spotify:user:31phqvitquseox6y24sbjy7prlo4", "Invalid Uri"
    assert country == "IN"
    assert display_name == "MOHIT GAIKWAD"
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")


def test_Get_UserProfile():
    header = {
        'Authorization': token
    }
    resp = requests.get("https://api.spotify.com/v1/users/" + user_id, headers=header)
    print(resp.text)
    print(
        ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>test_Get_UserProfile>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

    b = resp.json()
    uri = b['uri']
    href_ = b["href"]
    type_ = b["type"]
    img = b["images"]
    id = b["id"]
    display_name = b["display_name"]
    print(href_, '', type_, '', img, '', id)

    # validation
    status = resp.status_code
    assert status == 200, "status code invalid"
    assert uri == "spotify:user:31phqvitquseox6y24sbjy7prlo4", "Invalid Uri"
    assert href_ == 'https://api.spotify.com/v1/users/31phqvitquseox6y24sbjy7prlo4'
    assert display_name == "MOHIT GAIKWAD", "Invalid Name"
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")


# --------------------------------playlist----------------------------------------------------

def test_get_playlist():
    header = {
        'Authorization': token
    }
    resp = requests.get("https://api.spotify.com/v1/me/playlists", headers=header)
    print(resp)
    print(resp.text)
    a = resp.status_code
    assert a == 200, "Status code invalid"
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")


def test_create_playlist():
    num = random.random()
    header = {
        'Authorization': token
    }

    body = '{"name":"Bridgelabz CFP1","description":"New playlist description","public":false}'

    resp = requests.post("https://api.spotify.com/v1/users/" + user_id + "/playlists", headers=header,
                         data=body)
    print(resp)
    print(resp.text)
    # json_response = resp.json()
    # print(json_response['items'][0]['name'])
    # assert json_response['items'][0]['name'] == "Bridgelabz Playlist1"
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")


def test_Add_itemTo_playlist():
    header = {
        'Authorization': token
    }
    parameters = {
        "uris": "spotify:track:16LrVogeqYzGOfPXCzTVyU"
    }

    resp = requests.post("https://api.spotify.com/v1/playlists/0KtQ1oo4a89xIfZMFkIPs5/tracks", headers=header,
                         params=parameters)
    print(resp)
    print(resp.text)
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")


def test_Change_playlist_details():
    header = {
        'Authorization': token
    }
    body = '{"name":"Updated Playlist Name","description":"Updated playlist description","public":True}'
    resp = requests.put("https://api.spotify.com/v1/playlists/" + playlist_id, headers=header, data=body)
    print(resp.text)
    print(
        ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>test_Change_playlist_details>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    # validation
    status = resp.status_code
    assert status == 200, "status code invalid"
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")


def test_GetUsersPlaylists():
    header = {
        'Authorization': token
    }
    resp = requests.get("https://api.spotify.com/v1/users/" + user_id + "/playlists", headers=header)
    print(resp.text)
    print(
        ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>test_GetUsersPlaylists>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    # validation
    status = resp.status_code
    assert status == 200, "status code invalid"
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")


def test_GetPlaylists():
    header = {
        'Authorization': token
    }
    resp = requests.get("https://api.spotify.com/v1/playlists/" + playlist_id, headers=header)
    print(resp.text)
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    # validation
    status = resp.status_code
    assert status == 200, "status code invalid"

    print(
        ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>test_GetPlaylists>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")


def test_GetPlaylistItems():
    header = {
        'Authorization': token
    }
    resp = requests.get("https://api.spotify.com/v1/playlists/" + playlist_id, headers=header)
    print(resp.text)
    print(
        ">>>>>>>>>>>>>>>>>>>>>>>>>>>>GetPlaylistItems>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    # validation
    status = resp.status_code
    assert status == 200, "status code invalid"

    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")


def test_Getcurrent_user_playlist():
    header = {
        'Authorization': token
    }
    resp = requests.get("https://api.spotify.com/v1/me/playlists", headers=header)
    print(resp.text)
    print(
        ">>>>>>>>>>>>>>>>>>>>>>>>>>>>test_Getcurrent_user_playlist>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

    c = resp.json()
    href = c["href"]
    items = c["items"]
    limit = c["limit"]
    next = c["next"]
    offset = c["offset"]
    previous = c["previous"]
    total = c["total"]
    print(href, "->", items, "->", limit, "->", next, "->", offset, '->', previous, '->', total)

    # validation
    status = resp.status_code
    assert status == 200, "status code invalid"
    assert href == 'https://api.spotify.com/v1/users/31phqvitquseox6y24sbjy7prlo4/playlists?offset=0&limit=20'
    assert limit == 21, "Actual limit is 20"
    assert next == None

    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")


def test_Get_playlist_cover_image():  # error
    header = {
        'Authorization': token
    }
    resp = requests.get("https://api.spotify.com/v1/playlists/" + playlist_id + "/images", headers=header)
    print(resp.text)
    print(
        ">>>>>>>>>>>>>>>>>>>>>>>>>>>>test_Get_playlist_cover_image>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

    c = resp.json()
    height_of_image = c["height"]
    url = c["url"]
    width_of_image = c["width"]

    print("height_of_image", height_of_image, ">>>>", "url", url, ">>>>>", "width_of_image", width_of_image)

    # validation
    status = resp.status_code
    assert status == 200, "status code invalid"
    assert height_of_image == 640
    assert url == 'https://i.scdn.co/image/ab67616d0000b2736648188ebc8f37a56f5a4a21'
    assert width_of_image == 640, "Actual width  is 640"


def test_update_playlist_items():
    header = {
        'Authorization': token
    }
    body = '{"range_start":1,"insert_before":0,"range_length":2}'
    resp = requests.put("https://api.spotify.com/v1/playlists/" + playlist_id + "/tracks", headers=header, data=body)
    print(resp.text)
    print(
        ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>test_update_playlist_items>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    # validation
    status = resp.status_code
    snapshot_id = resp.json()
    assert status == 200, "status code invalid"
    assert snapshot_id == "NyxmZTQ3YWU0MWJiNmU4MWM1YWNjYzI4MWE3NjVlY2Y2ZDliMThlMzIx", ">>>>>>>>id gets changed<<<<<<<<<<<"
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")


def test_delete_playlist_items():
    header = {
        'Authorization': token
    }
    body = {"uri": "spotify:user:31phqvitquseox6y24sbjy7prlo4"}
    resp = requests.delete("https://api.spotify.com/v1/playlists/" + playlist_id + "/tracks", headers=header, data=body)
    print(resp.text)
    print(
        ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>test_delete_playlist_items>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")


# --------------------------------Search--------------------------------------------------------


def test_search_for_items():
    header = {
        'Authorization': token
    }
    parameter = {
        "q": "deva shree ganesha",
        "type": "track"
    }
    resp = requests.get("https://api.spotify.com/v1/search", headers=header, params=parameter)
    print(resp.text)
    print(
        ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>test_search_for_items>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

    d = resp.json()
    # total_tracks = d["total_tracks"]
    # name = d["name"]
    # print(total_tracks, '', name)

    # d = resp.json()
    # print(d["tracks"]['track_number'])

    # validation
    status = resp.status_code
    assert status == 200, "status code invalid"

    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")


# ------------------------------------Tracks-------------------------------------------------------

def test_get_track_audio_analysis():  # analysis not found
    header = {
        'Authorization': token
    }

    resp = requests.get("https://api.spotify.com/v1/audio-analysis/" + track_id, headers=header)
    print(resp.text)
    print(
        ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>get_track_audio_analysis>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    # validation
    status = resp.status_code
    assert status == 200, "status code invalid"
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")


def test_GetTracksAudioFeaturesWith_Id():  # analysis not found
    header = {
        'Authorization': token
    }

    resp = requests.get("https://api.spotify.com/v1/audio-features/" + track_id, headers=header)
    print(resp.text)
    print(
        ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>get_track_audio_analysis>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    # validation
    status = resp.status_code
    assert status == 200, "status code invalid"
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")


def test_getTrack():
    header = {
        'Authorization': token
    }

    resp = requests.get("https://api.spotify.com/v1/tracks/" + track_id, headers=header)
    print(resp.text)
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>get_track_audio_analysis>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    # validation
    status = resp.status_code
    assert status == 200, "status code invalid"
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")


def test_getseveralTrack():
    header = {
        'Authorization': token
    }

    resp = requests.get("https://api.spotify.com/v1/tracks/" + track_id, headers=header)
    print(resp.text)
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>get_track_audio_analysis>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    # validation
    status = resp.status_code
    assert status == 200, "status code invalid"
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")


# test_Get_Current_Profile()
# test_Get_UserProfile()
# test_get_playlist()
# test_create_playlist()
# test_Add_itemTo_playlist()
# test_Change_playlist_details()
# test_GetUsersPlaylists()
# test_GetPlaylists()
# test_GetPlaylistItems()
# test_Get_playlist_cover_image()
# test_update_playlist_items()
# test_delete_playlist_items()
# test_search_for_items()
# test_get_track_audio_analysis()
# test_GetTracksAudioFeaturesWith_Id()
# test_getTrack()
# test_getseveralTrack()
