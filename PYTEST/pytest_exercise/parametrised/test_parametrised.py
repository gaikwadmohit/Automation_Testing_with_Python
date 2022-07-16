import pytest


# @pytest.fixture(params=['a', 'b'])
# def param_using_fixtures(request):
#     print(request.params)
#
#
# def test_login(param_using_fixtures):
#     print("login Successfully")


@pytest.mark.parametrize("a, b,  c",[(1,2,3),(5,4,6),(11,2,13)])
def test_param_using_mark(a,b,c):
    assert a+b==c