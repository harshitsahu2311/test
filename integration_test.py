# integration_test.py
from app import divide

def test_api_logic():
    result = divide(20, 4)
    assert result == 5
