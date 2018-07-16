"""Example of pyATS work. Used AETest package and
Easypy module - 'easypy first_example_job.py'"""
import os
from ats.easypy import run


def main():
    """
    main() function is the default easypy job file entry point.
    """

    script_path = os.path.dirname(os.path.abspath(__file__))
    testscript = os.path.join(script_path, 'first_example.py')

    # execute the testscript
    run(testscript=testscript)
