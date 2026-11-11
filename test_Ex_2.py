import pytest
from Ex_2_functions import reverse

def test_reverse():
    assert reverse("hello") == "olleh"
    assert reverse("Python") == "nohtyP"
    assert reverse("12345") == "54321"
    assert reverse("") == ""
    assert reverse("a") == "a"

pytest.main()