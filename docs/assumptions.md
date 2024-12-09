## Assumptions and limitations

The following list of assumptions and limitations is not orderd
by priority.

- There is no access to the internal part of the API (database or 
other type of storage) to verify the order is created indeed and 
the values returned are relevant to the actual state system.
- If reset endpoint is broken, there is no way to check the number
of current_orders in the response
- Authorization token should have the expiration period and will require
maintainance within the automated suite
- There is no access to the initial api to setup the execution
pipeline being triggerable by the actual changes. 
- There is no any information about the system architecture and 
environment, which makes it hard to set the expectations on performance
making any performance testing not valuable at the moment
- There is no documentation on the use cases/business expectations
set for the api, so even fixing all the bugs found will not make
us sure the API is of an appropriate quality. Same is valid for suggestions
on the API, they might be irrelevant to the business requirements.
- There are no preparations in the test suite for the versioning tests as there 
is only one version at the moment and though the structure suggests having
next one potentially, this didn't happen at that time and may actually never
happen.
- There is no elegant way to check the order was not created in case of invalid 
data provided other than creating a valid order and checking the number
- There is no information on what is product id, whether it's something the 
system is expected to have in the database or just a random number

[BACK](../README.md)
