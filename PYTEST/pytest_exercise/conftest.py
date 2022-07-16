import pytest


@pytest.fixture(autouse=True)
def tc_setup():
    print("Launch browser")
    print("Open Facebook web application")
    print("Login with Username and passward")

    yield

    print("Log-Out Facebook")
    print("Close Browser")
