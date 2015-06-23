import time
def num_divisor(n):
	count =0
	i=1
	while i*i < n:
		if n % i ==0:
			count +=2
		i +=1
	if i*i == n:
		count +=1
	return count
	
sum = 1
num = 1	
start = time.time()
while num_divisor(sum) <= 500:
	num +=1
	sum +=num

e = time.time() -start
print e, " ", sum