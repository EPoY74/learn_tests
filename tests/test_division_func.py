"""Тестирую деление
https://youtu.be/1HtEPEn4-LY?si=9JqaJE9hXowgrSg1 
"""
import pytest

from learn_tests.less1 import division


def test_is_division_good():
    """Тестирую деление
    """
    assert division(10,2) == 5


def test_is_division_good_negdtiv_1():
    """Делим А на -В
    """
    assert division(10,-2) == -5


def test_is_division_good_negdtiv_2():
    """Делим -А на В
    """
    assert division(-12,2) == -6

def test_is_division_good_negdtiv_3():
    """Делим -А на -В
    """
    assert division(-10,-2) == 5