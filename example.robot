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
