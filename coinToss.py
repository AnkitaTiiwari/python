#coin toss game
import random
print("Welcome to the Coin Toss Game!")
list = []

for i in range(100):
    if random.randint(0,1) == 0:
        list.append("H")

    else:
        list.append("T")  

print(list)        

for i in range(len(list)-1):
    for j in range(len(list[:i+5])):
        print(list[j:i+5])
        i = i+ 1
        j = j + 1
