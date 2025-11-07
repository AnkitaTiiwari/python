birthday = {
    "kimi" : '2000-01-15',
    "sunny" : '2000-09-09'

}

while True:
    name = input("Enter a name whose bithday you wanna see : ")

    if name == '':
        break
    
    if name in birthday:
        print(name + 's birthday is on ' + birthday[name])
    else:
        print(name + ' is not in the list')
        birthday[name] = input('enter his/her birthday')    
        for name in birthday:
            print(name + ' : ' + birthday[name])
    


