#fibonacci sequence using recursion
def fibbo(n):
    if n <=1:
        return n
    else:
        #print(n)
        return(fibbo(n-1)+ fibbo(n-2))

num = int(input('Enter a num : '))


if num<= 0:
    print("Enter a positive integer!!")
else:
    for i in range(1,num +1):
        #print(i)
        result = fibbo(i)
        print(result)



            