from fild.sdk import Dictionary, Float, Int, String, Uuid
from fild.sdk.fakeable import Fakeable
from fildapi import ApiMethod, HttpMethod

API_URL = 'api/v1'


class CreateOrderReq(Dictionary):
    ProductId = Int(name='product_id', min_val=1)
    Quantity = Int(name='quantity', min_val=1)
    DeliveryDate = String(name='delivery_date', fake_as=Fakeable.Date)
    PricePerUnit = Float(name='price_per_unit', min_val=0, f_len=2)
    DiscountRate = Float(name='discount_rate', min_val=0, max_val=1, f_len=2,
                         required=False)
    Note = String(name='note', fake_as=Fakeable.Sentence, required=False)


class OrderDetails(Dictionary):
    OrderId = Uuid(name='order_id')
    ProductId = Int(name='product_id', min_val=1)
    Quantity = Int(name='quantity', min_val=1)
    DeliveryDate = String(name='delivery_date', fake_as=Fakeable.Date)
    PricePerUnit = Float(name='price_per_unit', min_val=0, f_len=2)
    DiscountApplied = Float(name='discount_applied', min_val=0, max_val=1,
                            f_len=2, default=0)
    TotalAmount = Float(name='total_amount', min_val=0, f_len=2)
    ConfirmationCode = String(name='confirmation_code')


class CreateOrderResp(Dictionary):
    CurrentOrders = Int(name='current_orders', min_val=0)
    OrderDetails = OrderDetails(name='order_details')


class CreateOrder(ApiMethod):
    method = HttpMethod.POST
    url = '/orders/create'
    req_body = CreateOrderReq
    resp_body = CreateOrderResp


class Reset(ApiMethod):
    method = HttpMethod.POST
    url = '/reset'
