import pytest
from apps.pv_opt.pvpy import OctopusAccount

def test_requires_args():
    with pytest.raises(TypeError):
      OctopusAccount()

def test_values_are_not_mutated():
    # Ensure that values set aren't modified (essentially that the properties remain pass-thru properties).
    expected_account_number = 123456789
    expected_api_key = 987654321
    
    account = OctopusAccount(expected_account_number, expected_api_key)
    
    assert expected_account_number == account.account_number
    assert expected_api_key == account.api_key