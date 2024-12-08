import pytest

from qa.calls import CreateOrder, Reset


@pytest.fixture(autouse=True)
def reset_orders():
    Reset().request()


def test_create_order():
    CreateOrder().request().verify()


def test_create_order_with_discount():
    CreateOrder(price=12.21, quantity=1, discount=0.1).request().verify()
