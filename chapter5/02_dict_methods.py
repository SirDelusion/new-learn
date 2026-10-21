marks = {"Lucky":100,
         "deep": 50,
         "rohan":55,
        }

# print(marks.items())
# print(marks.keys())
# # print(marks.values())
# marks.update({"Lucky":99,"dax":90}) #this is possible because dict are mutable
# print(marks)
# print(marks.get("Lucky2"))#this will print none because it cant get that 
# print(marks["Lucky2"])#this will give us a error because theres no Lucky2 key in the dict
# marks.clear()
# print(marks)
# new_marks= marks.copy()
# print(new_marks)
# j,o = marks.popitem() #this return the last pair lifo
# print(j,o)
k = marks.pop("Lucky")
print(k)