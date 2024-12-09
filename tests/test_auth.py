import pytest

from fild.sdk.fakeable import Fakeable, fake_string_attr

from qa.calls import CreateOrder


def test_invalid_token():
    CreateOrder(token=fake_string_attr(Fakeable.IosToken)).request().verify(
        error_code=403, error_message='Forbidden'
    )


@pytest.mark.xfail(strict=True, reason='issue #14')
def test_missing_token():
    CreateOrder(token='').request().verify(
        error_code=403, error_message='Forbidden'
    )
