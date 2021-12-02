########################################
#Author:    Gabriel Kiprono
#           CSC 4585-001
#           workshop1.py
#           August 27 2021
########################################

from z3 import *

def buggyFunc(floatVar, intVar):
    res = []
    tempVar = int(floatVar)
    if(tempVar == 3*intVar):
        if(intVar > tempVar-50):
            print(res[5])


def concolicTesting():
    x=Int('x')
    y=Int('y')
    solve(x==3*y, y-x>-50)



if __name__ == "__main__":
    #buggyFunc(3,1)
    concolicTesting()