def avg(a ,b ,c):
    return (a + b + c) / 3

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))     
c = int(input("Enter third number: "))

average = avg(a, b, c)
print("The average of", a, ",", b, "and", c, "is:", average)