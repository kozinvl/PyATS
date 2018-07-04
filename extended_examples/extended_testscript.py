import logging
import argparse
from ats import aetest
from ats.log.utils import banner

logger = logging.getLogger(__name__)

parameters = {'arg_A': 'value A',
              'arg_B': 'value B'
              }


class CommonSetup(aetest.CommonSetup):
    @aetest.subsection
    def simple_subsection(self):
        self.from_simple_subsection = 'this is simple'
        self.passed('It Always passes!')
        logger.info('is not executed, because self.passed')

    @aetest.subsection
    def using_parameters(self, testbed, arg_a, arg_b):
        logger.info('testbed: %s' % testbed)
        logger.info('Parameter A: %s' % arg_a)
        logger.info('Parameter B: %s' % arg_b)

    @aetest.subsection
    def self_is_self(self):
        assert self.from_simple_subsection is 'this is simple'

    @aetest.subsection.loop(result=['passed', 'skipped'])
    def subsection_looped_parameters(self, result):
        result_api = getattr(self, result)
        result_api()

    @aetest.subsection
    def testbed_info(self, testbed):
        if not testbed or not testbed.devices:
            logger.warning('no testbed was provided to script launch')
        else:
            logger.info('Testbed Name: %s' % testbed.name)
            for device in testbed:
                logger.info('    Device: %s' % device.name)
                for intf in device:
                    logger.info('        Interface: %s' % intf.name)
                    if intf.link:
                        logger.info('            Link: %s' % intf.link.name)
                    else:
                        logger.info('            Link: none')

            if 'routers' in self.parameters:
                # validate each router is in the testbed
                for rtr in self.parameters['routers']:
                    assert rtr in testbed.devices

            if 'links' in self.parameters:
                # validate links
                for link in self.parameters['links']:
                    assert link in testbed.links

    @aetest.subsection
    def connect_device(self, testbed):
        if not testbed or not testbed.devices:
            logging.warning('No testbed was provided to script launch')
        else:
            # Using the label, connect to the uut device
            if 'labels' in self.parameters:
                if 'uut' in self.parameters['labels'] and \
                        self.parameters['labels']['uut'] in testbed.devices:
                    # store the device into parameters
                    testbed.devices['uut'].connect()
                    self.parent.parameters['uut'] = testbed.devices['uut']

    def random_local_method(self):
        return "Ooooo, I got called!"


class ExampleTestcase(aetest.Testcase):
    uid = 'ExampleTestcase'
    description = 'An alternative description for this ExampleTestcase'
    groups = ['group_A', 'group_B', 'group_C']
    parameters = {
        'local_A': 'default value A',
        'local_B': 'default value B',
    }
    data_A = 1
    data_B = 'abc'

    @aetest.setup
    def setup(self):
        logger.info("%s Setup/Preparation" % self.uid)
        self.word = True
        self.passed('Setup pass')

    @aetest.setup
    def simple_test(self):
        assert self.word is True
        logger.info('Testcase data_A: %s' % self.data_A)
        logger.info('Testcase data_B: %s' % self.data_B)

    @aetest.setup
    def accessing_parameters(self, testbed, arg_A,
                             arg_B,
                             local_A,
                             local_B):
        logger.info('Testbed: %s' % testbed)
        logger.info('arg_A: %s' % arg_A)
        logger.info('arg_B: %s' % arg_B)
        logger.info('local_A: %s' % local_A)
        logger.info('local_B: %s' % local_B)
