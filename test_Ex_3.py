import pytest
from Ex_3_functions import find_common_elements

def test_find_common_elements():
    assert find_common_elements([1, 2, 3], [3, 4, 5]) == [3]
    assert find_common_elements([1, 2, 3], [4, 5, 6]) == []
    assert find_common_elements([1, 2, 3], [1, 2, 3]) == [1, 2, 3]
    assert find_common_elements([], [1, 2, 3]) == []
    assert find_common_elements([1, 2, 3], []) == []

pytest.main()