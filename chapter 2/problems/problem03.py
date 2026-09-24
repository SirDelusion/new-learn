# a = eval(input("Enter your input:"))
# b = type(a)
# print(b)
import ast

def smart_input(prompt=""):
    raw = input(prompt)
    try:
        return ast.literal_eval(raw)
    except (ValueError, SyntaxError):
        # If it's a plain word (like "hello" without quotes), treat it as a string
        return raw
    
val = smart_input("Enter something: ")
print("Value:", val)
print("Type:", type(val)) 