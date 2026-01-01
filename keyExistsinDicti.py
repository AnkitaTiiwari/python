Fruits = {'a': "Apple", 'b':"Banana", 'c':"Carrot"}
key_to_lookup = 'a'
# if Fruits.get(key_to_lookup):
#     print(f"Key '{key_to_lookup}' exists in the dictionary with value: {Fruits[key_to_lookup]}")
# else:
#     print(f"Key '{key_to_lookup}' does not exist in the dictionary.")

# if key_to_lookup in Fruits:
#     print(f"Key '{key_to_lookup}' exists in the dictionary with value: {Fruits[key_to_lookup]}")
# else:
#      print(f"Key '{key_to_lookup}' does not exist in the dictionary.")

print(sorted(Fruits))
print(sorted(Fruits.items()))

print(sorted(Fruits.keys()))
print(sorted(Fruits.values(),reverse=True))
