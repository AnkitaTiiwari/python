#exploring list data type

spam = ["cat", "dog", "bat"]

print(spam.index("dog"))  # returns 1

spam.append("moose")
print(spam)  

spam.insert(2,'chicken')
print(spam)

spam.remove("cat")
print(spam)


#spam.remove("elephant")  
#print(spam)

spam.reverse()
print(spam)

spam.sort()
print(spam)

spam.append("Ankita")
spam.append("Kimi")

spam.append("kimi")

spam.sort()
print(spam)

spam.sort(key=str.upper)
print(spam)