# Fibonacci Series

limit = int(input("Enter the top limit : "))

start = 0
next_num = 1
sum = 0

if limit <= 0:
    print("Please enter a positive number")
else:    
    for i in range(limit + 1):
        sum = start + next_num
        print(start)
        start = next_num
        next_num = sum