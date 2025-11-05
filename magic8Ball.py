#magic 8 ball

import random

while True:

    if input("Ask me a question: or press q to exit") == "q":
        break
    else:
        messages = [
            "It is certain",
            "It is decidedly so",
            "Without a doubt",
            "Yes - definitely",
            "You may rely on it",
            "As I see it, yes",
            "Most likely",
            "Outlook good",
            "Yes"]

        number = random.randint(0,len(messages)-1)
        print(messages[number])