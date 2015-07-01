num1 = "15"
num2 = "8"

end_num1 = len(num1) - 1
end_num2 = len(num2) - 1

tmp =0
carry=0
result = "";



while (end_num1 !=0) or (end_num2 != 0) :
	if end_num1 == 0:
		while end_num2 != 0 :
			result = num2[end_num2] + result
			end_num2 -=1
	elif end_num2 == 0 :
		while end_num1 != 0 :
			result = num1[end_num1] + result
			end_num1 -=1
	else :
		if	int(num1[end_num1]) + int(num2[end_num2])+carry < 10:
			tmp = int(num1[end_num1 ]) + int(num2[end_num2]) + carry
			result = str(tmp) + result
			carry =0
			tmp =0
			
			
			end_num1 -=1
			end_num2 -=1
		else :
			tmp = int(num1[end_num1 ]) + int(num2[end_num2 ]) + carry - 10
			result = str(tmp) + result
			carry = 1
			tmp =0
			
		
			end_num1 -=1
			end_num2 -=1

print result	
print end_num1
print end_num2	