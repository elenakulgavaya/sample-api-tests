from fildapi import ApiCaller
from fildapi.config import Cfg
from fildapi.deepdiff import is_valid_uuid, has_some_value

from qa import api


# pylint: disable=arguments-differ


class CreateOrder(ApiCaller):
    method = api.CreateOrder

    def __init__(self, token=None, price=None, quantity=None, discount=None,
                 note=None, updates=None):
        token = token or Cfg.App.token
        self.req_body = api.CreateOrderReq().with_values({
            api.CreateOrderReq.PricePerUnit.name: price,
            api.CreateOrderReq.Quantity.name: quantity,
            api.CreateOrderReq.DiscountRate.name: discount,
            api.CreateOrderReq.Note.name: note,
        })
        super().__init__(
            req_body=self.req_body,
            updates=updates,
            headers={'Authorization': f'Bearer {token}'}
        )

    def calculate_total(self):
        price = self.req_body.PricePerUnit.value
        quantity = self.req_body.Quantity.value
        discount_rate = self.req_body.DiscountRate.value or 0
        result = (price * quantity) * (1 - discount_rate)

        return round(result, 2)

    def verify(self, current_orders=1, error_message=None, error_code=None):
        rules = None

        if error_message:
            error_code = error_code or 400
            resp_body = api.ErrorResp().with_values({
                api.ErrorResp.Error.name: error_message,
            })
        else:
            resp_body = api.CreateOrderResp().with_values({
                api.CreateOrderResp.CurrentOrders.name: current_orders,
                api.CreateOrderResp.OrderDetails.name: {
                    api.OrderDetails.ProductId.name:
                        self.req_body.ProductId.value,
                    api.OrderDetails.PricePerUnit.name:
                        self.req_body.PricePerUnit.value,
                    api.OrderDetails.Quantity.name:
                        self.req_body.Quantity.value,
                    api.OrderDetails.DiscountApplied.name:
                        self.req_body.DiscountRate.value or 0,
                    api.OrderDetails.TotalAmount.name:
                        self.calculate_total()
                }
            })
            rules = {api.CreateOrderResp.OrderDetails.name: {
                api.OrderDetails.OrderId.name: is_valid_uuid,
                api.OrderDetails.ConfirmationCode.name: has_some_value,
            }}

        self.verify_response(
            error_code=error_code or 201,
            resp_body=resp_body,
            rules=rules
        )


class Reset(ApiCaller):
    method = api.Reset

    def __init__(self, token=None):
        token = token or Cfg.App.token
        super().__init__(headers={'Authorization': f'Bearer {token}'})
