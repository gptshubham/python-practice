# eval()

# # write a program to read employee data from keyboard and print that Data
# ee_no = eval(input('Enter Employee Number: '))
# ee_name = input('Enter Employee Name: ')
# ee_salary = eval(input('Enter Employee Salary: '))
# ee_address = input('Enter Employee Address: ')
# married = eval(input('Enter Weather Married or not ["True" | "False"]'))
#
# print('Please Confirm Your Information :',ee_name,ee_no,ee_salary,married,ee_address,sep='\n')

# result = eval(input('Enter some expression: '))
# print(result)

# # taking list as input from user
# l = eval(input('Enter a list: '))
# print(l, type(l))

# # split()
# l2 = '10 20 30 skg True 15.51'.split()
# print(l2, type(l2))

# # unpacking
# a,b,c = [10,20,30]
# print(a)
# print(a + b + c)

# list comprehension

# # read multiple values from the keyboard in a single line and convert them into list of int values
#
# l3 = [int(x) for x in input('enter values: ').split()]
# print(l3 , type(l3))
# print(l3[0], type(l3[0]))

# # write a program to read 3 float numbers from the keyboard with , seperator and print their sum
# l4 = [float(x) for x in input('Enter 3 floating point numbers seperated by , : ').split(',')]
# total = 0
# for i in l4:
#     total += i
#
# print(total)