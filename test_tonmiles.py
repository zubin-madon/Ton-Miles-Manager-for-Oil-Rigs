import pytest
import functions


def test_calculate_boyed_weight_():
    assert functions.calculate_boyed_weight(2000, 29, 0.75) == 43500/2000
    assert functions.calculate_boyed_weight(0, 29, 0.75) == 0
    assert functions.calculate_boyed_weight(-2000, 29, 0.75) == 0
test_calculate_boyed_weight_()


def test_total_weight_():
    assert functions.cal_total_wt(2000,4000,6000,8000) == 20000
test_total_weight_()


def test_block_ton_miles_():
    assert functions.block_ton_miles(3000, 20) == 22.72727272727273
    assert functions.block_ton_miles(0, 20) == 0
    assert functions.block_ton_miles(2000, 0) == 0
    assert functions.block_ton_miles(0, -20) == 0
    assert functions.block_ton_miles(-2000, 0) == 0
test_block_ton_miles_()
