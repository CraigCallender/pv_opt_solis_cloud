import pytest
from apps.pv_opt.pvpy import BatteryModel

def test_requires_args():
    # Dummy test to ensure that the pytest setup works.
    with pytest.raises(TypeError):
        BatteryModel()

def test_default_values():
    # Ensure that the default values are set correctly and if they're ever changed, we get a warning with a failing test.
    battery = BatteryModel(capacity=1000)

    assert 0.15 == battery.max_dod
    assert 1000 == battery.capacity
    assert 100 == battery.current_limit_amps
    assert 50 == battery.voltage

def test_max_charge_power_calculated_correctly():
    # Ensure that the charge_power() calculation is correct.
    expected : int = 1250 # 25V * 50A = 1250W
    battery = BatteryModel(capacity=1000, current_limit_amps=50, voltage=25)

    assert expected == battery.max_charge_power

def test_max_discharge_power_calculated_correctly():
    # Ensure that the charge_power() calculation is correct.
    expected : int = 1250 # 25V * 50A = 1250W
    battery = BatteryModel(capacity=1000, current_limit_amps=50, voltage=25)

    assert expected == battery.max_discharge_power

def test_values_are_not_mutated():
    # Ensure that values set aren't modified (essentially that the properties remain pass-thru properties).
    expected_capacity = 1234
    expected_max_dod = 0.5
    expected_current_limit_amps = 33
    expected_voltage = 24
    
    battery = BatteryModel(expected_capacity, expected_max_dod, expected_current_limit_amps, expected_voltage)
    
    assert expected_capacity == battery.capacity
    assert expected_max_dod == battery.max_dod
    assert expected_current_limit_amps == battery.current_limit_amps
    assert expected_voltage == battery.voltage
