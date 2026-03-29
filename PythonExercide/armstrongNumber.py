# Armstrong Number

num = input("Enter a number : ")
input_num = num

#get how many digits
digits = len(str(num))

#empty list to store digits
digits_list = []

#get the digits and store in list
for i in range(digits):
    temp = int(num)% 10
    digits_list.append(temp)
    num = int(num) // 10

#now calculate the armstrong sum by iterating through the list and adding the power of each digit to the sum
armstrong_sum = 0
for i in range(0,digits ):
    armstrong_sum = armstrong_sum + digits_list[i] ** digits

#check if the armstrong sum is equal to the input number and print the results
if int(input_num) == int(armstrong_sum):
    print("Number is a armstrong number")
else:
    print("no its not")