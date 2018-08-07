from ats.topology import loader
from ats import topology
from ats.utils.fileutils import FileUtils

# local imports
import sys
import argparse
from ats.topology import loader

# loading testbed immediately
tb = topology.loader.load('testbed.yaml')

# input data in remote file
string_configuration = 'Welcome to pyATS'

device = tb.devices['remote_device']

device.connect()
device.execute('cd /tmp')
device.execute('cat New_file.txt')
device.execute("echo '{}' > New_file.txt".format(string_configuration))
