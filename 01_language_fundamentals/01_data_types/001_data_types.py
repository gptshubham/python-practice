from time import clock_getres

x = 10

print(type(x))
# data type
print(id(x))
# memory address
print(x)

# indexing and slicing strings
full_name = 'Shubham Kumar Gupta'

print(full_name[-1])
print(full_name[8:14])

print(full_name[len(full_name)-1:: -1])

# type casting
# int()
x = '12'
print(type(x))

y = int(x)
print(type(y))

x = '12.12'
# y = int(x)
# print(type(y))
# ValueError: invalid literal for int() with base 10: '12.12'

x = 12.12
y = int(x)
print(type(y))

x = '12pointTwelve'
# y = int(x)
# print(type(y))
# ValueError: invalid literal for int() with base 10: '12pointTwelve'
