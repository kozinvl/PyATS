from ats import aetest
import logging

logger = logging.getLogger(__name__)

parameters = {'data_1': '1', 'data_2': '2'}


class CommonSetup(aetest.CommonSetup):
    data_A = 'string'
    data_B = 5
    parameters = {'default_key': 'default'}

    @aetest.subsection
    def common_setup(self):
        logger.info('Current section: %s' % self.uid)
        assert self.data_A == 'string'

    @aetest.loop(variable=['subsection_2', 'subsection_3'])
    @aetest.subsection
    def common_next(self, variable):
        logger.info("Current : %s" % variable)
        if variable == 'subsection_2':
            self.var = 5
            self.parameters = {'new_key': self.var}
            logger.info('%s Was added  in parameters dict ' % self.var)
        else:
            self.parameters.update({'other_key': 6})
            logger.info('value was added')

    @aetest.subsection
    def common_last(self):
        logger.info('Parameters number: %s' % self.parameters['new_key'])
        logger.info(parameters)
        logger.info(self.parameters)


class MainCase(aetest.Testcase):
    parameters = {'xyz': '123'}

    @aetest.setup
    def setup(self):
        logger.info('Setup from Case')

    @aetest.test
    def test(self):
        logger.info('Test section')
        logger.info(self.parameters)
        assert self.parameters['xyz'] == '123'

    @aetest.cleanup
    def cleanup(self):
        logger.info('Cleanup all data from Case')


class CommonCleanup(aetest.CommonCleanup):
    @aetest.subsection
    def clean(self):
        logger.info('Common Cleanup')


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
