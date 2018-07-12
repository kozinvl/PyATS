"""Example of pyATS work. Used just AETest package"""
import os
from ats.easypy import run


def main():
    """
    main() function is the default easypy job file entry point.
    """

    script_path = os.path.dirname(os.path.abspath(__file__))
    testscript = os.path.join(script_path, 'first_task.py')

    # execute the testscript
    run(testscript=testscript)
#= os.path.join(os.path.dirname(__file__), '..')