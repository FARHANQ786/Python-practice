# str="this is aprogram on string \nwe are doing it on python"
# print(str)
# rts="this is rockstar \twe are doing it on python"
# print(rts)
# concatenation
# print("hello"+"world")
# str="dsdddfsdsdsf"+"    " # empyt spaces also be counted in length of string
# print(len(str))

# indexing - means positioning

#rockstar
#01234567
#-5-4-3-2-1

# str="this is rockstar"
# print(str[0]) # first character of string
# print(str[1]) # second character of string
# print(str[-1]) # last character of string
# print(str[-2]) # second last character of string

#  slicing - means taking a part of string
# str = "this is rockstar"
# #str[starting index : ending index] # ending index is not included
# print(str[0:4]) # this
# print(str[5:10]) # is r
# print(str[11:16]) # rockstar 
# print(str[8:len(str)]) # rockstar  
# print(str[8:]) # rockstar [8:len(str)]
# print(str[:8]) # this is [0:8]
# print(str[-1:-3]) # empty string as -1 is greater than -3
# print(str[-3:-1]) # ta


# string functions
str = "i am studying from apna collge"
print(str.endswith("collge")) # True 
print(str.endswith("am")) # false  


print(str.capitalize()) # I am studying from apna collge
str=str.capitalize()
print(str)


print(str.replace("from","not")) # i am studying not apna collge


print(str.find("am")) # 2

print(str.count("a")) # 1