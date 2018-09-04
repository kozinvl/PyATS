from ats import aetest
import logging

# available levels:
#       logging.INFO
#       logging.CRITICAL
#       logging.ERROR
#       logging.WARNING
#       logging.DEBUG
# create a logger for this module
logger = logging.getLogger(__name__)

logger.setLevel(logging.INFO)


class TestcaseOne(aetest.Testcase):
    @aetest.setup
    def setup(self):
        # informational messages
        logger.info('info messages')
        # critical messages
        logger.critical('critical messages')

    @aetest.test
    def test_one(self):
        # debug messages
        logger.debug('debug messages')

        # warning messages
        logger.warning('warning messages')

    @aetest.cleanup
    def cleanup(self):
        # error messages
        logger.error('error messages')


if __name__ == '__main__':
    aetest.main()
