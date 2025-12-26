import random

head = 0
tells = 0

for i in range(1, 1001):
    
    rand = random.randint(0,1)
    if rand == 0:
        head = head + 1
    else:
        tells = tells + 1

    if i == 500:
        print(f'Already reached halfway. Heads are {head} tells are {tells}')



