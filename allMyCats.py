#collecting cats name
import sys
cats = [];
while True:
    print("Enter cat " + str(len(cats)+1) + " names or type exit to exit!")
    name = input()
    if name == 'exit':
        break
    else:    
        cats = cats + [name]

print("The cat names are:") 
for cat in cats:
    print(cat)
