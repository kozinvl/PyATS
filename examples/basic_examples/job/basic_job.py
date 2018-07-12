import ats
import os
from ats.easypy import run
import ats.easypy


def main():
    """
    main() function is the default easypy job file entry point.
    """

    script_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    testscript = os.path.join(script_path, 'first_task.py')

    # execute the testscript
    run(testscript=testscript)
