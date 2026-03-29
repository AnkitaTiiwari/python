#ArithmeticAdditionandDivision.py

num1 = int(input("Enter first number to be Added : "))
num2 = int(input("Enter second number to be Added : "))
sum = num1 + num2
print(f'The sum of {num1} and {num2} is {sum}')

dividend = int(input("Enter dividend : "))
divisor = int(input("Enter divisor : "))

if divisor == 0:
    print('divisor is zero, would create divide by zero error')
else:
    result = dividend / divisor    
    print(f"reslt is {result}")