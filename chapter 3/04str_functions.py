name = "lakshit"

print(len(name))
print(name.endswith("it"))
print(name.startswith("La"))
print(name.capitalize())


a = "Lakshit is a really good swimmer"

print(a.find("good"))
print(a.replace("good","best"))
# print(a.strip("really")) why this didnt work is because the string are immutable we use..
print(a.replace("really"," "))