# configuring your own logging using log handlers
# -----------------------------------------------
from ats import aetest
from ats.topology import loader
import logging

from ats.log import ScreenHandler, TaskLogHandler

# create a logger
logger = logging.getLogger(__name__)

# create a handler
screen_handler = ScreenHandler()
tasklog_handler = TaskLogHandler('log_file.txt')

# attach to your logger
logger.addHandler(screen_handler)
logger.addHandler(tasklog_handler)

# set log level to show everything
logger.setLevel(logging.DEBUG)
testbed = loader.load("testbed_1.yaml")


class TestcaseOne(aetest.Testcase):
    server = None

    @aetest.setup
    def setup(self):
        self.server = testbed.devices['vm-a']
        self.server.connect()
        logger.warning("Connected to server")

    @aetest.test
    def test_one(self):
        logger.critical('Check the results')
        virtual_machine_name = self.server.execute('hostname')
        assert len(virtual_machine_name) == 'Hello'

    @aetest.cleanup
    def cleanup(self):
        logger.error('Close connection to Server')


if __name__ == '__main__':
    aetest.main()
