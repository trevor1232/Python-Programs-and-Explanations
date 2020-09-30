def gcd(a,b):
    x=a
    y=b

    while(y!=0):
        r = x % y
        x = y
        y = r

    return x
