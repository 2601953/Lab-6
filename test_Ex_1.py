import pytest
from Ex_1_functions import multiply

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-9, -4) == 36
    assert multiply(6, -3) == -18
    assert multiply(-4, 0) == 0
    assert multiply(0, 4) == 0
    assert multiply("abc", "xyz") == None

pytest.main()