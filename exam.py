from math import *

def quadratic(a,b,c):
    root = b^2 - 4*a*c

    x1 = 0
    x2 = 0
    
    if root >= 0:
        x1 = (-(b)+sqrt(root))/(2*a)
        x2 = (-(b)-sqrt(root))/(2*a)
        print (x1, x2)
    else:
        print 'Root 1 = {}+{}i'.format(-b/(2*a), sqrt(-root)/(2*a))
        print 'Root 2 = {}-{}i'.format(-b/(2*a), sqrt(-root)/(2*a))

def polynomial(num, coef):
    sum = 0
    iteration = 1
    for x in coef:
        sum += x*num^(len(coef)-iteration)
        iteration += 1
    print sum

quadratic(1,3,5)
polynomial(2,[1,2,3])
