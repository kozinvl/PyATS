import logging
import argparse
from ats import aetest
from ats.log.utils import banner
from libs import local_library

logger = logging.getLogger(__name__)

parameters = {'arg_A': 'value A',
              'arg_B': 'value B'
              }


class CommonSetup(aetest.CommonSetup):
    @aetest.subsection
    def simple_subsection(self):
        self.from_simple_subsection = 'sample'
        self.passed('It Always passes!')
        logger.info('is not executed, because self.passed')

    @aetest.subsection
    def using_parameters(self, testbed, arg_A, arg_B):
        logger.info('testbed: %s' % testbed)
        logger.info('Parameter A: %s' % arg_A)
        logger.info('Parameter B: %s' % arg_B)

    @aetest.subsection
    def self_is_self(self):
        assert self.from_simple_subsection is 'sample'

    @aetest.subsection.loop(result=['passed', 'skipped'])
    def subsection_looped_parameters(self, result):
        # equivalent to self.passed(), self.skipped()
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
        logger.info(banner(self.random_local_method()))

    def random_local_method(self):
        return "Ooooo, I got called in banner! Amazing"


class ExampleTestcase(aetest.Testcase):
    uid = 'SecondExampleTestcase'
    description = 'An alternative description for ExampleTestcase #2'
    groups = ['group_A', 'group_B', 'group_C']
    parameters = {
        'local_A': 'default value A',
        'local_B': 'default value B',
    }
    data_A = 1
    data_B = 'abc'

    @aetest.setup
    def setup(self):
        # assign some values to self
        self.word = True
        # declare section passed
        self.passed('Setup pass')

    @aetest.test
    def a_simple_test(self):
        # let's do some testing
        assert self.word is True
        # access attributes/data set within testcase definition
        logger.info('Testcase data_A: %s' % self.data_A)

    @aetest.test
    def accessing_parameters(self,
                             testbed,
                             arg_A,
                             arg_B,
                             local_A,
                             local_B):
        logger.info('Testbed: %s' % testbed)
        logger.info('arg_A: %s' % arg_A)
        logger.info('arg_B: %s' % arg_B)
        logger.info('local_A: %s' % local_A)
        logger.info('local_B: %s' % local_B)

    @aetest.test
    def accessing_parameteres_with_other_methods(self, **kwargs):
        assert self.parameters == kwargs
        import pprint
        logger.info(pprint.pformat(self.parameters))

    @aetest.test.loop(index=range(4),
                      result=['passed', 'failed', 'skipped', 'errored'])
    def test_loop(self, index, result):
        logger.info('Current index value: %s' % index)
        result_api = getattr(self, result)
        result_api()

    @aetest.test
    def assert_errors_are_failures(self):
        assert 'Apple' > 'Google', "Apple > Google? Blasphemy! Preposterous!"

    @aetest.test
    def exceptions_are_errors(self, non_existent_parameter):
        pass

    @aetest.test
    def show_version(self, uut=None):
        if uut:
            uut.execute('Show version')

    @aetest.cleanup
    def cleanup(self):
        self.parameters = {}


@aetest.loop(a=[2, 3])
class LoopedTestcase(aetest.Testcase):
    # associate groups
    groups = ['group_A', 'group_B']

    @aetest.setup
    def setup(self, a):
        logger.info(banner('Value A: %s' % a))

    @aetest.test.loop(b=[4, 5])
    def product(self, a, b):
        logger.info('%s x %s = %s' % (a, b, a * b))


class TestcaseWithSteps(aetest.Testcase):
    groups = ['group_A', ]

    @aetest.setup
    def setup(self, steps):
        with steps.start('this is a description of the step'):
            pass
        with steps.start('another step') as step:
            step.passed()

    @aetest.test
    def step_continue_on_failure_and_assertions(self, steps):
        # assertionErrors are also treated as failures
        with steps.start('assertion errors -> Failed', continue_=True):
            assert 1 == 0
        with steps.start('allowed to continue executing') as step:
            self.failed()
        with steps.start('this will not be run'):
            pass

    @aetest.test
    def steps_errors_exits_immediately(self, steps):
        # assertionErrors are also treated as failures
        with steps.start('exceptions causes all steps to skip over'):
            blablabla_function_doesnt_exist()
        with steps.start('another step that never runs'):
            pass

    @aetest.test
    def steps_with_child_steps(self, steps):
        with steps.start('test step one') as step:
            # start more steps
            with step.start('substep one') as sstep:
                # there's no limit to step nesting
                with sstep.start('subsubstep one') as sstep:
                    with sstep.start('subsubsubstep one') as sstep:
                        with sstep.start('running out of indentation') as sstep:
                            with sstep.start('definitely gone too far...'):
                                pass
            with step.start('substep two') as substep:
                pass
        with steps.start('test step two') as step:
            # cal another function from library, pass in the step
            local_library.function_supporting_step(step)


class CommonCleanup(aetest.CommonCleanup):
    @aetest.subsection
    def example_cleanup_subsection(self):
        pass

    @aetest.subsection
    def results_default_to_passed(self):
        # no exception here, and therefore the result for this subsection
        # is a definite Passed
        assert 'Google' > 'Apple', ':) no explanation necessary'

    @aetest.subsection
    def assertion_error_is_failed(self):
        # this will cause an AssertionException
        assert 'I' > "We", 'teamwork is always stronger'

    @aetest.subsection
    def exception_driven_behavior_error(self):
        # call something that doesn't exist will certainly wreak havoc
        i_am_a_proc_that_does_not_exist('arguments for the win')


if __name__ == '__main__':
    import argparse
    from ats import topology

    logging.root.setLevel('INFO')
    logging.root.setLevel('INFO')

    parser = argparse.ArgumentParser(description="standalone parser")
    parser.add_argument('--testbed', dest='testbed',
                        help='testbed YAML file',
                        type=topology.loader.load,
                        default=None)

    args = parser.parse_known_args()[0]
    aetest.main(testbed=args.testbed)
