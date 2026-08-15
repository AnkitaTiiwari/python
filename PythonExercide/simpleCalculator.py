#simple calculator

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a+b 

print('Select the operation. \n1. Add \n2.Subtract \n3.Multiply \n4.Division')

while True:
    try:
        choice = int(input("Enter choice(1/2/3/4): "))

        if choice in (1,2,3,4):
            #do operation
            num1 = float(input("Enter first number : "))
            num2 = float(input("Enter second number : "))

            if choice == 1:
                result = add(num1,num2)
            elif choice == 2:
                result = subtract(num1,num2)
            elif choice == 3:
                result = multiply(num1,num2)
            elif choice == 4:
                result = divide(num1,num2)
            else:                        
                print("Invalid input")
            
            print("Result: ", result)
            print("Do you want to perform another calculation? (yes/no)")
            again = input().strip().lower()
            if again != 'yes':
                break

        else:
            print("Please enter correct choice")    

    except:
        print("Exception")    