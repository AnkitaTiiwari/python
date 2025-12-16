#we are writing custom input code
import pyinputplus as pyip

def custom_function(numbers):
    num_list = list(numbers)
    sum = 0
    for n in num_list:
        sum += int(n)

    if sum == 10:
        return num_list
    else:
        raise ValueError("The numbers must add up to 10.")

#print("This is a custom input file")
num = pyip.inputCustom(custom_function)
print("You entered the numbers:", num)