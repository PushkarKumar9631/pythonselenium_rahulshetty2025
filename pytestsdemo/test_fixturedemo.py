## fixture are used to excute some method first as pre requisite for another method or test cases
## @pytest.fixture()
## we can also write post test requisites in the same fixture as well and it will be executed last, use yeild keyword

import pytest


@pytest.fixture()
def setup():
    print("I will be executed first")
    yield ## whatever we write in this it will be executed after test execution
    print("i will be executed last")

def test_fixturedemo(setup):
    print("i will execute steps in fixture demo method")