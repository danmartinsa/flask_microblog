import pytest
from codigo import add_numbers

@pytest.fixture(scope="session")
def y_value():
    return 10

@pytest.mark.parametrize(
        "a, b, expected", [
            (1,2,13),
            (2,3,14),
            (3,5,18),
            ]
        )
def test_with_param(a,b,expected, y_value):
    assert add_numbers(a, b, y_value) == expected
