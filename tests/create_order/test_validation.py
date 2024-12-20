import pytest

from fild.sdk.fakeable import fake_string_attr, Fakeable

from qa import api
from qa.calls import CreateOrder, Reset


@pytest.fixture(autouse=True)
def check_order_not_created():
    Reset().request()

    yield
    # Check on valid order submit the current orders is 1, not 2
    # Which means the order with invalid data has not been created
    current_orders = CreateOrder().request().response.json().get(
        api.CreateOrderResp.CurrentOrders.name
    )
    assert current_orders == 1, 'Unexpected orders in the list'


@pytest.mark.xfail(strict=True, reason='issue #6')
@pytest.mark.parametrize(argnames=['value', 'error_message'], argvalues=[
    (fake_string_attr(Fakeable.Uuid), 'Invalid product_id: must be a number'),
    ('test_value', 'Invalid product_id: must be a number'),
], ids=['uuid', 'string'])
def test_invalid_product_id(value, error_message):
    CreateOrder(updates={
        api.CreateOrderReq.ProductId.name: value
    }).request().verify(error_message=error_message)


def test_invalid_quantity_string():
    CreateOrder(updates={
        api.CreateOrderReq.Quantity.name: 'test'
    }).request().verify(error_message='Invalid quantity: must be a number')


@pytest.mark.xfail(strict=True, reason='issue #7')
@pytest.mark.parametrize(argnames=['value', 'error_message'], argvalues=[
    (0, 'price_per_unit cannot be less than 0.01'),
    (-1, 'price_per_unit cannot be negative'),
    (0.5, 'Invalid quantity: must be a number'),
], ids=['zero', 'negative', 'float'])
def test_invalid_quantity_number(value, error_message):
    CreateOrder(updates={
        api.CreateOrderReq.Quantity.name: value
    }).request().verify(error_message=error_message)


@pytest.mark.parametrize('value', ['test', '01-01-1990'],
                         ids=['string', 'wrong_format'])
def test_invalid_delivery_date(value):
    CreateOrder(updates={
        api.CreateOrderReq.DeliveryDate.name: value
    }).request().verify(
        error_message='Invalid date format. Use YYYY-MM-DD format'
    )


@pytest.mark.parametrize(argnames=['value', 'error_message'], argvalues=[
    ('test', 'Invalid price_per_unit: must be a number'),
    (-1, 'price_per_unit cannot be negative'),
], ids=['string', 'negative'])
def test_invalid_price_per_unit(value, error_message):
    CreateOrder(updates={
        api.CreateOrderReq.PricePerUnit.name: value
    }).request().verify(error_message=error_message)


@pytest.mark.xfail(strict=True, reason='issue #8')
def test_invalid_price_per_unit_zero():
    CreateOrder(updates={
        api.CreateOrderReq.PricePerUnit.name: 0
    }).request().verify(
        error_message='price_per_unit cannot be less than 0.01'
    )


@pytest.mark.xfail(strict=True, reason='issue #9')
@pytest.mark.parametrize(argnames=['value', 'error_message'], argvalues=[
    ('test', 'Invalid discount_rate: must be a number'),
    (2, 'discount_rate cannot be greater than 1'),
    (-1, 'discount_rate cannot be negative'),
], ids=['string', 'too_big', 'negative'])
def test_invalid_discount_rate(value, error_message):
    CreateOrder(updates={
        api.CreateOrderReq.DiscountRate.name: value
    }).request().verify(error_message=error_message)


@pytest.mark.xfail(strict=True, reason='issues #4, #5')
def test_check_if_note_is_escaped():
    CreateOrder(updates={
        api.CreateOrderReq.Note.name: "'; IF (1=2) WAITFOR DELAY '0:0:20'--"
    }).request().verify()


@pytest.mark.xfail(strict=True, reason='issue #10')
def test_missing_required_field_product_id():
    field_name = api.CreateOrderReq.ProductId.name
    CreateOrder(updates={field_name: None}).request().verify(
        error_message=f'{field_name} is required'
    )


@pytest.mark.xfail(strict=True, reason='issue #11')
def test_missing_required_field_quantity():
    field_name = api.CreateOrderReq.Quantity.name
    CreateOrder(updates={field_name: None}).request().verify(
        error_message=f'{field_name} is required'
    )


@pytest.mark.xfail(strict=True, reason='issue #12')
def test_missing_required_field_delivery_date():
    field_name = api.CreateOrderReq.DeliveryDate.name
    CreateOrder(updates={field_name: None}).request().verify(
        error_message=f'{field_name} is required'
    )


@pytest.mark.xfail(strict=True, reason='issue #13')
def test_missing_required_field_price_per_unit():
    field_name = api.CreateOrderReq.PricePerUnit.name
    CreateOrder(updates={field_name: None}).request().verify(
        error_message=f'{field_name} is required'
    )
