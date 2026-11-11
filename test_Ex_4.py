import pytest
from Ex_4_functions import movie_ticket_price

def test_movie_ticket_price():
    assert movie_ticket_price(0, 1, 0, 10) == 14.25
    assert movie_ticket_price(2, 2, 0, 17) == 30
    assert movie_ticket_price(2, 2, 0, 13) == 28.50

pytest.main()