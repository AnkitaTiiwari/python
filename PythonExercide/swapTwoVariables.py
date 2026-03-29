#swapping variables

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

temp = a
a = b
b = temp

print(f"After swapping: {a}, {b}")