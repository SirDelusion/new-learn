# c = (1,5,6,99,8,5,8,'5',5.2) 
# print(c.count(5))
# print(c.index(99))

m = (1,2,3,5,3,6,3,6,3)
n = (8,9,8,9)
p = m + n  # to concatenate to tuples to join the tuples 
print(p)

rep_of_n = n * 3 #when you want to get the tuple repeated
print(rep_of_n)

print(8 in n) # called membership if its in the tuple or not 
print(10 in n)

print(len(n)) # use to calculate the length of the tuple

print(min(n)) #to get min value in tuple
print(max(n))

print(n[1:3]) # this is called slicing in tuple first number is always included and end is not included
a,b,c,d = n
print(a,b,c,d) # this is called unpacking of the tuple