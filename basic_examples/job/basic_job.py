import ats
import os
from ats.easypy import run

def main():
    '''
    main() function is the default easypy job file entry point.
    '''

    # eind the location of the script in relation to the job file
    script_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    testscript = os.path.join(script_path, 'test_script.py')
    print(script_path)
    print(testscript)

    # execute the testscript
    run(testscript=testscript)

