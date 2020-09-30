def divAlg(a,b):
    if (a > b):
        q = 0
        while(True):
            r = a - b * q
            if (b * (q + 1) > a):
                return [q,r]
            else:
                q = q + 1
    else:
        return None
