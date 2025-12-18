#sandwich maker

import pyinputplus as pyIp

bread_dicti = {'wheat':1.5,'white':2.0,'sourdough':2.5}
protein_dicti = {'chicken':3.0,'turkey':2.5,'ham':2.0,'tofu':1.5}
cheese_dicti = {'swiss':2,'cheddar':2.5,'mozzeralla':2.4}
sauce_dicti = {'mayo':0.5,'mustard':0.4}

breadType = pyIp.inputMenu(prompt="Please choose the bread type : \n",choices=['wheat','white','sourdough'])
print(breadType)

proteinType = pyIp.inputMenu(prompt="Please choose the protein type : \n",choices=['chicken','turkey','ham','tofu'])

cheeseChoice = pyIp.inputYesNo(prompt='Do you wanna add cheese : ')

if cheeseChoice == 'yes' :
    cheeseType = pyIp.inputMenu(prompt='which kinda cheese you want',choices=['swiss','cheddar','mozzeralla'])


sauceChoice = pyIp.inputYesNo(prompt='Do you wanna add sauces : ')

if sauceChoice == 'yes':
    sauceType = pyIp.inputMenu(prompt='which kinda sauce you want',choices=['mayo','mustard'])

numberOfSandwiches = pyIp.inputInt(prompt='How many sandwiches you want : ')

totalCost = (bread_dicti[breadType] + protein_dicti[proteinType] + cheese_dicti[cheeseType] + sauce_dicti[sauceType]) * numberOfSandwiches

print(f'Your total cost is : {totalCost}')