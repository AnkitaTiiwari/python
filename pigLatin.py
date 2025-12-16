#some made up launguage rules
#words that start with a vowel add "ay" to the end
#words that start with a consonant, move the first letter to the end and add "ay"

vowels = ('a','e','i','o','u')
text = input("Enter a sentence to convert to Pig Latin: ")


def _pig_latin_word(word):
    words = text.split(' ')
    pigLatinSentence = ''
    for i in range(len(words)):
    #print(words[i])
        if words[i]=='':
            continue
        elif words[i].isnumeric():
            pigLatinSentence += words[i] + ' '
        elif words[i].startswith(vowels):
            words[i] = words[i] + 'ay'
            pigLatinSentence += words[i] + ' '
        else:
            words[i] = words[i][1:] + 'ay' + words[i][0]
            pigLatinSentence += words[i] + ' '
    return pigLatinSentence

pigLatinSentence = _pig_latin_word(text)
print(pigLatinSentence)
