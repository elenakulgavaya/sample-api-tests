## Test approach and strategy document

### Introduction
#### Purpose of the document
This test strategy outlines the approach, scope and resources used to
ensure the quality of `Order Creation API`. The purpose is to validate
functionality and security of the endpoint.

#### Goals
The primary objectives are to confirm that API matches the declared 
schema, prove that it creates orders correctly respecting provided discounts
and also ensure it meets minimum security requirements.

#### System under test
The Order Creation API consists of a single endpoint, which based
on the input criteria calculates total and stores new order information
into the system.
There is no information on business needs or the consumers of the API.

This document provides a high-level test strategy to ensure 
the API is robust and secure.

### Scope of Testing
The testing will cover single endpoint which is `/orders/create`. 
Endpoint `reset` is not included into testing scope and is not to be tested.
Authorization part should be covered by the test.
The test types to be performed: automated functional tests.
There won't be done any performance or usability tests as there are no
requirements for those types.

### Test Approach
#### Levels of testing
Testing should be performed on the lowest possible level, with the current 
system we can only do `system` level tests, other levels are not 
available.

#### Test design technic
The `black-box` testing technic will be applied as it's the only available
for test.
Due to the lack of the requirements the `exploratory testing` technic
will be used to define the test cases. At the same point boundary values 
and equivalence classes will be used based on API schema shared.

#### Tools and frameworks
Test automation is performed with the help of Python PyTest framework,
using requests for interacting with APi and fild library for defining 
contracts and generating data.
The test code is stored in git repository and can be used as a test
documentation storing all the testcases.
The CI pipeline is setup using GitHub actions in the test repository
which can be triggered manually and automatically on making changes in tests.

#### Automation strategy
All the test cases should be automated. Automated test is used as a test scenario
with no additional storage for that data. The git repo being the storage 
for the automated test code is also used for versioning test documentation.
Github actions are used to check the status of current tests. 
All the tests should be passing in the main branch. If the issue is introduced
to the system, the behavior of the test should be changed to expect failure
until the issue is fixed.


### Test Environment
The API is provided with no option and/or need ot support the dedicated
environment.
Test data is generated per test and there is no need to store any of it
separately.
Authorization tokens used for test should be secured. The one used in
the automated pipeline should be stored as a project secret, the
should be an option to use personal one for local execution.


### Test Deliverables
 - Test cases in form of automated test scripts
 - Defect reports in [Bug Reports](bugs.md)
 - Current Status in the [README.md](../README.md)


### Defect Management
Defects are going to be reported in [Bug Reports](bugs.md) and 
the corresponding test for reproducing the defect should be marked as
expected to fail. Once the change is made to the SUT fixing the bug, the test
should be unmarked to ensure the bug is fixed and forming back the regression 
suite.
Severity is provided for all the issues, while the priority can not be set
without access to the project management.

### Continuous Testing and Feedback
Test pipeline ideally should be tight to the SUT changes. In the current 
configuration the pipeline is available to be executed upon request by starting
the job from the GitHub Actions page.
Once the tests start to fail the new bug should be created (exsiting reopened).

[BACK](../README.md)
