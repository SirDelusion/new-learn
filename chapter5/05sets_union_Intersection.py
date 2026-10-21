s1 = {1,5,3,6,8,11,556,330}
s3 = {1,5,3}
s4 = {77777,88888,999999,5555}
s2 = {2,8,9,66,9,887,552,3,5,8}

print(s1.union(s2)) #combined
print(s1.intersection(s2)) # common values 
print(s2.difference(s1)) # this gives the item only present in the earlier mentioned set not common ones
print(s1.symmetric_difference(s2)) #Returns elements in either set, but not both
print(s3.issubset(s1)) #ki chote veer ji part ne family de 
print(s3.issuperset(s1))# ki family chote veer ji di h

print(s4.isdisjoint(s3)) #Checks whether two sets have no common elements