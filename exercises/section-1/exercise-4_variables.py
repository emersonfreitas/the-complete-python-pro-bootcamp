"""
Write a program that switches the values stored in the variables a and b.
"""
a = input("a: ")
b = input("b: ")

aux = b 
b = a
a = aux

print("a: " + a)
print("b: " + b)
