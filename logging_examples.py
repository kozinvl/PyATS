import sys
import logging
from ats.log import ScreenHandler
from ats.log.utils import banner
from ats.log.utils import title
import time

# get the root logger
logger = logging.getLogger(__name__)

# create handler (defaults to STDOUT)
handler = ScreenHandler()
# or, if you want to output to STDERR, use below instead
handler = ScreenHandler(sys.stderr)

# add handler to logger
logger.addHandler(handler)

# now try logging :)
logger.critical('A critical message')
logger.error(banner('an error message\nwith newline'))
time.sleep(1)

msg = banner('Something Done Wrong', v_margin='~', h_margin='~')
print(msg)

msg = banner('a banner message')
print(msg)
print(banner('Another Text Message',
             width = 80))

msg = title('a title message')
print(msg)

