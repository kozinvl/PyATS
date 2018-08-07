import logging
from ats.topology import loader
from ats import topology
from ats import aetest

log = logging.getLogger(__name__)

string_configuration = 'Welcome to pyATS'

# loading testbed immediately
tb = topology.loader.load('testbed.yaml')


class TestcaseOne(aetest.Testcase):
    _temp_string = None

    @aetest.setup
    def setup(self):
        log.info('Connection to Linux Server')
        device = tb.devices['remote_device']
        device.connect()
        device.execute('cd /tmp')
        self._temp_string = device.execute('cat New_file.txt')

    @aetest.test
    def test_one(self):
        log.info('Check the results')
        assert self._temp_string == string_configuration

    @aetest.cleanup
    def cleanup(self):
        log.info('Close connection to Server')
