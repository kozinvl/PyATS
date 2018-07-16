"""Example of pyATS work. Used just AETest package and input arguments
to the testscript - 'python second_example.py --testbed testbed_1.yaml'
"""

import logging
from ats import aetest
from ats.topology import loader

log = logging.getLogger(__name__)


class TestcaseOne(aetest.Testcase):
    server = None

    @aetest.setup
    def setup(self, testbed):
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
    # local imports
    import sys
    import argparse
    from ats.topology import loader

    parser = argparse.ArgumentParser(description="standalone parser")
    parser.add_argument('--testbed', dest='testbed')

    # parse args
    args, sys.argv[1:] = parser.parse_known_args(sys.argv[1:])

    # post-parsing processing
    testbed = loader.load(args.testbed)

    # and pass all arguments to aetest.main() as kwargs
    aetest.main(testbed=testbed)
