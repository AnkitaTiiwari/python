
def collatz(number):
    result = 0
    try:
        if number%2 ==0 :
            #means number is even
            result = number//2
            return result
        else:
            result = 3*number +1
            return result    

    except:
        print("Ran into issue")  

result = 0
print("Enter the number you wanna pass")
number = int(input())

if number < 1:
    print("Please enter a number greater than 0")

while True:
    result = collatz(number)   
    print(result)
    if result > 1: 
        number = result
    else:
        break       