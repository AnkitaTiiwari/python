import pyinputplus as pyip

# num =  pyip.inputNum(prompt= "Input a number : ")
# print(num)

# num = pyip.inputNum(prompt="Enter a number between 2-8 : ",min=2,max=8)
# print(num)

# num = pyip.inputNum(prompt="Enter a number between 2-8 : ",lessThan=8,greaterThan=2,limit=2)
# print(num)

# num = pyip.inputNum(prompt="Enter a number between 2-8 : ",lessThan=8,greaterThan=2,limit=2,timeout=5)
# print(num)


num = pyip.inputNum(prompt="Enter a number between 2-8 : ",lessThan=8,greaterThan=2,limit=2,timeout=5,default=5)
print(num)
