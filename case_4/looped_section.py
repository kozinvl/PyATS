from ats import aetest


@aetest.loop(uids=['Case_4', 'Case_4.1'])
class TestCase4(aetest.Testcase):

    @aetest.setup
    def setup(self):
        print('Now in Setup Section')

    # looped test section
    @aetest.loop(uids=['test_1', 'test_2'])
    @aetest.test
    def test(self):
        print('test.....')

    # second variant
    @aetest.test.loop(uids=['test_3', 'test_4'])
    def test_1(self):
        print('test..')

    @aetest.cleanup
    def cleanup(self):
        print('Now in Cleanup Section')


if __name__ == '__main__':
    aetest.main()
