import pprint

sentence = 'Hey Its me. I\'m the problem'

count = {}

for c in sentence:
    count.setdefault(c, 0)
    count[c] += 1

pprint.pprint(count)    

print("----")

pprint.pformat(count)    