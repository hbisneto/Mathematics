# Mathematics

def POW(a, b):
    return a ** b

def SQRT(a):
    return a**(1/float(2))

def CBRT(a):
    return a**(1/float(3))

def Multiply(a, b):
    return a * b

def Divide(a, b):
    return a / b

def Plus(a, b):
    return a + b

def Minus(a, b):
    return a - b

def Fib(number):
    a = 0
    b = 1
    while a < number:
        print(a, end=' ')
        a, b = b, a + b

def Percent(total, calc):
    return (total/100) * calc

def baskara(a, b, c, suppress_warn = True):
    """The delta (Δ) in Bhaskara's formula is the discriminant of the quadratic equation, and it's calculated as Δ = b² - 4ac.
    The value of delta can tell us about the roots of the equation:

    - If Δ > 0, the equation has two distinct real roots.
    - If Δ = 0, the equation has one real root.
    - If Δ < 0, the equation does not have any real roots.

    So, if the delta in Bhaskara's formula returns a value less than zero (negative), it means that the quadratic equation does not have any real roots. In other words, there are no real numbers that you can substitute for x in the equation ax² + bx + c = 0 that will make it true. 
    However, it's important to note that while there are no real roots, there could be complex roots. Complex roots involve imaginary numbers, which are based on the square root of negative one.
    But that's a topic for another discussion! 😊
    """
    delta = ((b**2) -4*a*c)
    if delta < 0:
        if suppress_warn == False:
            print("=" *80)
            print("The equation does not have any real roots")
            print("=" *80)
    sqrt = delta**(1/float(2))
    x = (-b + (sqrt)) / (2 * a)
    x2 = (-b - (sqrt)) / (2 * a)
    y = [delta, x, x2]
    return y

def arithmetic_progression(a, b, c):
    """a: The position you want to find
    b: The first number of the index
    c: The interval between numbers in the list
    """
    calc = b + (a - 1) * c
    return calc
