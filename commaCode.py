#comma code
print("Enter values for list")
list = []
while True:
    value = input()
    if value == 'end':
        break
    else:   
        list.append(value)

#list = ["apple", "banana", "cherry"]

if len(list) == 0:
    print("List value available:", ", ".join(list))
else:
    print("List value available:", ", ".join(list[:-1]) + " and " + list[-1])