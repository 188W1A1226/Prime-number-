import math
n=int(input())
c=0
for i in range(0,int(math.sqrt(n)+1):
	if(n%i==0):
		c=1
		break
if(c==1):
	print("not prime")
else:
	print("prime")
