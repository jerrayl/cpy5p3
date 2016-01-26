#determine prime

def is_prime(n):
    # 1, 0 and negative numbers are not prime
    if n < 2:
        return False
    # 2 is the only even prime number
    elif n == 2: 
        return True    
    # all other even numbers are not primes
    elif n%2==0: 
        return False
    # for all odd numbers
    for x in range(3, int(n**0.5+1), 2):
        if n % x == 0:
            return False
    return True


def test():
    n=0
    r=0
    for i in range(1,999999):
        if is_prime(i):
            if i<10:
                print ("   ",end="")
            elif i<100:
                print ("  ",end="")
            elif i<1000:
                print (" ",end="")
            print (i," ",end="")
            n+=1
            r+=1
        if r==10:
            print("\n")
            r=0
        if n==1000:
            break




    
