import logging

logger = logging.getLogger(__name__)


def function_supporting_step(step):
    '''function_supporting_step
    This function demonstrate the use of steps within function APIs.
    '''

    with step.start('function step one'):
        # do some meaningful testing
        pass

    with step.start('function step two'):
        # do some meaningful testing
        pass

    with step.start('function step three'):
        # do some meaningful testing
        pass

    return
