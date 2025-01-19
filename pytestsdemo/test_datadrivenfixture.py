## fixture for this is defined in conftest.py check that file and check for dataLoad class
import pytest

## data driven
@pytest.mark.usefixtures("dataLoad")
class TestExample2:

    def test_editProfile(self, dataLoad): # when we are returning something from our fixture then we need to pass fixture
        print(dataLoad[0])  ## in our test like we passed in above line`
        print(dataLoad[1])
        print(dataLoad[2])

## paramaterizing fixture

def test_crossBrowser(crossBrowser):
    print(crossBrowser)

## calling multiple values in each params of fixture
def test_crossBrowser2(crossBrowser2):
    print(crossBrowser2)
