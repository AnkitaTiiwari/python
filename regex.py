import re

# phoneNumberRegex = re.compile(r'(\d\d\d\d)-(\d\d\d)-(\d\d\d\d)')
# mo = phoneNumberRegex.search('My number is 1521-555-4242.')
# print('Found phone number: ' + mo.group())

# print('Group 1 :' + mo.group(1))

# print('Group 2 :' + mo.group(2))
# print('Group 3 :' + mo.group(3))
# print(mo.group(0))
# print(mo.groups())

 

# ###escaping paranthesis
# seconPhoneNumner = re.compile(r'(\(\d\d\d\d\))')
# mo2 = seconPhoneNumner.search('my number (1521)')
# print('Found phone number: ' + mo2.group())

# ###pipe character
# heroRegex = re.compile(r'Batman|Shaktiman')
# matched = heroRegex.search('Who is nice,Shaktiman or Batman')
# print(matched.group())

# ##pipe with grouping
# heroRegex = re.compile(r'(Bat|Shakti)man')
# matched = heroRegex.search('Who is nice,Batman or Shaktiman')   
# print(matched.group(1))

# ##optional matching with ?
# batRegex = re.compile(r'bat(wo)?man')
# mo3 = batRegex.search('Adventure of batman')
# print(mo3.group())

# mo4 = batRegex.search('Adventure of batwoman')
# print(mo4.group())

# ##matching with *
# batRegex = re.compile(r'bat(wo)*man')
# mo5 = batRegex.search('batman sucks!')
# print(mo5.group())

# mo5 = batRegex.search('batwoman sucks!')
# print(mo5.group())

# mo5 = batRegex.search('batwowowowowowowoman sucks!')
# print(mo5.group())

# ##matching with +
# batRegex = re.compile(r'bat(wo)+man')
# #mo6 = batRegex.search('batman sucks!')
# #print(mo6.group())

# mo6 = batRegex.search('batwoman sucks!')
# print(mo6.group())

# mo6 = batRegex.search('batwowowowowowowoman sucks!')
# print(mo6.group())

# #matching with {n}
# haRegex = re.compile('(HA){3}')
# mo1 = haRegex.search('I said HAHAHA')
# print(mo1.group())

# mo1 = haRegex.search('I said HaHaHa')
# mo1 == None

# #greedy and non-greedy
# greedyRegex = re.compile(r'(Ha){3,5}')
# mo1 = greedyRegex.search('HaHaHaHaHa')
# print(mo1.group())

# nonGreedyRegex = re.compile(r'(Ha){3,5}?')
# mo2 = nonGreedyRegex.search('HaHaHaHaHa')
# print(mo2.group())

##findall() method with groups

# findallRegex = re.compile(r'(\d\d)-(\d\d)')
# print(findallRegex.findall('My pincode is 70-18,suds pincode is 70-19'))


# ##findall() method without groups

# findallRegex = re.compile(r'\d\d\d\d')
# print(findallRegex.findall('My pincode is 70-18,suds pincode is 70-19'))

# #making my own character class
# charClassRegrex = re.compile(r'[AEIOU]')
# print(charClassRegrex.findall('I Am Don!'))

# #including Range
# rangeRegrex = re.compile(r'[a-zA-Z]')
# print(rangeRegrex.findall('I am number 4 alien H0 H0 H0'))

# rangeRegrex = re.compile(r'[^a-zA-Z]')
# print(rangeRegrex.findall('I am number 4 alien H0 H0 H0'))

#caret and dollar sign
# StartsandEndsRegrex = re.compile(r'^Hello\s\d$')
# mo = StartsandEndsRegrex.search('Hellom 3') == None
# print(mo)

# #wildcard character
# wildcardRegrex = re.compile(r' .at')
# print(wildcardRegrex.findall('I have a rat hat bat and a cat'
#                              ))

#wildcard with star
wildcardwithStarRegex = re.compile(r'First Name : (.*) Last Name : (.*)')
mo2 = wildcardwithStarRegex.search('First Name : Ankita Last Name : Tiwari')
print(mo2.group())