import pytest


@pytest.fixture
def setup():
    print("Launch browser")
    print("Open Facebook web application")
    print("Login with Username and passward")

    yield

    print("Log-Out Facebook")
    print("Close Browser")

def test_share_Event(setup):
    print("click on Event and write")
    print("post Event")

def test_send_friend_req(setup):
    print("Click on friends")
    print("search friend")
    print("send request")
