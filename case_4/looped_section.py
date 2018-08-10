from ats import aetest


@aetest.loop(uids=['Case_4', 'Case_4.1'])
class TestCase4(aetest.Testcase):

    # looped test section
    @aetest.loop(uids=['test_1', 'test_2'])
    @aetest.test
    def test(self, section):
        print("current section: %s" % section.uid)

    # second variant
    @aetest.test.loop(uids=['test_3', 'test_4'], a=[3, 4])
    def test_2(self, a):
        print('test..')
        # if a=[3, 4, 5], 5 will not execute!
        # because of uids[].length == 2
        print("%s ^ 2 = %s" % (a, a * a))


@aetest.loop(a=[4, 5])
class TestCase5(aetest.Testcase):

    @aetest.setup
    def setup(self):
        # mark the next test for looping
        aetest.loop.mark(self.simple_test, uids=['test_one', 'test_two'])

    @aetest.test
    def simple_test(self, section):
        print("current section: %s" % section.uid)

    # loop test with different parameters
    @aetest.test.loop(b=[6, 7])
    def test(self, a, b):
        print("%s x %s = %s" % (a, b, a * b))


if __name__ == '__main__':
    aetest.main()
