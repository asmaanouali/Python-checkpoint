#Question 6 program
import numpy as np
original_array1=np.array([0,1,2])
original_array2=np.array([2,1,0])
result=np.cov(original_array1,original_array2)
print(result)
