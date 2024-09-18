import pytest
from apps.pv_opt.pvpy import InverterModel

def test_does_not_require_args():
    # Ensure the InverterModel does not require any arguments.
    InverterModel()

def test_default_values():
    # Ensure that the default values are set correctly and if they're ever changed, we get a warning with a failing test.
    inverter = InverterModel()
    
    assert 0.97 == inverter.inverter_efficiency
    assert 0.91 == inverter.charger_efficiency
    assert 100 == inverter.inverter_loss
    assert 3000 == inverter.inverter_power
    assert 3500 == inverter.charger_power