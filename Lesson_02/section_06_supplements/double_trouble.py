

try:
    'me' / 2
except Exception as e:
    raise ArithmeticError('poop') from e
