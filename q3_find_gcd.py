#greatest common divisor

def gcd(m,n):
    if m<n:
        i=m
    elif m>=n:
        i=n
    while i>0:
        if m%i==0 and n%i==0:
            break
        else:
            i-=1
    return i

def test_gcd():
    if gcd(24,16)==8 and gcd(255,25)==5:
        return True
    else:
        return False


