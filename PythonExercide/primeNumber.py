#check if a number is prime or not

num = int(input("Enter a number : "))

flag = False

if num == 1:
    print(f'{num} is not a prime number')
elif num > 1:
    for i in range(2,num):
        if num % i == 0:
            flag = True



if flag:
    print(f"{num} Not a prime number")
else:
    print(f'{num} is a prime number')