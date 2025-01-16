# any pytest file should start with test_  and then the file name
# pytest methods or functions name should always start with test_ then the name
##  its very important to write method names something meaning full
# -k stands for method names execution, -s logs in output -v stands for more into metadata
# you can also run specific file name with py.test <filename>
# you can mark test with @pytest.mark.smoke and then run with -m <markname>
# python has predefined mark as skip for skipping any method using @pytest.mark.skip , in cmd >> py.test -m skip -v -s
# for not reporting some test results into your reports use @pytest.mark.xfail

import pytest


@pytest.mark.smoke
def test_thirdprogramcreditcard():
    msg = "hello world"
    assert msg == "hi", "Test failed because the strings do not match"

@pytest.mark.skip ## here skipping this test case
def test_fourthprogram():
    a = 4
    b = 6
    assert a+b == 6, "Addition do not match"