## Suggestions for API improvements

1. Implement generic validation based on schema (use schema validator). Currently
not only the validation is not working properly, but the error messages are not 
unified.
2. This depends a lot on the consumers of the APi and also the business needs
but I would suggest not duplicating the information sent within the request
in the response. If the decision is made to keep the fields, then consider 
truly having all the fields provided (including `note`)
3. Discount provided as a separate field should be a subject of validation if 
it can actually be applied to the specific order
4. Depending on the business logic and consumers but I would suggest moving 
information on `current_orders` into a separate endpoint, rather than having
it mixed with the new order info. With my assumption there that there are 
endpoints for edit/read/update/delite orders as well.

[BACK](../README.md)
