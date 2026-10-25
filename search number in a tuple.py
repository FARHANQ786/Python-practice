nums = (1,4,9,36,25,36,49,81,100)

x = 36

i = 0
while i < len(nums):
    if nums[i] == x:
        print("number found at index", i)
    i += 1