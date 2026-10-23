# break keyword 
nums = (1,4,9,16,25,36,49,81,100)

x = 36

i = 0
while i < len(nums):
    if nums[i] == x:
        print("number found at index", i)
        break # comes out of the looop when the condition is satisfied
        
    else:
        print("number not found")
    i += 1
print("out of the loop")    



# continue - terminates the current execution and moves to next
# i = 1
# while i<=5:
#     if i == 3:
#         i += 1
#         continue # skips the current iteration and moves to next iteration
#     print(i)
#     i += 1 


# print odd numbers from 1 to 10 using continue continue
i = 1
while i<=10:
    if i%2 == 0:
        i += 1
        continue
    print(i)
    i += 1


