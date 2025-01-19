## fixture are used to excute some method first as pre requisite for another method or test cases
## @pytest.fixture()
## we can also write post test requisites in the same fixture as well and it will be executed last, use yeild keyword
## we can declare all fixture in one file, the file name should be conftest.py inside it define all fixture and avoid
## duplicacy, after defining in conftest file, we can use it in all test cases by calling them
## data driven and parameterization can be done using tuple format

import pytest


# @pytest.fixture()
@pytest.fixture(scope="class") ## we are declaring fixture to run at class level, not at method level, so that it can run prerquistes
# ones the class is executed and then run post requistes or yield command ones class and all its methods are executed
def setup():
    print("I will be executed first")
    yield ## whatever we write in this it will be executed after test execution
    print("i will be executed last")


## fixture which provides data to test cases is below
@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return ["rahul", "Shetty", "rahulshettyacademy.com"]


## fixture which is used for providing data sets as params
@pytest.fixture(params=["chrome", "firefox", "IE"])
def crossBrowser(request):
    return request.param

## paramterizing multiple values in params
@pytest.fixture(params=[("chrome", "Rahul", "Shetty"), ("firefox", "shetty"), ("IE", "SS")])
def crossBrowser2(request):
    return request.param