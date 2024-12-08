# sample-api-tests


## Issues found
### Data formats:
In the `/orders/create` response the following fields do not correspond to the 
declared schema:
1. `order_id`: is a numeric string, while expected was uuid
2. `delivery_date` format doesn't conform to declared `YYYY-MM-DD`

Test to reproduce: 

### Discount does not change order total
When requesting `orders/create` with the discount, the response indicates 
discount has been applied by the valid value in `discount_applied` field
but the `total_amount` doesn't show any effects of it.

Test to reproduce: 
