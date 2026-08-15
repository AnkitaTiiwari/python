# Factorial using recursion

def factorial(n):
    if n == 1:
        return 1
    else:
        fact = n * factorial(n-1)
        return fact


number = int(input("Enter a number : "))

if number <= 0:
    print("Please enter a positive number")
else:
    result = factorial(number)    
    print(f"The factorial of {number} is {result}")