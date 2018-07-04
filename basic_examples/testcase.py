import logging
from ats import aetest

log = logging.getLogger(__name__)


class common_setup(aetest.СommonSetup):

    @aetest.subsection
    def subsection_one(self):
        pass

    @aetest.subsection
    def subsection_two(self):
        pass

class Testcase_one(aetest.Test):

    def setup(self):
        pass