num1 = "15"
num2 = "8"

end_num1 = len(num1) 
end_num2 = len(num2) 

tmp =0
carry=0
result = "";



while (end_num1 !=0) and (end_num2 != 0) :

	if	int(num1[end_num1 -1]) + int(num2[end_num2 -1])+carry < 10:
		tmp = int(num1[end_num1 -1]) + int(num2[end_num2-1]) + carry
		result = str(tmp) + result
		carry =0
		tmp =0
		
		
		end_num1 -=1
		end_num2 -=1
	else :
		tmp = int(num1[end_num1 -1]) + int(num2[end_num2 -1]) + carry - 10
		result = str(tmp) + result
		carry = 1
		tmp =0
		
	
		end_num1 -=1
		end_num2 -=1

print result	
print end_num1
print end_num2	