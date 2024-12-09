import pytest

from qa.calls import CreateOrder, Reset


@pytest.fixture(autouse=True)
def reset_orders():
    Reset().request()


def test_create_order():
    CreateOrder().request().verify(skip_types=False)


def test_create_order_with_note():
    CreateOrder(note='Order information').request().verify()
