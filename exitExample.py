import sys

while True:
    text = input("Type exit to exit")
    if text == "exit":
        sys.exit()
    print("You typed ", text)