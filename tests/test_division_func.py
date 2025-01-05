"""Тестирую деление
https://youtu.be/1HtEPEn4-LY?si=9JqaJE9hXowgrSg1 
"""
import pytest

from learn_tests.less1 import division

@pytest.mark.parametrize('a, b, result',
                         [(10,5,2),
                          (-10, 5, -2),
                          (10, -5, -2),
                          (-10, -5, 2),
                          (5, 2, 2.5),
                          (-5, 2, -2.5),
                          (5, -2, -2.5),
                          (-5,-2, 2.5)] )
def test_is_division_good(a:int, b:int, result: float):
    """Тестирую деление
    """
    assert division(a,b) == result

