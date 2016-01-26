#sum series

def m_series(i):
    #initialize variables
    result=0
    #perform calculation
    for n in range(1,i+1):
        result += (n/(n+1))
    #output result
    return result

def test():
    print("i         m(i)")
    for i in range(1,21):
        print("{0:<10}{1:.4f}".format(i,m_series(i)))

print(test())
