"""Example of Easypy module work. Job file tasks using
Task() api (sequential execution)
(recreating the same job file as run() api example using Task class)
To run job file write in terminal 'easypy easypy_large_example_job.py'"""

from ats.easypy import Task
from ats.easypy import run

# Define the waiting time in advance
timeout = 300


# each job file must have a main() function defined.
# This is the main entry point of a job file run.
def main(runtime):
    # using Task class to create a task object with "first_example.py"
    # (max runtime = 60*5 seconds = 5 minutes)
    task_1 = Task(testscript='first_example.py',
                  runtime=runtime,
                  taskid='example_task_1')

    # start the task
    task_1.start()

    # wait for a max runtime of 300 seconds = 5 minutes
    task_1.wait(timeout)

    # check whether the next script should continue
    # based on previous task's results.
    if task_1.result:
        # last result passed, run the next task
        task_2 = Task(testscript='second_example.py',
                      runtime=runtime,
                      taskid='example_task_2')

        # start & wait
        task_2.start()
        task_2.wait(timeout)

    # execute the third test script
    run('third_example.py')
