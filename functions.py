import math

def integer(value):
    return int(value)

def is_prime(value):
    if value < 2:
        return False
    for i in range(2, math.isqrt(value) + 1):
        if value % i == 0:
            return False
    return True

def is_perfect(value):
    if value < 0:
        return False
    sqaure_root= math.sqrt(value)
    pefect_val = sqaure_root.is_integer()
    return pefect_val

def is_Armstrong(value):
    l = len(str(value))
    sum = 0
    
    if value < 0:
        return ""
    if  value > 0:
        for i in str(value):
            sum = sum + int(i)**int(l)

        if sum == value:
            return "Armstrong number"
        else:
            return ""
    
def is_Even_or_Odd(value):
    if value % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
def properties(value):
   if is_Armstrong(value) == "Armstrong number":
    property = [is_Armstrong(value),is_Even_or_Odd(value)]
    return property
   elif is_Armstrong(value) == "":
    property = [is_Even_or_Odd(value)]
    return property

def digit_sum(value):
    digit = abs(value)
    addition = 0
    for i in str(digit):
        addition += int(i)
    return addition 

