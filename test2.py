import pytest

@pytest.fixture
def tester():
    name = "Astika"
    password = "Password123"
    return (name, password)


def test1(tester):
    first_name = "Astika"
    assert tester[0] == first_name


def test_2(tester):
    password_check = "Password123"
    assert tester[1] == password_check