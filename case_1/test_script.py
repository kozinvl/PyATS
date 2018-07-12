import logging
from ats import aetest
from ats.topology import loader

log = logging.getLogger(__name__)
tb = loader.load("testbed_1.yaml")
server = tb.devices['mohamoha-ads']

server.connect()
#
# class common_setup(aetest.CommonSetup):
#
#     @aetest.subsection
#     def subsection_two(self, section):
#         log.info('Doing something another')
#         log.info("inside %s" % (section))
#
#
# class Testcase_One(aetest.Testcase):
#
#     @aetest.setup
#     def setup(self):
#         log.info("%s Setup/Preparation" % self.uid)
#         self.a = 1
#         self.b = 2
#         self.c = 3
#
#
# class common_cleanup(aetest.CommonCleanup):
#     @aetest.subsection
#     def clean_everything(self):
#         log.info('In Common Cleanup')
#         log.info('Finish')
#
#
# if __name__ == '__main__':
#     aetest.main()
