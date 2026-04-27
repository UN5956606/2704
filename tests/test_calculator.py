import pytest
from calculator import *

class TestCalculateSimpleInterest:
  def test_normal(self):
    assert calculate_simple_interest(100, 2, 2) == 4.0
    assert calculate_simple_interest(200, 2, 2) == 8.0
  
  def test_zero(self):
    assert calculate_simple_interest(00, 2, 2) == 0.0
    assert calculate_simple_interest(100, 0, 2) == 0.0
    
  def test_valueError(self):
    with pytest.raises(ValueError, match="Аргументы должны быть неотрицательными"):
      calculate_simple_interest(-100, 2, 2)
    with pytest.raises(ValueError, match="Аргументы должны быть неотрицательными"):
      calculate_simple_interest(100, -2, 2)
    with pytest.raises(ValueError, match="Аргументы должны быть неотрицательными"):
      calculate_simple_interest(100, 2, -2)

class TestCalculateCompoundInterest:
  def test_normal(self):
    assert calculate_compound_interest(1000, 10, 3, 1) == 1331
    assert calculate_compound_interest(1000, 10, 2, 2) == 1216
  
  def test_zero(self):
    assert calculate_compound_interest(1000, 0, 3, 1) == 1000
    assert calculate_compound_interest(1000, 10, 0, 1) == 1000
    with pytest.raises(ValueError, match="n должно быть положительным"):
      calculate_compound_interest(1000, 10, 3, 0)
    
  def test_valueError(self):
    with pytest.raises(ValueError, match="Аргументы должны быть неотрицательными"):
      calculate_compound_interest(-1000, 10, 3, 1)
    with pytest.raises(ValueError, match="Аргументы должны быть неотрицательными"):
      calculate_compound_interest(1000, -10, 3, 1)
    with pytest.raises(ValueError, match="Аргументы должны быть неотрицательными"):
      calculate_compound_interest(1000, 10, -3, 1)
      
class TestCalculateTax:
  def test_normal(self):
    assert calculate_tax(1000, 100) == 1000.0
    assert calculate_tax(5000, 50) == 2500.0
    assert calculate_tax(5000, 0.1) == 5.0
  
  def test_zero(self):
    assert calculate_tax(000, 100) == 0.0
    assert calculate_tax(1000, 0) == 0.0
    
  def test_valueError(self):
    with pytest.raises(ValueError, match="tax_rate должен быть в пределах 0-100"):
      calculate_tax(1000, -1)
    with pytest.raises(ValueError, match="tax_rate должен быть в пределах 0-100"):
      calculate_tax(1000, 512)
    with pytest.raises(ValueError, match="tax_rate должен быть в пределах 0-100"):
      calculate_tax(1000, 2**232)