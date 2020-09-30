def gcd(a,b):
    x = a
    y = b
    while(y!=0):
        r = x % y
        x = y
        y = r

    return x

def inverse_mod(inv, a):
    if (gcd(inv, a) == 1):
        x = 1
        while x < a:
            y = x * inv
            if (y % a == 1):
                return x
            x = x + 1

def cmt(a1,a2,a3,m1,m2,m3):
    mod = m1*m2*m3
    a_1 = (mod/m1) % m1
    a_2 = (mod/m2) % m2
    a_3 = (mod/m3) % m3

    inv1 = inverse_mod(a_1,m1)
    inv2 = inverse_mod(a_2,m2)
    inv3 = inverse_mod(a_3,m3)

    x1 = a1*(mod/ m1)*inv1
    x2 = a2 * (mod / m2) * inv2
    x3 = a3 * (mod / m3) * inv3
    sol = (x1 + x2 + x3) % mod
    return sol
