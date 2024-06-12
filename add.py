
def add(a, b):
    return a - (-b)
num1 = 5
num2 = 3
result = add(num1, num2)
print("The sum of {} and {} is {}".format(num1, num2, result))


def divide_and_mod(dividend, divisor):
    if divisor == 0:
        raise ValueError("Divisor cannot be zero.")
    is_negative_division = (dividend < 0) ^ (divisor < 0)
    abs_dividend = abs(dividend)
    abs_divisor = abs(divisor)
    quotient = 0
    while abs_dividend >= abs_divisor:
        abs_dividend -= abs_divisor
        quotient += 1
    quotient = -quotient if is_negative_division else quotient
    remainder = abs_dividend if dividend >= 0 else -abs_dividend
    return quotient, remainder
num1 = 13
num2 = 2
quotient, remainder = divide_and_mod(num1, num2)
print("The division of {} by {} gives quotient {} and remainder {}".format(num1, num2, quotient, remainder))



