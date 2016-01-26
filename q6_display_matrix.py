#display matrix
from random import randint

def print_matrix(n):
    for i in range(n):
        for j in range(n):
            print(randint(0,1),end=" ")
        print("\n")

