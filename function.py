# function defining
# def sum(a, b):# a and b are parameters , parameter are optional
#     return a + b # no output returning is also optional


# sum_result = sum(5, 10) # 5 and 10 are arguments
# print("The sum is:", sum_result)    # sum is 15

def print_hello():
    print("Hello ") # displays Hello but does not return anything

s=print_hello()
print(s) # None becuase function is not returning anything , it is just printing something

def print_hello():
    return "Hello " # stores Hello in memory and returns it to the caller

s = print_hello()
print(s) # This will print "Hello " since the function now returns a value.