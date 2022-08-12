#Question 4 program
def missing_char(string,index):
    #the function code
    p=list(string)
    del p[index]
    return ''.join(p)

#the main code
string=input('give non-empty a string: ')
while string=='':
    string=input('try again : ')
index=int(input('give an index: '))
while (index>=len(string)) or (index<0):
    index=int(input('try again : '))
print('→ ',missing_char(string,index))
