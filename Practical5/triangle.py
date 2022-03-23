#The number of dots in the first triangle is 1
a=1
#Use i to represent the serial number of a triangle
i=1
#We need to calculate the numbers of the dots in the first 10 triangles
for i in range(1,11) :
#Each time add a value that equals to the value of i+1 to a, we can get the number of dots in the next triangle
	print(a)
	a=a+i+1
#Add 1 to i and continue on the calculation of the next triangle
	i=i+1
