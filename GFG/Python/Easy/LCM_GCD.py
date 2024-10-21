def lcmAndGcd(A, B):
    # code here
    a = A
    b = B

    while a > 0 and b > 0:
        if a > b:
            a = a % b
        else:
            b = b % a

    gcd = a if a > 0 else b

    lcm = abs(A*B)/gcd

    return int(lcm), gcd
