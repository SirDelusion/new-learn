#s = {10, 20, [1, 2], "hello"}
s = {10, 20, "hello"}
print(type(s))#TypeError: unhashable type: 'list'
# because dict are not hashable and set are mutable but items must be hashable