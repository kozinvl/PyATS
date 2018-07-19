##Task 1

- Create testbed using next parameters:
  - Single device named `“vm-server”` with `“mac or linux”` OS
  - Device must contain connection: protocol `“telnet”`, ip `“localhost”` and port
  - Use `“loader”` module to load created testbed
- Using only AEtest - check in testcase that the testbed contains device `“vm-server”`

##Task 2

- Use testbed from task 1 and add information about login/password remote device
- Use `SSH` protocol
- Create Test Case:
  - In Setup section connect to device
  - In Test section use command `“whoami”` on device
-	Check that output equal login from testbed

##Task 3
- Create job file and run with CLI (Easypy)
