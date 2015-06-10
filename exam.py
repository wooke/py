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

def change(cost, paid):
    twenties = 0
    tens = 0
    fives = 0
    twos = 0
    ones = 0
    
    if cost/(paid-cost) < 1:
        print "Insufficient payment"
    else:
        twenties = (paid-cost)/20
        tens = (paid-cost-twenties*20)/10
        fives = (paid-cost-twenties*20-tens*10)/5
        twos = (paid-cost-twenties*20-tens*10-fives*5)/2
        ones = (paid-cost-twenties*20-tens*10-fives*5-twos*2)/1
        print 'Change is {} twenties, {} tens, {} fives, {} twos, and {} ones'.format(twenties, tens, fives, twos, ones)

def target_word(words, targetword):
    target = []
    wordlist = words.split()
    
    for x in range(len(wordlist)):
        if wordlist[x] == targetword:
            target.append(x)
    if target == []:
        return False
    else:
        return target

def make_index(words):
    table = {}
    target = []
    wordlist = words.split()
    for word in wordlist:
        target = target_word(words, word)
        table[word] = target
    return table

def alt_target(words, targetword):
    return make_index(words)[targetword]

sequence = 'we dont need no education we dont need no thought control we dont'

print "1) Quadratic solution for y = 1x^2 + 3x + 5"
quadratic(1,3,5)
print "\n2) Polynomial evaluation"
polynomial(2,[1,2,3])
print "\n3) Change procedure"
change(40, 78)
print "\n4a) Target word"
print target_word(sequence, 'dont')
print "\n4b) Target table"
print make_index(sequence)
print "\n4c) Alternate target word lookup"
print alt_target(sequence, 'dont')
