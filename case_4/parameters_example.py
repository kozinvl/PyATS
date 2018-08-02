from ats import aetest
import random

# static base value
a = 'static value'
# static dict
parameters = {'param_A': 'default_value', 'param_B': 10, 'param_C': [], 'param_D': dict()}


class TestCase(aetest.Testcase):
    # local parameters
    parameters = {'param_E': 'not_default_value'}

    @aetest.setup
    def setup(self):
        # update parameters
        self.parameters['param_F'] = 'self_value'
        self.parameters['param_A'] = 'this_value'

    @aetest.test
    def test(self):
        # print testscript parameters
        # access & print parent testscript parameters
        print(self.parent.parameters)
        # access & print all current known parameter
        # this also includes any parameters from the parent
        print(self.parameters)
        print(a)

    @aetest.test
    def test_1(self):
        pass


new_dict = {'param_G': 'new_value', 'digit': random.random}
# update static dict
parameters.update(new_dict)


class TestCase2(aetest.Testcase):
    @aetest.setup
    def setup(self, param_D):
        # param_D is a dictionary (mutable)
        # any modification to this dictionary persists
        param_D['key'] = 'value'

    # section needing both "param_A" and "param_B"
    @aetest.test
    def test_one(self, param_A, param_D):
        print(param_A)
        print(param_D)

    @aetest.test
    def test_two(self, digit, param_non_existent=998):
        print(param_non_existent)
        print(digit)
        assert digit > 0.0001

    # using arbitrary keywords **kwargs
    # all known parameters are passed in as a dictionary
    @aetest.cleanup
    def cleanup(self, **kwargs):
        print(kwargs)


# defining a parametrized function
@aetest.parameters.parametrize(lower_bound=1, upper_bound=100)
def generate_number(lower_bound, upper_bound):
    return random.randint(lower_bound, upper_bound)


class TestCase3(aetest.Testcase):
    @aetest.test
    def expected_to_pass(self, generate_number, expectation=1):
        # test whether expectation is < than generated number
        print(generate_number)
        assert expectation < generate_number


if __name__ == '__main__':
    aetest.main()
