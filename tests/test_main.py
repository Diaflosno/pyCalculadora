import pytest
from src.main import sum, comparacion, resta, multiplicacion, division, numero_par

def test_sum():
    assert sum(10,5) == 15

def test_comparacion():
    assert comparacion(10,2) == 1

def test_resta():
    assert resta(10,5) == 5

def test_multiplicacion():
    assert multiplicacion(10,5) == 50

def test_division():
    assert division(10,5) == 2

def test_numero_par():
    assert numero_par(10) == True
    assert numero_par(5) == False
