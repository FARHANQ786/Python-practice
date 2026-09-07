num1=int(input("enter the 1 number " ))
num2=int(input("enter the 2 number " ))
num3=int(input("enter the 3 number " ))
if(num1>=num2 and num1>=num3):
    print("first number is greater than second and third number")
elif(num2>=num1 and num2>=num3):
    print("second number is greater than first and third number")
else:
    print("third number is greater than first and second number")        


