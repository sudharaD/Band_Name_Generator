a = input("a: ")
b = input("b: ")
print(type(a))
temporaryB = b
b = a
a = temporaryB

print("a = " + a)
print("b = " + b)