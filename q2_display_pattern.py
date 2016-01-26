#display pattern

def display_pattern(n):
    for i in range(1, n+1):
        row = ""
        for j in range(i):
            row += str(i-j)+" "
        if n >= 10:
            space = 3*n-9
        else:
            space = 2*n
        print("{0:>{1}}".format(row,space))

