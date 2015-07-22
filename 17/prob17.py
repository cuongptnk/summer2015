import string

def translate(number):
    digits = ('zero','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen')
               
    tens = ('twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety')         

    if 0 <= number <= 19:
        return digits[number]
        
    elif 20 <= number <= 99:
        if number % 10:
            return tens[(number / 10) - 2] + " " + translate(number % 10)
        else:
            return tens[(number / 10) - 2]
            
    elif 100 <= number <= 999:
        if number % 100:
            return digits[number / 100] + " hundred and " + translate(number % 100)
        else:
            return digits[number / 100] + " hundred"
            
    elif number == 1000:
        return digits[1] + " thousand"         



def countLetters(word):
    numberLetter = 0
    
    for i in word:
        if i in string.lowercase + string.uppercase:
            numberLetter += 1
            
    return numberLetter
   
total = 0

for i in range(1, 1001):
    total += countLetters(translate(i))
    
print total