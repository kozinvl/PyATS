"""Example of pyATS work. Used just AETest package and data in the form"""

import logging
from ats import aetest
from ats.topology import loader
from ats import topology

log = logging.getLogger(__name__)
testbed = topology.loader.load('testbed.yaml')


class TestcaseOne(aetest.Testcase):
    server = None

    @aetest.setup
    def setup(self):
        log.info('Connection to Linux Server')
        self.server = testbed.devices['remote_device']
        self.server.connect()

    @aetest.test
    def test_one(self):
        log.info('Check the results')
        virtual_machine_name = self.server.execute('hostname')
        assert len(virtual_machine_name) > 3

    @aetest.cleanup
    def cleanup(self):
        log.info('Close connection to Server')
