"""Example of pyATS work. Used AETest package and
To run job file write in terminal 'easypy multiprocess_example_job.py'"""
import os
from ats.easypy import run


# main() function is the default easypy job file entry point.
def main():
    # definition of the path to test script
    script_path = os.path.dirname(os.path.abspath(__file__))
    testscript = os.path.join(script_path, 'multiprocess_example.py')

    # execute the testscript
    run(testscript=testscript)
