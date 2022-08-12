#Question 1 program
result_list=[]
for i in range(2000,3201): #since 3200 is also included
    if (i%7==0) and (i%5!=0):
        result_list.append(i)
print("Numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 :",result_list)
    
