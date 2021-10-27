# Mathematics

def POW(A, B):
    return A ** B

def SQRT(A):
    return A**(1/float(2))

def CBRT(A):
    return A**(1/float(3))

def Multiply(A, B):
    return A * B

def Divide(A, B):
    return A / B

def Plus(A, B):
    return A + B

def Minus(A, B):
    return A - B

def Fib(Number):
    A = 0
    B = 1
    while A < Number:
        print(A, end=' ')
        A, B = B, A + B
    print()

def Percent(Total, Calc):
    return (Total/100) * Calc
