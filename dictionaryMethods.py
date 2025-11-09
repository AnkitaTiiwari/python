
dict = {"kimi":"smart","sunny":"lazy"}
# for i in dict.keys():
#     print(i)

# for i in dict.values():
#     print(i)

# for i in dict.items():
#      print(i)

print('kimi' in dict.keys())

print('kimi' in dict.values())

print('kimi' in dict.items())

print('kimi' in dict)
#get()
print(dict.get('kimi'))

print('She/he has the quality ' + dict.get('kimi',0))
