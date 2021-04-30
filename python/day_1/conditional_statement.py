# if else statement 
num = 10
if num > 100 :
    print("Greater")
else :
    print("Smaller")

    
# multiple if else statement
num = 100
if(num > 100) :
    print("Greater than 100")
elif(num <= 100 and num >= 50) :
    print("Within 50 to 100")
else :
    print("Less than 50")

    
# multilevel if else statement
num = 19

if((num % 3 == 0) and (num % 5 == 0)):
    print("Div by 3 and 5")
else:
    if(num % 3 == 0):
        print("Div by 3")
    elif(num % 5 == 0):
        print("Div by 5")
    else:
        print("Not div by 3 and 5")