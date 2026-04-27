def calculate_simple_interest(principal:float, rate:float, time:float):
  if principal < 0 or rate < 0 or time < 0:
    raise ValueError("Аргументы должны быть неотрицательными")
  return principal * rate * time / 100

def calculate_compound_interest(principal:float, rate:float, time:float, n):
  if not isinstance(n, int) or n <= 0:
    raise ValueError("n должно быть положительным")
  if principal < 0 or rate < 0 or time < 0:
    raise ValueError("Аргументы должны быть неотрицательными")
  return int(round(principal * (1 + rate/(100*n))**(n*time)))

def calculate_tax(amount, tax_rate):
  if not (0 <= tax_rate <= 100):
    raise ValueError('tax_rate должен быть в пределах 0-100')
  if amount < 0:
    raise ValueError('Amount не может быть меньше 0')
  return amount * tax_rate / 100