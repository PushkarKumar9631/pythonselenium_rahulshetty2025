## fixture are used to excute some method first as pre requisite for another method or test cases
## @pytest.fixture()
## we can also write post test requisites in the same fixture as well and it will be executed last, use yeild keyword
## we can declare all fixture in one file, the file name should be conftest.py inside it define all fixture and avoid
## duplicacy, after defining in conftest file, we can use it in all test cases by calling them
## data driven and parameterization can be done using tuple format



import pytest

### below fixture has been defined in conftest.py file as per the pytest standards so here it is commented

# @pytest.fixture()
# def setup():
#     print("I will be executed first")
#     yield ## whatever we write in this it will be executed after test execution
#     print("i will be executed last")

# def test_fixturedemo(setup):
#     print("i will execute steps in fixture demo method")

@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixturedemo1(self):
        print("i will execute steps in fixture demo method")

    def test_fixturedemo2(self):
        print("i will execute steps in fixture demo method")

    def test_fixturedemo3(self):
        print("i will execute steps in fixture demo method")