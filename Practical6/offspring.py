paternal_age=[30,35,40,45,50,55,60,65,70,75]
chd=[1.03,1.07,1.11,1.17,1.23,1.32,1.42,1.55,1.72,1.94]
dir = {}
for i in range(len(paternal_age)):
    dir[paternal_age[i]] = chd[i]
print("The relative risks for congenital heart disease (CHD) in the offspring of older fathers of different ages are ",dir)

#For a 55-year-old father, the risk of CHD for the offspring can be printed as follows: 
age = 55
print("The risk of CHD for the offspring of a father aged",age,"is",dir[int(age)])

import numpy as np
import matplotlib.pyplot as plt
N = 10
x = (30,35,40,45,50,55,60,65,70,75)
y = (1.03,1.07,1.11,1.17,1.23,1.32,1.42,1.55,1.72,1.94)
plt.ylabel('congenital heart disease in the offspring')
plt.xlabel('paternal age')
plt.title('Parental age vs offspring health')
plt.scatter(x,y,marker= 'o')
plt.show()

