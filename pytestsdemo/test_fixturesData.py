import pytest

from pytestsdemo.BaseClass import BaseClass


## this has been using baseclASS FILE FOR LOGGING
## when we run this same file using >> py.test --html=report.html -s  the logs will come as attached as html report

@pytest.mark.usefixtures("dataLoad")
class TestExample2(BaseClass): ## parent baseclass has been inherited in the child class

    def test_editProfile(self, dataLoad):
        log = self.getLogger() ## logger has been called from base class and stored in log object
        log.info(dataLoad[0])
        log.info(dataLoad[2])
        print(dataLoad[2])








