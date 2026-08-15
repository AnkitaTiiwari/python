#sum of natural numbers

limit = int(input("Enter the top limit : "))

sum = 0

for i in range(1,limit+1):
    sum += i

print(f'Sum of natural number till {limit} is {sum}')    