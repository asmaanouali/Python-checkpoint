#Question 7 program
from math import sqrt
H=30
C=50
str=input('give a comma-separated sequence: ')
l=str.split(',')
for i in range(len(l)):
    l[i]=int(sqrt((2 * C * int(l[i]))//H))
for i in l:
    if i==l[-1]:
        print(i,end="")
    else:
        print(i,end=",")
