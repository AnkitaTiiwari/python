sentence = input("Enter a sentence: ")

word_list = sentence.split()
word_frequency = 0

for word in word_list:
    if word in word_list:
        word_frequency += 1
    else:
        word_frequency = 1

print(f"Word Frequency:{word_frequency}")

