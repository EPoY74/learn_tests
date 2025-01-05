"""Тестирую деление
"""
import pytest

from learn_tests.less1 import division


def test_is_division_good():
    """Тестирую деление
    """
    assert division(10,2) == 5