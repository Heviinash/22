# 1 is addition
# 2 is subtraction
# 3 is multiplication
# 4 is division

name=input(" Hello what is your name: ")
print(" Hello " +name )


print("This is a diy python calculator created by Heviinash Parugavelu" )
print(" I hope it help you to solve your problems in Mathematics questions " +name )

operation=int(input(" What operation do you one ? "))

num1=int(input(" What number will you like to put ? "))

num2=int(input(" What is the second number will you like to put? "))

if operation == 1 : 
    print( +num1 + num2 )
    print(" There you go this is your answer " +name )

elif operation == 2 :
    print( +num1 - +num2 )
    print(" There you go this is your answer " +name)    

elif operation == 3 :
    print(+num1 * +num2 ) 
    print(" There you go this is your answer " +name)    

elif operation == 4 :
     print( +num1 / +num2 )
     print(" There you go this is your answer " +name)    