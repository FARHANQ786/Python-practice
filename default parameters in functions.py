def prod(a, b=2): # default parameter always at last
    return a * b # stores value in memory and returns it to the caller
    print(a * b)

print(prod( 3)) # 5*3 = 15
s=prod(5) # 5*2 = 10
print(s)
