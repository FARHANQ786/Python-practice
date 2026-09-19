# set of unordered items , each elelment must be unique and immutable
# set - {         } set is mutable
col = {2,2,3,4,3,2,2,4,6,7,5,"world",4,8,9,0}
print(col)
print(len(col)) # count 1 time does not include duplicate

# empty set 
collection= set() # syntax of empty set
print(type(collection))

# methods of set 
collection.add(1)
collection.add(2)
collection.add(3)
collection.add(5)
collection.add(44)
collection.add("rockstar")


# collection.remove(44) # removes spedific item
# print(collection)

print(collection)

print(collection.pop()) # removes random value
print(collection.pop())


collection.clear()# empties set
print(collection)


set1={1,2,3}
set2={2,3,4}

print(set1.union(set2)) # {1,2,3,4}
print(set1.intersection(set2)) #{2,3}