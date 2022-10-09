def sum_it(a, b):
    return a + b

def minus_it(a, b):
    return a - b

def mult(a, b):
   return a * b

def div(x, y):
    try:
        return x/y
    except ZeroDivisionError:
        return "You can't divide by zero"

