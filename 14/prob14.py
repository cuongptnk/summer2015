import time
 


def collatz(n):
	count =1
	while n > 1:
		count +=1
		if n%2 == 0:
			n = n/2
		else:
			n = 3*n +1
	return count

	
def largest_collatz(s,e):
	largest = 1
	result = 1
	while s != e:
		tmp =collatz(e)
		



s = 1
e = 1000000
largest = 1
result = 1
while s < e:
	tmp = collatz(s)
	if tmp > largest:
		largest = tmp
		result = s
	s +=1
print result