from ats import aetest
from ats.topology import loader
from ats.utils.fileutils import FileUtils
from genie.libs import filetransferutils

# Transferring a single file to or from a remote server
tb = loader.load("testbed.yaml")

this_device = FileUtils.from_device(tb.devices['remote_device'])

this_device.copyfile(source='scp://remote_server:/tmp/demo.txt',
                     destination='/Users/vkozin/Downloads/',
                     timeout_seconds=15)

assert this_device.is_local('/Users/vkozin/Downloads/demo.txt')
