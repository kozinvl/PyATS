from ats import aetest
import logging
import multiprocessing
from ats.async import Pcall

logger = logging.getLogger(__name__)

# set test variables
test_variable_1 = 50
int_null_variable = 0
test_set_of_ints = (test_variable_1, test_variable_1,
                    test_variable_1, test_variable_1)


# define function to be called in forked processes
def change_params(params):
    params = params + test_variable_1
    return params


class TestCase(aetest.Testcase):

    @aetest.setup
    def setup(self):
        logger.info('Setup from TestCase')

    # create a child process to run the skip function
    @aetest.test
    def multiprocessing_test(self):
        process = multiprocessing.Process(target=self.skipped(
            'This section was skipped'))
        logger.info('It will not printed on the console because of skipped!')
        process.start()
        process.join()
        logger.info('Test section')

    # create a parallel calls to run the function
    @aetest.test
    def parallel_call_test(self):
        # create a Pcall object
        process = Pcall(change_params,
                        params=(int_null_variable, int_null_variable,
                                int_null_variable, int_null_variable))
        # start all child processes
        process.start()
        # wait for everything to finish
        process.join()
        # check results
        assert process.results == test_set_of_ints

    # create a multiple parallel calls to run the function
    @aetest.test
    def parallel_multiple_call_test(self):
        # create a Pcall objects
        process_a = Pcall(change_params,
                          params=(int_null_variable, int_null_variable,
                                  int_null_variable, int_null_variable))
        process_b = Pcall(change_params,
                          params=(int_null_variable, int_null_variable,
                                  int_null_variable, int_null_variable))
        # start all child processes
        process_a.start()
        process_b.start()
        # wait for everything to finish
        process_a.join()
        process_b.join()
        # check results
        assert process_a.results == process_b.results

    @aetest.cleanup
    def cleanup(self):
        logger.info('Cleanup all data from test_case')
