from ats import aetest
import logging

logger = logging.getLogger(__name__)

parameters = {'data_1': 1, 'data_2': 2}


class CommonSetup(aetest.CommonSetup):
    data_A = 'string'
    data_B = 5
    parameters = {'default_key': 'default_value'}

    @aetest.subsection
    def common_setup(self):
        logger.info('Running current section: %s' % self.uid)
        self.data_C = 6
        self.passed('Test was passed')

    @aetest.loop(uid=['subsection_2', 'subsection_3'])
    @aetest.subsection
    def looped(self, uid):
        logger.info("Current section: %s" % uid)
        if uid == 'subsection_2':
            self.parameters = {'new_key': 11}
            logger.info('%s Was added in parameters' % self.parameters['new_key'])
        else:
            self.parameters.update({'other_key': 12})
            logger.info('%s Was added in parameters' % self.parameters['other_key'])

    @aetest.subsection
    def verify(self):
        logger.info('verifying variable')
        assert self.data_B == 5

    @aetest.subsection
    def using_values(self, new_key, data_1):
        logger.info('new_key : %s' % new_key)
        logger.info('data_1 : %s' % data_1)
        logger.info('data_C: %s' % self.data_C)
        self.passed('Marking that test always pass')

    @aetest.subsection
    def skip_test(self):
        self.skipped('Test was skipped')
        logger.info('It will not printed on the console because of skipped!')


class TestCase(aetest.Testcase):
    parameters = {'abc': 123}

    @aetest.setup
    def setup(self):
        logger.info('Setup from TestCase')

    @aetest.test
    def test(self):
        logger.info('Test section')
        assert self.parameters['abc'] == 123

    @aetest.cleanup
    def cleanup(self):
        logger.info('Cleanup all data from test_case')
        self.parameters = {}


class CommonCleanup(aetest.CommonCleanup):
    @aetest.subsection
    def cleanup(self):
        logger.info('Common Cleanup')

    @aetest.subsection
    def cleanup_second(self):
        logger.info('Done')


if __name__ == '__main__':
    import argparse
    from ats import topology

    logging.root.setLevel('INFO')
    parser = argparse.ArgumentParser(description="standalone parser")
    parser.add_argument('--testbed', dest='testbed',
                        help='testbed YAML file',
                        type=topology.loader.load,
                        default=None)

    args = parser.parse_known_args()[0]
    aetest.main(testbed=args.testbed)
