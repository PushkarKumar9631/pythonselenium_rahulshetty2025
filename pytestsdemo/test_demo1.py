# any pytest file should start with test_  and then the file name
# pytest methods or functions name should always start with test_ then the name
##  its very important to write method names something meaning full
# -k stands for method names execution, -s logs in output -v stands for more into metadata
# you can also run specific file name with py.test <filename>
import pytest


@pytest.mark.smoke
def test_firstprogram():
    print("hello world")
@pytest.mark.xfail
def test_secondprogramcreditcard():
    print("hello")

@pytest.fixture()
def setup():
    print("I will be executed first")

def test_fixturedemo(setup):
    print("i will execute steps in fixture demo method")