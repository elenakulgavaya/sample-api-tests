import pytest

from qa.calls import CreateOrder, Reset


@pytest.fixture(autouse=True)
def reset_orders():
    Reset().request()


@pytest.mark.xfail(strict=True, reason='issues #1, #2')
def test_create_order():
    CreateOrder().request().verify()


@pytest.mark.xfail(strict=True, reason='issues #1, #2')
def test_create_order_with_note():
    CreateOrder(note='Order information').request().verify()
