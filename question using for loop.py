# print elements of a list using for loop
list = [1,4,9,16,25,36,49,82,36,100]
# for i in list:
#     print(i)


x=36

idx = 0
for i in list:
    if x == i:
        print("number found at index", idx)   
    idx += 1