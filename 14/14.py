def Length_Collatz_sequence(start):
	if start == 1 :
		return 1
	if start % 2 == 0 :
		return 1 + Length_Collatz_sequence(start/2)
	else:
		return 1 + Length_Collatz_sequence(start*3+1)

i = 2
longest = 1
result = i
while i < 1000000:
	temp = Length_Collatz_sequence(i)
	if temp > longest:
		longest = temp
		result = i
	i += 1
print result