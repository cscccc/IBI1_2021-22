
#The given number of cuts at the begining is 0
n=0
p=1
#The pizza should be cut for an increasing number of straight cuts until 64 pieces are created
while p < 64:
#Use the equation to calculate the number of pieces p that can be created
	p=(n*n+n+2)/2
	print("Cut ",n,", at most ",int(p)," pizza slides")
#Add 1 to i and continue to calculate the number of pieces created later 
	n=n+1
#When the pieces are enough, stop the calculation
	if p >=64:
		break 
