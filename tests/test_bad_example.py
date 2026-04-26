import pytest
from bad_example import average_age



def test_average_age_basic_case():
    records = [
        {'name': 'Anna', 'age': 20},
        {'name': 'Jan', 'age': 30},
    ]
    assert average_age(records) == 25


def test_average_age_empty_list():
    with pytest.raises(Exception):
        average_age([])
