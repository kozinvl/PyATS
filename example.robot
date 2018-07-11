# Example
# -------
#
#   Demonstration of pyATS Robot Framework Keywords

*** Settings ***
# Importing test libraries, resource files and variable files.

Library        ats.robot.pyATSRobot

*** Variables ***
# Defining variables that can be used elsewhere in the test data.
# Can also be driven as dash argument at runtime

${datafile}     datafile.yaml
${testbed}      testbed.yaml

*** Test Cases ***
# Creating test cases from available keywords.

Initialize
    # select the testbed to use
    use testbed "${testbed}"

    # connec to testbed device through cli
    connect to device "ios" as alias "cli"

CommonSetup
    # calling pyats common_setup
    run testcase "basic_example_script.common_setup"

Testcase pass
    # calling pyats testcase
    run testcase "basic_example_script.tc_one"


#Keywords FR
#connect to all devices
#Connect to all devices
#
#connect to device "${device:[^"]+}"
#Connect to device connection as defined in testbed.yaml
#
#connect to device "${device:[^"]+}" as alias "${alias:[^"]+}"
#Connect to a device via non-default alias.
#
#connect to device "${device:[^"]+}" via "${via:[^"]+}"
#Connect to a device with non-default via.
#
#connect to device "${device:[^"]+}" via "${via:[^"]+}" as alias "${alias}"
#Create a new alias by connecting to a device via non-default connection
#
#connect to devices "${devices}"
#Connect to devices via connection as defined in testbed.yaml. Specify devices with semi-colon separated list, e.g. "R1;R2"
#
#disconnect from all devices
#Disconnect from devices with default alias. Specify devices with semi-colon separated list, e.g. "R1;R2"
#
#disconnect from device "${device:[^"]+}"
#Disconnect from device with default alias
#
#disconnect from device "${device:[^"]+}" with alias "${alias}"
#Disconnect from device using alias
#
#run testcase	python_path, *args, **kwargs
#The keyword allow to call any pyATS testcase by passing the full python path of the testcase.
#
#run testcase "${pythonpath:[^"]+}"
#The keyword allow to call any pyATS testcase by passing the full python path of the testcase.
#
#use testbed "${testbed}"
#Load testbed YAML file and instantiate testbed object