from nose.tools import assert_equals
from sum_of_three import sum3

def test_numbers_0_0_0():
    assert_equals(sum3(0, 0, 0), 0)

def test_numbers_1_2_3():
    assert_equals(sum3(1, 2, 3), 6)

def test_with_negative_numbers():
    assert_equals(sum3(-1, 1, 0), 0)
