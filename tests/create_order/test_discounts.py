import pytest

from qa.calls import CreateOrder, Reset


@pytest.fixture(autouse=True)
def reset_orders():
    Reset().request()


@pytest.mark.xfail(strict=True, reason='issues #3, #1, #2')
def test_create_order_with_discount():
    CreateOrder(price=12.21, quantity=1, discount=0.1).request().verify()


@pytest.mark.xfail(strict=True, reason='issues #3, #1, #2')
def test_discount_on_multiple_items():
    CreateOrder(price=15.98, quantity=3, discount=0.2).request().verify()


@pytest.mark.xfail(strict=True, reason='issues #3, #1, #2')
def test_full_price_discount():
    CreateOrder(price=2.4, quantity=10, discount=1).request().verify()
