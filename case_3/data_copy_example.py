from ats import aetest
from ats.topology import loader
from ats.utils.fileutils import FileUtils
from genie.libs import filetransferutils

# Transferring a single file to or from a remote server

tb = loader.load("testbed.yaml")

# Instanciate a filetransferutils instance for the device corresponding
# to the device specific OS
this_device = FileUtils.from_device(tb.devices['my_device'])

# copy from remote to local machine
this_device.copyfile(source='scp://remote_server:/tmp/demo.txt',
                     destination='/Users/vkozin/Downloads/',
                     timeout_seconds=15)

# copy from local to remote machine
this_device.copyfile(source='/Users/vkozin/Downloads/Task_1.docx',
                     destination='scp://remote_server:/tmp/',
                     timeout_seconds=15)
