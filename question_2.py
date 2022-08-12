#Question 2 program
#programme itératif
def facto_iteratif(n):
    fact=1
    for i in range(1,n):
       fact=fact*n
       n-=1
    return fact

#programme récursif
def facto_recursif(n):
    if n==1 or n==0:
        return 1
    else:
        return n*facto_recursif(n-1)

n=int(input('n= '))
print("itér : n! =",facto_iteratif(n)) 
print("récur : n! =",facto_recursif(n)) 
