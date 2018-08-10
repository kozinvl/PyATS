"""Example of using 'ping' command, device & connection integration
when given a device object"""

from ats.topology import loader
from ats import topology
from ats.topology import Testbed, Device, Interface, Link

test_ip = '108.177.119.103'
device = Device('vm',
                tacacs={
                    'username': 'mshumakov'
                },
                passwords={
                    'enable': ' ',
                    'tacacs': ' ',
                    'line': ' '},
                connections={
                    'linux': {
                        'protocol': 'telnet',
                        'ip': '192.168.242.44'
                    },
                })

interface_a = Interface('Ethernet1/1',
                        type='ethernet',
                        ipv4='10.129.201.101'
                        )
device.add_interface(interface_a)
testbed = Testbed(name='myTestbed')
testbed.add_device(device)
device.testbed = testbed

link_a = Link('emptyLink')
link_a.connect_interface(interface_a)
# device.connectionmgr.connect()
device.connect()
device.is_connected()
device.default()
device.default.execute('ping' + test_ip)
device.ping(test_ip)

# users should be able to directly interface with it, eg:
# connect to it

# send commands
output = device.execute('hostname')
device.ping(test_ip)

assert output in testbed

# disconnect from device
device.disconnect()
