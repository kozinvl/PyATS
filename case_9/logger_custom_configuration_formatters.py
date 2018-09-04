# configuring own logging using log handlers
from ats import aetest
from ats.topology import loader
import logging
import sys
from ats import topology

from ats.log import ScreenFormatter, TaskLogFormatter

# create a logger
logger = logging.getLogger(__name__)

# create handlers using logging standard handlers
screen_handler = logging.StreamHandler(stream=sys.stdout)
tasklog_handler = logging.FileHandler('log_file.log')

# set handler to use ats format and screen format
screen_handler.setFormatter(ScreenFormatter())
tasklog_handler.setFormatter(TaskLogFormatter())
# attach to your logger
logger.addHandler(screen_handler)
logger.addHandler(tasklog_handler)

# set log level to show everything
logger.setLevel(logging.ERROR)
logger.info('Loading testbed from YAML file')
testbed = topology.loader.load('''
devices:
    vm-a:
        os: 'linux'
        tacacs:
            username: mshumakov
        passwords:
            linux: 'mykola00'
        connections:
          linux:
            protocol: ssh
            ip: 192.168.242.44
        type: 'linux'
''')


class TestcaseOne(aetest.Testcase):
    server = None

    @aetest.setup
    def setup(self):
        logger.info('Connection to Linux Server')
        self.server = testbed.devices['vm-a']
        self.server.connect()
        logger.info("Connected to server")

    @aetest.test
    def test_one(self):
        logger.error('Check the results')
        virtual_machine_name = self.server.execute('hostname')
        assert len(virtual_machine_name) == 0


if __name__ == '__main__':
    aetest.main()
