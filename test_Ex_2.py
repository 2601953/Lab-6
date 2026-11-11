import pytest
from Ex_2_functions import sorted_string

def test_sorted_string():
    assert sorted_string("hello") == "ehllo"
    assert sorted_string("Python") == "hnoPty"
    assert sorted_string("12345") == "12345"
    assert sorted_string("") == ""
    assert sorted_string("a") == "a"

pytest.main()