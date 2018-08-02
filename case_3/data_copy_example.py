from ats.topology import loader
from ats import topology
from ats.utils.fileutils import FileUtils

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

# loading testbed immediately
tb = topology.loader.load('''
devices:
    remote_device:
        os: 'linux'
        tacacs:
            username: vkozin
        passwords:
            linux: '159753852'
        connections:
          linux:
            protocol: ssh
            ip: 192.168.242.44
        type: 'linux'
''')

# input data in remote file
string_configuration = 'data for script'

device = tb.devices['remote_device']

device.connect()
device.execute('cd /tmp')
device.execute("echo '{}' > demo.txt".format(string_configuration))
