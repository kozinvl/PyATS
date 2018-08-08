"""Example of using 'ping' command, device & connection integration
when given a device object"""

from ats.topology import loader
from ats import topology

testbed = topology.loader.load('''
devices:
    vm424583:
        os: 'linux'
        tacacs:
            username: mshumakov
        passwords:
            linux: mykola00
        connections:
          linux:
            protocol: ssh
            ip: 192.168.242.44
        type: 'linux'
        ''')

device = testbed.devices['vm424583']
test_ip = '108.177.119.103'

# users should be able to directly interface with it, eg:
# connect to it
device.connect()

# send commands
output = device.execute('hostname')
device.ping(test_ip)

assert output in testbed.devices

# disconnect from device
device.disconnect()
