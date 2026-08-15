#natural logarithm
import math

number = float(input("ENter a number : "))

if number <= 0 :
    print("Please enter a positive number")
else:    
    print(math.log(number))
