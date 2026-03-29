#print prime numbers

num = int(input("Enter a number : "))

prime_list = []

for i in range(1,num+1):
        if num % i == 0:
            break
        else:    
            prime_list.append(i)

print(f"Prime numbers between 1 and {num} are: {prime_list}")