#Connect to a device using CLI

*** Settings ***
Library        ats.robot.pyATSRobot
Library        genie.libs.robot.GenieRobot
Library        unicon.robot.UniconRobot


*** Variables ***
# Defining variables that can be used elsewhere in the test data.
${testbed}     /genie_tests/default_testbed.yaml


*** TestCases ***
# Creating testcases using available Genie, PyATS & Unicon keywords


# Connect to a device using CLI as the communication protocol
connect to device with CLI
    use genie testbed "${testbed}"
    connect to devices "uut"



#Keywords Genie Robot
#Compare profile "${pts:[^"]+}" with "${pts_compare:[^"]+}" on devices "${devices:[^"]+}"
#Compare system profiles taken as snapshots during the run
#
#learn "${feature:[^"]+}" on device "${device:[^"]+}"
#Learn Ops feature on device
#
#learn "${feature:[^"]+}" on device "${device:[^"]+}" using alias "${alias:[^"]+}"
#Learn Ops feature on device using a specific alias
#
#learn "${feature:[^"]+}" on device "${device:[^"]+}" using alias "${alias:[^"]+}" with context "${context:[^"]+}"
#Learn Ops feature on device using a specific alias with a context (cli, xml, yang, ...)
#
#learn "${feature:[^"]+}" on device "${device:[^"]+}" with context "${context:[^"]+}"
#Learn Ops feature on device with a context (cli, xml, yang, ...)
#
#parse "${parser:[^"]+}" on device "${device:[^"]+}"
#Call any metaparser parser and parse the device output.
#
#parse "${parser:[^"]+}" on device "${device:[^"]+}" using alias "${alias:[^"]+}"
#Call any metaparser parser and parse the device using a specific alias
#
#parse "${parser:[^"]+}" on device "${device:[^"]+}" using alias "${alias:[^"]+}" with context "${context}"
#Call any metaparser parser and parse the device using a specific alias with a context (cli, xml, yang, ...)
#
#parse "${parser:[^"]+}" on device "${device:[^"]+}" with context "${context}"
#Call any metaparser parser and parse the device output with a context (cli, xml, yang, ...)
#
#Profile the system for "${feature:[^"]+}" on devices "${device:[^"]+}" as "${name:[^"]+}"
#Profile system as per the provided features on the devices
#
#Profile the system for "${feature:[^"]+}" on devices "${device:[^"]+}" as "${name:[^"]+}" using alias "${alias:[^"]+}"
#Profile system as per the provided features on the devices filtered using alias
#
#Run trigger "${name:[^"]+}" on device "${device:[^"]+}"
#Call any trigger defined in the trigger datafile on device
#
#Run trigger "${name:[^"]+}" on device "${device:[^"]+}" using alias "${alias:[^"]+}"
#Call any trigger defined in the trigger datafile on device using a specific alias
#
#Run trigger "${name:[^"]+}" on device "${device:[^"]+}" with context "${context:[^"]+}"
#Call any trigger defined in the trigger datafile on device with a context (cli, xml, yang, ...)
#
#Run trigger "${name}" on device "${device:[^"]+}" using alias "${alias:[^"]+}" with context "${context:[^"]+}"
#Call any trigger defined in the trigger datafile on device using a specific alias with a context (cli, xml, yang, ...)
#
#Run verification "${name:[^"]+}" on device "${device:[^"]+}"
#Call any verification defined in the verification datafile on device
#
#Run verification "${name:[^"]+}" on device "${device:[^"]+}" using alias "${alias:[^"]+}"
#Call any verification defined in the verification datafile on device using a specific alias
#
#Run verification "${name:[^"]+}" on device "${device:[^"]+}" using alias "${alias:[^"]+}" with context "${context:[^"]+}"
#Call any verification defined in the verification datafile on device using a specific alias with a context (cli, xml, yang, ...)
#
#Run verification "${name:[^"]+}" on device "${device:[^"]+}" with context "${context:[^"]+}"
#Call any verification defined in the verification datafile on device with a context (cli, xml, yang, ...)
#
#use genie testbed "${testbed}"
#Create the genie testbed
#
#verify count "${number:[^"]+}" "${structure:[^"]+}" on device "${device:[^"]+}"
#Verify that a specific number of <...> is <...> on a device.
#
#Supports the same functionality as the alias keyword.
#
#verify count "${number:[^"]+}" "${structure:[^"]+}" on device "${device:[^"]+}" using alias "${alias:[^"]+}"
#Verify that a specific number of <...> is <...> on a device using a specific alias
#
#verify count "<number>" "bgp neighbors" on device "<device>"
#
#verify count "<number>" "bgp routes" on device "<device>"
#
#verify count "<number>" "ospf neighbors" on device "<device>"
#
#verify count "<number>" "interfaces neighbors" on device "<device