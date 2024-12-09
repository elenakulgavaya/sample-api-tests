import pytest

from qa.calls import CreateOrder, Reset


@pytest.fixture(autouse=True)
def reset_orders():
    Reset().request()


@pytest.mark.xfail(strict=True, reason='issues #1, #2')
def test_create_second_order():
    CreateOrder().request()
    CreateOrder().request().verify(current_orders=2)


@pytest.mark.xfail(strict=True, reason='issues #1, #2')
def test_create_multiple_orders():
    for _ in range(3):
        CreateOrder().request()

    CreateOrder().request().verify(current_orders=4)


@pytest.mark.xfail(strict=True, reason='issues #1, #2')
def test_create_order_after_reset():
    CreateOrder().request()
    Reset().request()
    CreateOrder().request().verify(current_orders=1)
