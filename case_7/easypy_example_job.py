# Example
# -------
#
#   job file tasks using Task() api (sequential execution)
#   (recreating the same job file as run() api example using Task class)
from ats.topology import loader
from ats import topology
from ats.easypy import Task


# main() function
def main(runtime):
    # using Task class to create a task object
    # (max runtime = 60*5 seconds = 5 minutes)
    task_1 = Task(testscript='first_example.py',
                  runtime=runtime,
                  taskid='example_task_1')

    # start the task
    task_1.start()

    # wait for a max runtime of 60*5 seconds = 5 minutes
    task_1.wait(60 * 5)

    # check whether the next script should continue
    # based on previous task's results.
    if task_1.result:
        # last result passed, run the next task
        task_2 = Task(testscript='second_example.py',
                      runtime=runtime,
                      taskid='example_task_1')

        # start & wait
        task_2.start()
        task_2.wait(60 * 5)
