def fac(n):
    if n == 0 or n == 1:
        return 1
    else:
        fact = 1
        i = 1
        while i <= n:
            fact *= i
            i += 1  
        return fact    

s=fac(1)
print(s)
