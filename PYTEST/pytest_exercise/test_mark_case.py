import pytest

def test_calculation2():
    a = 2
    b = 6
    assert a + 4 == b, "Nice calculation"


@pytest.mark.regression
def test_mark_regression():
    a = "Hiii"
    assert a == "Hiii"


@pytest.mark.sanity
def test_mark_sanity():
    a = 2
    b = 4
    assert a + 2 == b, "Nice calculation"

@pytest.mark.skip
def test_skip():
    a = 2
    b = 4
    assert a + 2 == b, "Nice calculation"

@pytest.mark.xfail
def test_xfail():
    a = 2
    b = 4
    assert a + 3 == b, "Nice calculation"

@pytest.mark.xfail
def test_mark_xfail():
    a = "Hiii"
    assert a == "Hiii"
