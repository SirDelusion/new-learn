friends = ["Apple","Grapes",8,8.2,"lucky"]
print(friends[0])
friends.append("Lkkkk")
print(friends)


l1 = [1,5,9,8,27,8,66,977,5,553,2]
# l1.sort() # this sorts the list 
# l1.reverse()  this reverses the list
# l1.insert(3,66) this adds the number at a given place (position,the value)
# l1.pop(4) #this delete a variable given at the given index
# l1.remove(5)  this removes a specific thing from the list 
# unique = list(set(l1)) this is to remove duplicates
# now we ssee how to do it use conversion to dict
# unique = list(dict.fromkeys(l1)) 
numbers = []
for item in l1:
    if item not in numbers:
        numbers.append(item)
print(numbers)