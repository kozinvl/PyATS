"""Example of pyATS work. Used just AETest package and data in the form"""

import logging
from ats import aetest
from ats.topology import loader

log = logging.getLogger(__name__)
log.info('Loading testbed from YAML file')
testbed = loader.load("testbed_1.yaml")


class TestcaseOne(aetest.Testcase):
    server = None

    @aetest.setup
    def setup(self):
        log.info('Connection to Linux Server')
        self.server = testbed.devices['vm-a']
        self.server.connect()

    @aetest.test
    def test_one(self):
        log.info('Check the results')
        a = self.server.execute('hostname')
        assert len(a) > 3

    @aetest.cleanup
    def cleanup(self):
        log.info('Close connection to Server')


if __name__ == '__main__':
    aetest.main()
