#Grocery Price Calculator

grocery_list = {
"apple":1,
"potato":2,
"tomaten":2,
"onion":2,
"milk":2
}

cart = []

print("Available grocery items:",", ".join(grocery_list.keys()))

while True:
    item = input("enter:")

    if item == "no" : 
        break
    elif item in grocery_list:
        cart.append(item)
        print("anytihing else?")
    else:
        print("item is not available")

for item in cart:
    print("Added ", item, " to cart")

total = sum(grocery_list[item] for item in cart)
if total > 5:
        total = total - total * 0.05

print(f"Your total is: {total} ")

# total = 0

# for item in cart:
#     total = total + grocery_list[item]
#     if total < 5:
#         total = total - total * 0.05

# print("Total cost: ", total)   