# # key: value pairs      dictionaries are mutable
# dict = {
#     "key":9,
#     "subjects":["oython","rockstar,9"],
#     12.99:3.43
# }
# print(dict)

# print(type(dict))

# # to access info
# print(dict["key"])

# # to change something or add new field

# dict["key"]=32

# dict["name"]="farhan" # to add new field
# print(dict)

# # null dictionary
# docs={}
# docs["name"]=23
# print(docs)

# # nested dictionary
# student = {
#     "name": "farhan",
#     "subjects" : {
#         "maths":23,
#         "science":43,
#         "evs":21
#     } 
# }
# print(student)
# print(student["subjects"])
# print(student["subjects"]["maths"])

# methods in dictionries
student = {
    "name": "farhan",
     "subjects" : {
         "maths":23,
         "science":43,
         "evs":21
     } 
 }

print(student.keys())
print(list(student.keys())) # type casting
print(len(list(student.keys())))

print(student.values())
print(len(list(student.values())))



print(student.items())

pairs=list(student.items())
print(pairs[0])


student.get("name")



# to update dictionary
student.update({"name":"rock"})
print(student)

newdict = {"city" : "delhi"}
student.update(newdict)
print(student)





 

