'''example_job.py

This is the example job file for both comprehensive examples: the base_example
script and variant_example script.

In this jobfile, we'll demonstrate the purpose & configurability of job files,
and as well demonstrate some AEtest features.

Examples:
    # to run under standalone execution
    bash$ python base_example.py

    # to run under easypy
    bash$ easypy job/example_job.py

References:
   For the complete and up-to-date user guide on pyATS, visit:
    https://developer.cisco.com/site/pyats/docs/
'''

#
# optional author information
#
__author__ = 'Siming Yuan <siyuan@cisco.com>'
__copyright__ = 'Copyright 2017, Cisco Systems'
__email__ = 'pyats-support-ext@cisco.com'
__date__ = 'Nov 14, 2017'

#
# import block
#
import os
import logging
import argparse

from ats.easypy import run
from ats.datastructures.logic import And, Or, Not

loglevel = os.environ.get('loglevel', 'WARNING')
groups = os.environ.get('execution_group', None)
my_variable = os.environ.get('my_variable', 'default_value')

parser = argparse.ArgumentParser(description='example job file cli args parser')
parser.add_argument('--argument_a',
                    help='example argument a',
                    default=None)
parser.add_argument('--argument_b',
                    help='example argument b',
                    default=None)

labels = {}
routers = []
links = []
tgns = []

# Different routers and labels for another run()
routers2 = ['router_1']
labels2 = {
    'uut': 'router_1',
}

script_path = os.path.join(os.path.dirname(__file__), '..')


def main(runtime):
    custom_args = parser.parse_known_args()[0]
    logging.getLogger('ats.aetest').setLevel('INFO')
    logging.getLogger('libs').setLevel('DEBUG')
    logging.getLogger('ats.aetest').setLevel('INFO')
    logging.getLogger('libs').setLevel('DEBUG')

    run(testscript=os.path.join(script_path, 'extended_testscript.py'),
        runtime=runtime,
        parameter_A='jobfile value A',
        labels=labels,
        routers=routers,
        links=links,
        tgns=tgns)

    run(testscript=os.path.join(script_path, 'extended_testscript.py'),
        runtime=runtime,
        parameter_A='jobfile value A',
        labels=labels2,
        routers=routers2,
        links=links,
        tgns=tgns)
