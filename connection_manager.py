from ats import topology

# let's write an inline testbed file for simplicity
# (edit this to whatever your testbed looks like)
testbed = topology.loader.load('''
testbed:
    name: my-inline-testbed

devices:
    tplana-hath:
        type: iol
        connections:
            a:
                protocol: telnet
                ip: localhost
                port: 10000
''')

# pick the device to work with
device = testbed.devices['tplana-hath']

# we should be able to directly connect to it
device.connect()
assert device.connected

# run the various services associated with this connection
device.execute('show version')
device.configure('clock set 18:00:00 April 4 2063')

# disconnect from it
device.disconnect()
