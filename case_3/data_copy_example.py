from ats import aetest
from ats.topology import loader
from ats.utils.fileutils import FileUtils
from genie.libs import filetransferutils

# Transferring a single file to or from a remote server
tb = loader.load("testbed.yaml")

this_device = FileUtils.from_device(tb.devices['virtual_device'])

this_device.copyfile(source='flash: ~/tmp/demo.txt',
                     destination='tftp:/server_alias/path/to/file')
