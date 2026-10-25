marks = {"Lucky":100,
         "deep": 50,
         "rohan":55,
        }

# print(marks.items())
# print(marks.keys())
# # print(marks.values())
# marks.update({"Lucky":99,"dax":90}) #this is possible because dict are mutable
# print(marks)
# print(marks.get("Lucky2"))#this will print none because it cant get that  because data is missing ,when the key might optionally be missing, or when you want to provide a fallback value:
# print(marks["Lucky2"])#this will give us a error because theres no Lucky2 key in the dict,when the key is expected to always be present, and missing it indicates a genuine bug or error in your code.
# marks.clear()
# print(marks)
# new_marks= marks.copy()
# print(new_marks)
# j,o = marks.popitem() #this return the last pair lifo
# print(j,o)
k = marks.pop("Lucky")
print(k)