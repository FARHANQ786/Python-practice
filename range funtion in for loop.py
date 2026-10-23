# for i in range(10): # only the stop value is mandatory , by default start value is 0 and step value is 1
#     print(i) # 0,1,2,3,4,5,6,7,8,9

# for i in range(1,10): # start and stop value
#     print(i) # 1,2,3,4,5,6,7,8,9

# for i in range(1,10,2): # start, stop and step value
#     print(i) # 1,3,5,7,9


for i in range(102):
    if i-1 == -1:
        continue
    print(i-1)
        